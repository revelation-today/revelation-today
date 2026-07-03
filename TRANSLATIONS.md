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
| Poetic story (`story`) | 15/15 | 15/15 | 15/15 | 15/15 |
| Quick summary (`quick`) | 15/15 | 15/15 | 15/15 | 15/15 |
| Application (`appl`) | 15/15 | 15/15 | 15/15 | 15/15 |
| Deep dive (`expl`) | 15/15 | 15/15 | 15/15 | 15/15 |
| Kids (`kids`) | 15/15 | 15/15 | 15/15 | 15/15 |

All four languages are now at full chapter-level parity across all five tracks.

## Hub pages (`_index.md` for the track itself, e.g. `/quick`)

| Track | EN | DE | TR | IND |
|---|---|---|---|---|
| story | ok | ok | ok | ok |
| quick | ok | ok | ok | ok |
| appl | ok | ok | ok | ok |
| expl | ok | ok | ok | ok |
| kids | ok | ok | ok | ok |

## Deep dive (`expl`) extras beyond the 15 chapter hubs

`expl` has a lot of content beyond the one-hub-per-chapter table above: multiple detail
articles per chapter folder, plus `expl/background`, `expl/bible`, and `expl/topics`.
These are now also at full en/de/tr/ind parity (roughly 174 files per language, matching
German — the previously-complete reference language).

## Remaining known gaps

- **`/kids/lessons/*` (51 full Sunday-school lesson plans, ported from `sermon_kids/`)
  is still German-only by design** — the source material only exists in German, and
  porting 51 long lesson plans to en/tr/ind is a separate, much bigger job than
  incorporating them. Don't link to it from non-German hub pages until/unless it's
  translated.
- **Indonesian UI strings (`i18n/ind.yaml`) still aren't being picked up at build
  time.** `ind.yaml` has real translations for every key (`tour: "Tur"`, `contact:
  "Hubungi kami"`, etc.), but the built `ind` site's navbar falls back to the English
  `name:` values regardless (confirmed on pre-existing keys like `tour`/`contact`, not
  just newly-added ones) — this is a pre-existing site/template bug, not a missing
  translation, and content parity doesn't fix it. Worth a dedicated look at why Hugo
  isn't loading the `ind` i18n bundle.
- **A handful of pre-existing content quirks were carried over faithfully during this
  translation pass rather than silently "fixed"** (since fixing content during a
  translation task risks introducing inconsistencies across languages):
  - `appl/content/vision` and `appl/content/letters` (German, and now also Indonesian)
    have duplicated content between the two files.
  - `expl/topics/others/judgment-in-the-book-of-revelation` has a malformed markdown
    table in German (now also Indonesian).
  - `appl/topics/hero/who-rules-the-world.ind.md` references `era_en.jpg` since no
    `era_ind.jpg` exists.
  - These are worth cleaning up separately, in whichever language they're first
    noticed, rather than as a "translation" change.
- **Minor terminology/quality note**: the Indonesian content was produced by six
  parallel translation passes (one per track) rather than a single pass, so there may
  be small cross-track terminology inconsistencies (e.g. a term rendered slightly
  differently in `expl` vs `appl`) that a native-speaker read-through would catch.
  Spot-checks during this pass found the terminology reasonably consistent (each pass
  was told to match existing site usage), but this hasn't been exhaustively verified.

## How to use this

- Before promoting something to the main menu or homepage, check it's not a
  German/English-only feature quietly going live untranslated for tr/ind readers
  (this is what happened with Kids before this checklist existed).
- When you finish porting a track/language, update the table above in the same commit.
