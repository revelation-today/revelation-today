# -*- coding: utf-8 -*-
"""Phase G step 4: re-run the greps for every contradiction expl.md says is
resolved, over the whole content tree in all four languages."""
import io, os, re, collections

ROOT = r'C:\git\revelation-today\exampleSite\content'

# (label, regex, note). A hit means the old wording survived somewhere.
CHECKS = [
 ("nine trumpet-plagues (should be six)",
  r"nine (trumpet-)?plagues|neun (Posaunen)?plagen|sembilan tulah|dokuz bela"),
 ("first rider 'calls the two beasts' (old mapping, D4)",
  r"calls the two beasts|ruft die beiden Tiere"),
 ("third horseman as 'economic injustice' (now hunger)",
  r"economic injustice|wirtschaftliche Ungerechtigkeit"),
 ("Ruth half-Moabite",
  r"half-Moabite|halb Moabiterin|separuh Moab|yarı Moav"),
 ("temple rebuilt under Ezra / Nehemiah (should be Zerubbabel / the walls)",
  r"temple was rebuilt under (Ezra|Nehemiah)|Tempel unter (Esra|Nehemia) wieder"),
 ("the curse at Mal 3:10-11 (should be 3:9)",
  r"mal:3,10-11"),
 ("Sardis earthquake 17 BC (should be AD 17)",
  r"17 BC\.? \(?earthquake|earthquake .{0,30}17 BC|17 v\. Chr\..{0,20}[Ee]rdbeben|Erdbeben.{0,20}17 v\. Chr\."),
 ("Smyrna imperial temple AD 20 (should be AD 26)",
  r"temple to AD 20|Tempel auf 20 n\. Chr|bait kekaisaran Smirna pada tahun 20|tapınağını MS 20"),
 ("Antiochus 176 BC (should be 175 king / 167 desecration)",
  r"176 BC|176 v\. Chr|176 SM|MÖ 176"),
 ("Numbers 36 for a daughter's inheritance (should be Num 27)",
  r"Numbers 36|4\. Mose 36|Bilangan 36|Sayılar 36"),
 ("fig tree cited to Rev 17:14 (should be Mark 11)",
  r"fig tree.{0,60}(Revelation|Rev\.?) ?17|Feigenbaum.{0,60}Offenbarung 17"),
 ("church absent 'between chapters 4 and 19' (should be 3 and 21)",
  r"between chapters 4 and 19|zwischen Kapitel 4 und 19"),
 ("Rev 5:13 as heaven/earth/sea/under the sea",
  r"heaven, earth, sea, under the sea|Himmel, Erde, Meer, unter dem Meer"),
 ("full Ephesian citizenship",
  r"full Ephesian citizenship|volle ephesinische Bürgerrecht|kewarganegaraan penuh Efesus|tam Efes vatandaşlığına"),
 ("Prov 7:5 paired with Jas 1:27",
  r"pro:7,5"),
 ("beheading as a privilege of nobility and kings",
  r"nobility and kings|Adel und Könige"),
 ("crucifixion dated AD 31 (the site says AD 30)",
  r"\b31 AD\b|AD 31\b|31 n\. Chr\.|31 M\b|MS 31\b"),
 ("the 1,225 gap as 'over 750 times' (should be more than 1,100)",
  r"factor of over 750|das 750-fache|faktor lebih dari 750|750'den fazla"),
 ("Sadducees favouring increased observance",
  r"Sadducees favor(ed)? increased|Sadduzäer bevorzugten eine stärkere|Saduki lebih memilih ketaatan yang semakin|Sadukiler.{0,40}yasaya bağlılığın artırılmasını tercih"),
 ("'the source article' / 'the accuracy review' in any track",
  r"source article|accuracy review|Quellartikel|Quellenmaterial|Quellmaterial|Ausgangsartikel|Ausgangsmaterial|Genauigkeitsprüfung|Faktenprüfung|tinjauan akurasi|artikel sumber|bahan sumber|doğruluk incelemesi|kaynak makale"),
 ("Babylon instead of Babel in en/de (D9)",
  r"\bBabylon\b"),
]

hits = collections.defaultdict(list)
files = 0
for root, dirs, names in os.walk(ROOT):
    if 'bible_ref' in root:
        continue
    for n in names:
        if not n.endswith('.md'):
            continue
        p = os.path.join(root, n)
        rel = os.path.relpath(p, ROOT).replace('\\', '/')
        lang = n.split('.')[-2] if n.count('.') > 1 else 'en'
        if lang not in ('de', 'id', 'tr'):
            lang = 'en'
        files += 1
        s = io.open(p, encoding='utf-8').read()
        for label, pat in CHECKS:
            # the Babel check only applies to English and German
            if label.startswith('Babylon') and lang not in ('en', 'de'):
                continue
            for m in re.finditer(pat, s, re.I):
                line = s.count('\n', 0, m.start()) + 1
                ctx = s[max(0, m.start()-60):m.end()+60].replace('\n', ' ')
                hits[label].append((rel, line, ctx))

print('files scanned:', files)
print()
out = []
for label, _ in CHECKS:
    h = hits.get(label, [])
    out.append('%-62s %s' % (label[:62], 'clean' if not h else '%d HIT(S)' % len(h)))
print('\n'.join(out))
print()
for label, _ in CHECKS:
    h = hits.get(label, [])
    if not h:
        continue
    print('=' * 20, label, '(%d)' % len(h))
    for rel, line, ctx in h[:14]:
        print('   %s:%s' % (rel, line))
        print('      ...%s...' % ctx.strip()[:150])
    if len(h) > 14:
        print('   ... and %d more' % (len(h) - 14))
