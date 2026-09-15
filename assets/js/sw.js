// {{/* A Go template, rendered once by Hugo into /sw.js (partials/offline-save.html). */}}
/*
  Service worker: offline reading for revelation-today.

  Pages    Network first, so a reader who is online always gets the current
           text. Every page opened is kept, and served from here when the
           network is gone, or slower than SLOW_NETWORK_MS.
  Assets   CSS and JS carry a content hash in their names, so a stored copy is
           never stale: cache first. Images and other unhashed files are
           served from the cache and refreshed behind the scenes.
  Saving   The "save for offline reading" button (js/offline.js) posts a list
           of pages; they are fetched and stored here with the images they use.

  If this ever misbehaves in production, deploy a sw.js whose whole body is
  `self.registration.unregister()`. Browsers check for a new service worker
  on every navigation, so it takes effect on each reader's next visit.
*/
// {{/* The path of baseURL, e.g. /revelation-today/. Not `"/" | relURL`, which is just "/". */}}
// {{ $base := (urls.Parse site.BaseURL).Path }}
const BASE = '{{ $base }}';
const VERSION = '{{ now.Unix }}';
const LANGS = [{{ range site.Languages }}'{{ .Lang }}', {{ end }}];
const DEFAULT_LANG = '{{ range site.Sites }}{{ if eq .Home.RelPermalink $base }}{{ .Language.Lang }}{{ end }}{{ end }}';

const PAGES = 'rt-pages';
const ASSETS = 'rt-assets';
const HASHED = /\.[0-9a-f]{64}\.[a-z]+$/;
const SLOW_NETWORK_MS = 3000;

self.addEventListener('install', () => self.skipWaiting());

self.addEventListener('activate', event => {
  event.waitUntil(self.clients.claim());
  tidy().catch(() => {});
});

self.addEventListener('fetch', event => {
  const request = event.request;
  if (request.method !== 'GET') return;
  const url = new URL(request.url);
  if (url.origin !== location.origin || !url.pathname.startsWith(BASE)) return;

  if (request.mode === 'navigate') {
    event.respondWith(page(event));
  } else if (url.pathname.endsWith('.json')) {
    // search data and the offline index
    event.respondWith(networkFirst(request));
  } else if (['style', 'script', 'image', 'font', 'manifest'].includes(request.destination)) {
    event.respondWith(HASHED.test(url.pathname) ? cacheFirst(request) : staleWhileRevalidate(event));
  }
  // Anything else, including pages quicklink prefetches, goes to the network
  // untouched: only pages a reader actually opens are kept.
});

self.addEventListener('message', event => {
  const message = event.data || {};
  if (message.type === 'save') event.waitUntil(save(message, event.source));
});

async function page(event) {
  const cache = await caches.open(PAGES);
  const network = fetch(event.request);
  event.waitUntil(
    network
      .then(response => (isPage(response) ? storePage(cache, event.request.url, response.clone()) : null))
      .catch(() => {})
  );

  const cached = await matchPage(cache, event.request.url);
  if (!cached) return network.catch(() => offlinePage(event.request.url));

  // Prefer the network, but do not keep a reader waiting on a bad connection.
  const slow = new Promise(resolve => setTimeout(() => resolve(cached), SLOW_NETWORK_MS));
  return Promise.race([network.catch(() => cached), slow]);
}

function isPage(response) {
  return response.ok && response.type === 'basic' &&
    (response.headers.get('content-type') || '').includes('text/html');
}

function pageKey(url) {
  const key = new URL(url);
  key.hash = '';
  key.search = '';
  return key.href;
}

async function matchPage(cache, url) {
  const key = pageKey(url);
  return (await cache.match(key)) || (key.endsWith('/') ? undefined : cache.match(key + '/'));
}

// Stores a page with its title and language alongside, which the offline page
// uses to list what is saved without reading every page.
async function storePage(cache, url, response) {
  const html = await response.text();
  const title = (html.match(/<title>([^<]*)<\/title>/) || [])[1] || '';
  const lang = (html.match(/<html[^>]*\slang="?([\w-]+)/) || [])[1] || '';
  await cache.put(pageKey(url), new Response(html, {
    headers: {
      'content-type': response.headers.get('content-type') || 'text/html; charset=utf-8',
      'x-page-title': encodeURIComponent(title.trim()),
      'x-page-lang': lang,
      'x-saved-at': String(Date.now()),
    },
  }));
  return html;
}

async function offlinePage(url) {
  const first = new URL(url).pathname.slice(BASE.length).split('/')[0];
  const lang = LANGS.includes(first) ? first : DEFAULT_LANG;
  const cache = await caches.open(ASSETS);
  const response = (await cache.match(BASE + lang + '.offline.html')) ||
    (await cache.match(BASE + DEFAULT_LANG + '.offline.html'));
  return response || new Response('Offline', { status: 503, headers: { 'content-type': 'text/plain' } });
}

async function cacheFirst(request) {
  const cache = await caches.open(ASSETS);
  const hit = await cache.match(request);
  if (hit) return hit;
  const response = await fetch(request);
  if (response.ok) await cache.put(request, response.clone());
  return response;
}

async function staleWhileRevalidate(event) {
  const request = event.request;
  const cache = await caches.open(ASSETS);
  const hit = await cache.match(request);
  const refresh = fetch(request).then(async response => {
    if (response.ok) await cache.put(request, response.clone());
    return response;
  });
  event.waitUntil(refresh.catch(() => {}));
  return hit || refresh;
}

async function networkFirst(request) {
  const cache = await caches.open(ASSETS);
  try {
    const response = await fetch(request);
    if (response.ok) await cache.put(request, response.clone());
    return response;
  } catch (error) {
    const hit = await cache.match(request);
    if (hit) return hit;
    throw error;
  }
}

// Fetches and stores `pages`, then the images they use (only those not yet
// stored), and refreshes `assets`. Reports progress to the page that asked.
async function save({ id, pages = [], assets = [] }, client) {
  const pageCache = await caches.open(PAGES);
  const assetCache = await caches.open(ASSETS);
  const queue = pages.slice();
  const images = new Set();
  let done = 0;
  let failed = 0;
  const report = type => client && client.postMessage({ id, type, done, failed, total: pages.length });

  async function worker() {
    while (queue.length) {
      const url = queue.shift();
      try {
        const response = await fetch(url, { cache: 'no-cache' });
        if (!isPage(response)) throw new Error(String(response.status));
        const html = await storePage(pageCache, url, response);
        for (const match of html.matchAll(/<img\s(?:[^>]*?\s)?src="?([^"\s>]+)/g)) {
          const src = new URL(match[1], url);
          if (src.origin === location.origin) images.add(src.href);
        }
      } catch (error) {
        failed++;
      }
      done++;
      report('progress');
    }
  }
  await Promise.all([worker(), worker(), worker(), worker()]);

  await Promise.all(assets.map(url =>
    fetch(url, { cache: 'no-cache' }).then(r => r.ok && assetCache.put(url, r)).catch(() => {})));
  await Promise.all([...images].map(async url => {
    try {
      if (await assetCache.match(url)) return;
      const response = await fetch(url);
      if (response.ok) await assetCache.put(url, response);
    } catch (error) {}
  }));
  report('done');
}

// After a deploy: refresh the offline pages, and drop hashed CSS and JS that
// no stored page refers to any more. Only files fetched before this build are
// dropped, so nothing a page is loading right now can go missing.
async function tidy() {
  const built = Number(VERSION) * 1000;
  const pageCache = await caches.open(PAGES);
  const assetCache = await caches.open(ASSETS);

  for (const request of await assetCache.keys()) {
    if (!request.url.endsWith('.offline.html')) continue;
    try {
      const response = await fetch(request.url, { cache: 'no-cache' });
      if (response.ok) await assetCache.put(request, response);
    } catch (error) {}
  }

  const used = new Set();
  for (const request of await pageCache.keys()) {
    const html = await (await pageCache.match(request)).text();
    for (const match of html.matchAll(/(?:href|src)="?([^"\s>]+)/g)) {
      try { used.add(new URL(match[1], request.url).pathname); } catch (error) {}
    }
  }
  for (const request of await assetCache.keys()) {
    const path = new URL(request.url).pathname;
    if (!HASHED.test(path) || used.has(path)) continue;
    const response = await assetCache.match(request);
    const fetched = Date.parse((response && response.headers.get('date')) || '');
    if (fetched && fetched < built) await assetCache.delete(request);
  }
}
