# -*- coding: utf-8 -*-
"""Sort the open items in todo/expl.md by whether they are already fixed.

For each `- [ ]` item it takes the phrases the item puts in quotes — what the
item complains about — and looks for them in the live English page named by the
nearest `### ` heading. Items whose phrases are gone are candidates for ticking.

THIS IS A SORTING AID, NOT A VERDICT. Read every candidate against the page
before ticking it. On the 2026-10-07 run it was wrong in both directions until
three rounds of tightening, and it is still wrong sometimes. The traps:

  * a `{{% bible %}}` shortcode splits a quoted phrase, so the phrase looks gone
    -> shortcodes are replaced by their `val` text before matching;
  * quote marks and emphasis inside the phrase break the match
    -> both are stripped from page and phrase;
  * the reviewer splices in a reference or an ellipsis that is not on the page
    -> only contiguous runs of 20+ characters are looked for;
  * some items quote the text they want ADDED, not removed. Uzzah's missing
    1 Chr 15:13-15 reads as "gone" precisely because it is still missing.
    Nothing can fix this one automatically; it needs a reader.

Usage:  python tools/stale_check.py      (writes sweep.json next to the cwd)
"""
import io, sys, re, os, json
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

TODO = r"C:/Users/hagen/Dropbox/Bibel/revelation_app/todo/expl.md"
SITE = r"C:/git/revelation-today/exampleSite/content/expl"

lines = open(TODO, encoding="utf-8").read().split("\n")

items = []
section = None
page = None
i = 0
while i < len(lines):
    l = lines[i]
    if re.match(r"^## \d", l) or l.startswith("## 10"):
        section = l.strip("# ").strip()
        page = None
    m = re.match(r"^### `?([^`]+)`?", l)
    if m:
        cand = m.group(1).strip()
        page = cand if cand.endswith(".md") else None
    if l.startswith("- [ ]"):
        block = [l]
        j = i + 1
        while j < len(lines) and not lines[j].startswith("- [") and not lines[j].startswith("#"):
            block.append(lines[j])
            j += 1
        items.append({"line": i + 1, "section": section, "page": page,
                      "text": "\n".join(block).strip()})
        i = j
        continue
    i += 1

print("open items parsed:", len(items))

QUOTE = re.compile(r'[\u201c"\u201e]([^\u201d"\u201c\u201e]{12,})[\u201d"\u201c]')


SC = re.compile(r'\{\{%\s*(?:bible|int_link)\s+val="([^"]*)"[^%]*%\}\}')


def norm(s):
    s = SC.sub(lambda m: m.group(1), s)       # shortcode -> its visible text
    s = re.sub(r"\{\{%[^%]*%\}\}", " ", s)    # any other shortcode -> space
    s = s.replace("\u2019", "'").replace("\u2018", "'")
    s = s.replace("\u201c", '"').replace("\u201d", '"').replace("\u201e", '"')
    s = s.replace("\u2014", "-").replace("\u2013", "-").replace("\u2026", "...")
    s = re.sub(r'["\u201c\u201d\u201e\u2018\u2019\'*_]', "", s)   # quotes and emphasis
    s = re.sub(r"\s+", " ", s)
    return s.lower()


cache = {}


def page_text(rel):
    if rel not in cache:
        p = os.path.join(SITE, rel.replace("/", os.sep))
        cache[rel] = norm(open(p, encoding="utf-8").read()) if os.path.exists(p) else None
    return cache[rel]


gone, present, unknown = [], [], []
for it in items:
    frags = [f for f in QUOTE.findall(it["text"])]
    # strip ellipsis-joined pieces: test the longest contiguous run
    tests = []
    for f in frags:
        # the review author often splices in an ellipsis, a parenthetical
        # reference or a slash; only contiguous runs can be looked for
        for part in re.split(r"\u2026|\.\.\.|[()\[\]/]|\u2192", f):
            part = part.strip(" ,;:-\u2014\u2013")
            if len(part) >= 20:
                tests.append(part)
    t = page_text(it["page"]) if it["page"] else None
    if t is None or not tests:
        it["why"] = "no page" if t is None else "no quoted fragment"
        unknown.append(it)
        continue
    hits = [x for x in tests if norm(x) in t]
    it["tests"] = tests
    it["hits"] = hits
    if hits:
        present.append(it)
    else:
        gone.append(it)

print("fragment still on the page (likely still open):", len(present))
print("fragment gone (likely already fixed):          ", len(gone))
print("needs reading by hand:                         ", len(unknown))

json.dump({"gone": gone, "present": present, "unknown": unknown},
          open("sweep.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("\nwrote sweep.json")
