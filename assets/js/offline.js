// Offline reading: registers the service worker (sw.js) and runs the "save for
// offline reading" button in the footer. main.js is shared by every language,
// so all URLs and wording come from data attributes on #offline-save, rendered
// by partials/offline-save.html.
document.addEventListener("DOMContentLoaded", function () {
  const box = document.getElementById("offline-save");
  if (!box || !("serviceWorker" in navigator) || !("caches" in window)) return;
  const data = box.dataset;
  const container = navigator.serviceWorker;
  const controlled = !!container.controller;
  const offlineURL = new URL(data.offline, location.href).href;

  container.register(data.sw, { scope: data.scope }).catch(function () {});

  // A first visit is not yet served by the service worker, so nothing from it
  // was stored: hand over this page and what it loaded. Later visits are
  // stored as they happen; only the offline page of a language not seen
  // before still has to be fetched.
  container.ready.then(async function (registration) {
    if (!controlled) {
      const scope = new URL(data.scope, location.href).href;
      const assets = performance
        .getEntriesByType("resource")
        .map(function (entry) { return entry.name; })
        .filter(function (url) { return url.startsWith(scope) && !url.endsWith(".json"); });
      assets.push(offlineURL);
      registration.active.postMessage({ type: "save", id: "visit", pages: [location.href.split("#")[0]], assets: assets });
    } else if (!(await caches.match(offlineURL))) {
      registration.active.postMessage({ type: "save", id: "visit", assets: [offlineURL] });
    }
  });

  if (!data.unit) return;

  const button = box.querySelector("button");
  const key = "offline-saved:" + data.unit;
  const values = { title: data.title, n: data.count, done: 0 };
  const fill = function (template) {
    return template.replace(/\{(\w+)\}/g, function (_, name) { return values[name]; });
  };
  let saved = null;
  try { saved = localStorage.getItem(key); } catch (e) {}
  const show = function () {
    button.textContent = saved ? data.tSaved + " · " + data.tUpdate : fill(data.tSave);
  };
  show();
  box.hidden = false;

  button.addEventListener("click", async function () {
    button.disabled = true;
    if (navigator.storage && navigator.storage.persist) navigator.storage.persist().catch(function () {});
    const id = "save-" + Date.now();
    try {
      const index = await (await fetch(data.index)).json();
      const entry = index.find(function (item) { return item.unit === data.unit; });
      const pages = entry ? entry.pages.map(function (path) { return new URL(path, location.href).href; }) : [];
      if (!pages.length) throw new Error("nothing to save");
      values.n = pages.length;
      values.done = 0;
      button.textContent = fill(data.tSaving);

      const registration = await container.ready;
      const result = await new Promise(function (resolve) {
        function listen(event) {
          const message = event.data || {};
          if (message.id !== id) return;
          values.done = message.done;
          if (message.type === "done") {
            container.removeEventListener("message", listen);
            resolve(message);
          } else {
            button.textContent = fill(data.tSaving);
          }
        }
        container.addEventListener("message", listen);
        registration.active.postMessage({ type: "save", id: id, pages: pages });
      });

      if (result.failed) {
        values.done = result.done - result.failed;
        button.textContent = fill(data.tFailed);
      } else {
        saved = String(Date.now());
        try { localStorage.setItem(key, saved); } catch (e) {}
        show();
      }
    } catch (error) {
      button.textContent = fill(data.tFailed);
    }
    button.disabled = false;
  });
});
