# -*- coding: utf-8 -*-
"""expl_plan Phase F step 3: the old verse notation ("Dan.11/36-45") in the
visible link text of the bible shortcode. English was converted in 695f632f;
German, Indonesian and Turkish were not.

German writes "Offb 11,5-6", the others "Va 11:5-6". Only the separators change:
the dot between book and chapter becomes a space, the slash becomes the
language's chapter/verse separator. Book abbreviations are left exactly as they
are. Run with --apply to write; without it, it prints the diff.
"""
import io, os, re, sys, collections

ROOT = r'C:\git\revelation-today\exampleSite\content'
SEP = {'de': ',', 'id': ':', 'tr': ':', 'en': ':'}
VAL = re.compile(r'(\{\{% bible val=")([^"]*)(")')
HAS_OLD = re.compile(r'\d\s*/\s*\d')

# two values carry a typo as well: 12/17-13-18 is meant to be 12:17-13:18
TYPO = {'Offb.12/17–13–18': 'Offb 12,17–13,18',
        'Va.12/17–13–18': 'Va 12:17–13:18'}


def convert(v, lang):
    if v in TYPO:
        return TYPO[v]
    out = v
    # the dot that separates a book abbreviation from the chapter number
    out = re.sub(r'(?<=[^\W\d_])\.(?=\d)', ' ', out)
    # the chapter/verse slash
    out = re.sub(r'(?<=\d)\s*/\s*(?=\d)', SEP[lang], out)
    return out


def main(apply):
    changes = collections.defaultdict(list)
    for root, d, fs in os.walk(ROOT):
        if 'bible_ref' in root:
            continue
        for n in fs:
            if not n.endswith('.md'):
                continue
            lang = n.split('.')[-2] if n.count('.') > 1 else 'en'
            if lang not in ('de', 'id', 'tr'):
                lang = 'en'
            p = os.path.join(root, n)
            s = io.open(p, encoding='utf-8').read()
            if not HAS_OLD.search(s):
                continue
            rel = os.path.relpath(p, ROOT).replace(os.sep, '/')
            new_parts = []
            last = 0
            for m in VAL.finditer(s):
                v = m.group(2)
                if not HAS_OLD.search(v):
                    continue
                nv = convert(v, lang)
                if nv == v:
                    continue
                changes[rel].append((v, nv))
                new_parts.append((m.start(2), m.end(2), nv))
            if new_parts and apply:
                for a, b, nv in reversed(new_parts):
                    s = s[:a] + nv + s[b:]
                io.open(p, 'w', encoding='utf-8', newline='').write(s)
    total = sum(len(v) for v in changes.values())
    print(('APPLIED' if apply else 'DRY RUN'), '-', total, 'values in', len(changes), 'files')
    seen = set()
    for f in sorted(changes):
        for o, n in changes[f]:
            if (o, n) in seen:
                continue
            seen.add((o, n))
            print('   %-26s ->  %s' % (o, n))
    return total


if __name__ == '__main__':
    main('--apply' in sys.argv)
