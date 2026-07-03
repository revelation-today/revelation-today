# Translation coverage

A living checklist of what exists in each language, so gaps are visible instead of
discovered by accident. Update this when you add or port content — it doesn't need
to be exact, just roughly current.

Regenerate the raw numbers by counting files under `exampleSite/content/<track>/content/`
(one `.md`/`.<lang>.md` per chapter slug: `vision, letters, worship, seals, army, trumpets,
scroll, witnesses, jesus, beasts, harvest, bowls, harlot, 1000y, paradise`).

## Chapter coverage by track (15 chapters possible)

| Track | EN | DE | TR | IND |
|---|---|---|---|---|
| Poetic story (`story`) | 15/15 | 10/15 | 10/15 | 0/15 |
| Quick summary (`quick`) | 15/15 | 15/15 | 15/15 | 0/15 |
| Application (`appl`) | 15/15 | 15/15 | 15/15 | 0/15 |
| Deep dive (`expl`) | 15/15 | 15/15 | 15/15 | 0/15 |
| Kids (`kids`) | 15/15 | 15/15 | 0/15 | 0/15 |

## Hub pages (`_index.md` for the track itself, e.g. `/quick`)

| Track | EN | DE | TR | IND |
|---|---|---|---|---|
| story | ok | ok | ok | ok |
| quick | ok | ok | ok | **missing** |
| appl | ok | ok | ok | ok |
| expl | ok | ok | ok | ok |
| kids | ok | ok | **missing** | **missing** |

## Known specific gaps

- **Indonesian is a skeleton, not a track.** Every chapter-level page is missing in
  all 5 tracks (0/15 everywhere above). Only hub pages, `welcome`, `about`, `contact`,
  and some of `appl/topics` exist. Treat `ind` as "not started" for content work, not
  "partially translated."
- **Story, German/Turkish: 5 chapters missing** (`army`, `beasts`, `bowls`, `jesus`,
  `paradise`). These predate this round of work — only 10 of the 15 per-chapter story
  pages ever existed in de/tr. Their `story:` front-matter fields intentionally point
  back to `/story/tour` (the single long-form page) instead of a 404, but a de/tr reader
  following the Story card from those 5 chapters loses the "jump to just this bit"
  experience that English/other-complete chapters have.
- **Kids track: Turkish and Indonesian don't exist at all** (0/15, hub missing, tour
  missing). German and English are at parity (15/15).
- **`appl/topics/today/{fear,hero,manipulation,purpose}.md` are English-only** — no
  `.de.md`/`.tr.md`/`.ind.md` counterparts. (`appl/topics/hero/*` and
  `appl/topics/power/*` are fully translated into de/tr.)
- **`/themes` (theme taxonomy) is only tagged for en/de/tr topic articles** — since
  Indonesian has none of the underlying topic articles, and the four English-only
  `today/*` articles above only produce English-only theme terms (`fear`,
  `manipulation`, `purpose`; `hero` also exists in de/tr via the other hero articles).
- **Indonesian UI strings (`i18n/ind.yaml`) aren't being picked up at build time.**
  `ind.yaml` has real translations for every key (`tour: "Tur"`, `contact: "Hubungi
  kami"`, etc.), but the built `ind` site's navbar falls back to the English `name:`
  values regardless (confirmed on pre-existing keys like `tour`/`contact`, not just the
  ones added in this pass) — so this is a pre-existing site bug, not a missing
  translation. Worth a dedicated look at why Hugo isn't loading the `ind` bundle before
  investing more translation effort into that file.

## How to use this

- Before promoting something to the main menu or homepage, check it's not a
  German/English-only feature quietly going live untranslated for tr/ind readers
  (this is what happened with Kids before this checklist existed).
- When you finish porting a track/language, update the table above in the same commit.
