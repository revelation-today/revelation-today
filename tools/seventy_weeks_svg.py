# -*- coding: utf-8 -*-
"""Generate the seventy-weeks diagram in four languages, in the style of numbers-scale.*.svg."""
import io, os

FONT = "Inter, Segoe UI, Helvetica, Arial, sans-serif"
INK = "#1f2328"
MUTED = "#5b636b"
ORANGE = "#d9692b"
ORANGE_BG = "#fbe3d4"
GREEN = "#3f9a2c"
GREEN_BG = "#dcefd6"
BLUE = "#4a6b8a"
BLUE_BG = "#dde6ee"
RULE = "#c7cdd3"


def esc(t):
    return (t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
             .replace("'", "&apos;"))


def text(x, y, s, size=13, fill=INK, anchor="middle", weight="400"):
    if not s:
        return ""
    return ("<text x='%s' y='%s' font-family='%s' font-size='%s' fill='%s' "
            "text-anchor='%s' font-weight='%s'>%s</text>"
            % (x, y, FONT, size, fill, anchor, weight, esc(s)))


def build(L):
    o = []
    o.append("<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 1000 600' role='img' "
             "aria-label='%s'>" % esc(L["alt"]))
    o.append("<rect width='1000' height='600' rx='16' fill='#ffffff'/>")
    o.append(text(500, 40, L["title"], 25, INK, "middle", "700"))
    o.append(text(500, 68, L["subtitle"], 15, MUTED))

    # ---------------- panel A: the count ----------------
    o.append(text(40, 104, L["panelA"], 14, INK, "start", "700"))
    axis_y = 180
    xs = [112, 312, 456, 772, 912]
    # the three drawn stretches and the two pauses
    o.append("<line x1='112' y1='%d' x2='312' y2='%d' stroke='%s' stroke-width='2.5'/>"
             % (axis_y, axis_y, INK))
    o.append("<line x1='312' y1='%d' x2='456' y2='%d' stroke='%s' stroke-width='2.5' "
             "stroke-dasharray='5 7'/>" % (axis_y, axis_y, RULE))
    o.append("<line x1='456' y1='%d' x2='772' y2='%d' stroke='%s' stroke-width='2.5'/>"
             % (axis_y, axis_y, INK))
    o.append("<line x1='772' y1='%d' x2='912' y2='%d' stroke='%s' stroke-width='2.5' "
             "stroke-dasharray='5 7'/>" % (axis_y, axis_y, RULE))
    for x in xs:
        o.append("<line x1='%d' y1='%d' x2='%d' y2='%d' stroke='%s' stroke-width='2.5'/>"
                 % (x, axis_y - 7, x, axis_y + 7, INK))
    for x, (date, lines) in zip(xs, L["anchors"]):
        o.append(text(x, 126, date, 13.5, INK, "middle", "700"))
        for i, ln in enumerate(lines):
            o.append(text(x, 144 + i * 15, ln, 11.5, MUTED))
    mids = [(112 + 312) / 2.0, (312 + 456) / 2.0, (456 + 772) / 2.0, (772 + 912) / 2.0]
    for x, seg in zip(mids, L["segments"]):
        label, is_pause = seg[0], seg[1]
        o.append(text(x, 202, label, 12.5, MUTED if is_pause else INK, "middle",
                      "400" if is_pause else "700"))
        if len(seg) > 2 and seg[2]:
            o.append(text(x, 218, seg[2], 11, MUTED))

    # ---------------- panel B: the week, three times ----------------
    o.append(text(40, 262, L["panelB"], 14, INK, "start", "700"))
    colours = [(ORANGE, ORANGE_BG), (GREEN, GREEN_BG), (BLUE, BLUE_BG)]
    bar_x0, bar_mid, bar_x1 = 290, 570, 850
    for row, (rowdata, (col, bg)) in enumerate(zip(L["rows"], colours)):
        y = 330 + row * 80
        o.append("<rect x='%d' y='%d' width='%d' height='14' rx='7' fill='%s'/>"
                 % (bar_x0, y - 7, bar_x1 - bar_x0, bg))
        o.append("<line x1='%d' y1='%d' x2='%d' y2='%d' stroke='%s' stroke-width='3'/>"
                 % (bar_x0, y, bar_x1, y, col))
        for x in (bar_x0, bar_mid, bar_x1):
            o.append("<circle cx='%d' cy='%d' r='5.5' fill='%s'/>" % (x, y, col))
        caption, sub = rowdata["caption"]
        o.append(text(40, y - 4, caption, 14, col, "start", "700"))
        o.append(text(40, y + 13, sub, 11.5, MUTED, "start"))
        for x, date, desc in zip((bar_x0, bar_mid, bar_x1), rowdata["dates"], rowdata["desc"]):
            o.append(text(x, y - 30, date, 13, INK, "middle", "700"))
            o.append(text(x, y - 15, desc, 11.5, MUTED))
        for x in ((bar_x0 + bar_mid) / 2.0, (bar_mid + bar_x1) / 2.0):
            o.append(text(x, y + 26, L["half"], 11.5, col))

    o.append("<line x1='40' y1='536' x2='960' y2='536' stroke='%s' stroke-width='1'/>" % RULE)
    o.append(text(40, 562, L["footer"], 12.5, MUTED, "start"))
    o.append("</svg>")
    return "".join(o)


EN = {
    "alt": "The seventy weeks: the count with its two pauses, and the last week filled three times",
    "title": "The seventy weeks",
    "subtitle": "7 + 62 weeks with two pauses — and one week filled three times",
    "panelA": "The count",
    "anchors": [
        ("588/587 BC", ["the word to rebuild", "Jerusalem (Jer 30:18)"]),
        ("539 BC", ["Cyrus, the anointed one,", "sends the exiles home"]),
        ("c. 440 BC", ["Jerusalem stands again,", "the walls under Nehemiah"]),
        ("6 BC", ["Jesus is born"]),
        ("AD 27", ["the last week", "begins"]),
    ],
    "segments": [("7 × 7 = 49 years", False), ("the count pauses", True, "about 100 years"),
                 ("62 × 7 = 434 years", False), ("pause", True, "about 30 years")],
    "panelB": "The last week, filled three times",
    "rows": [
        {"caption": ("Antiochus IV", "the first fulfilment"),
         "dates": ["171 BC", "Dec 167 BC", "Dec 164 BC"],
         "desc": ["Onias III cut off", "sacrifice stops", "the temple rededicated"]},
        {"caption": ("Jesus", "the week itself"),
         "dates": ["AD 27", "AD 30", "AD 34"],
         "desc": ["baptised", "the cross", "Stephen is stoned"]},
        {"caption": ("The Jewish war", "the same pattern, 40 years later"),
         "dates": ["AD 66", "AD 70", "AD 73"],
         "desc": ["the war begins", "the temple destroyed", "the war ends"]},
    ],
    "half": "3½ years",
    "footer": "The years are real years. What repeats is the pattern they carry.",
}

DE = {
    "alt": "Die siebzig Wochen: die Zählung mit ihren zwei Pausen und die letzte Woche, dreimal gefüllt",
    "title": "Die siebzig Wochen",
    "subtitle": "7 + 62 Wochen mit zwei Pausen — und eine Woche, dreimal gefüllt",
    "panelA": "Die Zählung",
    "anchors": [
        ("588/587 v. Chr.", ["das Wort, Jerusalem wieder", "aufzubauen (Jer 30,18)"]),
        ("539 v. Chr.", ["Kyrus, der Gesalbte,", "lässt die Verbannten heim"]),
        ("um 440 v. Chr.", ["Jerusalem steht wieder,", "die Mauern unter Nehemia"]),
        ("6 v. Chr.", ["Jesus wird geboren"]),
        ("27 n. Chr.", ["die letzte Woche", "beginnt"]),
    ],
    "segments": [("7 × 7 = 49 Jahre", False), ("die Zählung pausiert", True, "etwa 100 Jahre"),
                 ("62 × 7 = 434 Jahre", False), ("Pause", True, "etwa 30 Jahre")],
    "panelB": "Die letzte Woche, dreimal gefüllt",
    "rows": [
        {"caption": ("Antiochus IV.", "die erste Erfüllung"),
         "dates": ["171 v. Chr.", "Dez. 167 v. Chr.", "Dez. 164 v. Chr."],
         "desc": ["Onias III. ausgerottet", "die Opfer hören auf", "der Tempel neu geweiht"]},
        {"caption": ("Jesus", "die Woche selbst"),
         "dates": ["27 n. Chr.", "30 n. Chr.", "34 n. Chr."],
         "desc": ["Taufe", "das Kreuz", "Steinigung des Stephanus"]},
        {"caption": ("Der jüdische Krieg", "dasselbe Muster, 40 Jahre später"),
         "dates": ["66 n. Chr.", "70 n. Chr.", "73 n. Chr."],
         "desc": ["der Krieg beginnt", "der Tempel zerstört", "der Krieg endet"]},
    ],
    "half": "3½ Jahre",
    "footer": "Die Jahre sind wirkliche Jahre. Was sich wiederholt, ist das Muster, das sie tragen.",
}

ID = {
    "alt": "Ketujuh puluh minggu: hitungan dengan dua jedanya, dan minggu terakhir yang diisi tiga kali",
    "title": "Ketujuh puluh minggu",
    "subtitle": "7 + 62 minggu dengan dua jeda — dan satu minggu yang diisi tiga kali",
    "panelA": "Hitungannya",
    "anchors": [
        ("588/587 SM", ["firman untuk membangun", "kembali Yerusalem (Yer 30:18)"]),
        ("539 SM", ["Koresh, yang diurapi,", "memulangkan buangan"]),
        ("sekitar 440 SM", ["Yerusalem berdiri lagi,", "tembok di bawah Nehemia"]),
        ("6 SM", ["Yesus lahir"]),
        ("27 M", ["minggu terakhir", "dimulai"]),
    ],
    "segments": [("7 × 7 = 49 tahun", False), ("hitungan berhenti", True, "sekitar 100 tahun"),
                 ("62 × 7 = 434 tahun", False), ("jeda", True, "sekitar 30 tahun")],
    "panelB": "Minggu terakhir, diisi tiga kali",
    "rows": [
        {"caption": ("Antiokhus IV", "penggenapan pertama"),
         "dates": ["171 SM", "Des 167 SM", "Des 164 SM"],
         "desc": ["Onias III disingkirkan", "kurban berhenti", "bait ditahbiskan kembali"]},
        {"caption": ("Yesus", "minggu itu sendiri"),
         "dates": ["27 M", "30 M", "34 M"],
         "desc": ["dibaptis", "salib", "Stefanus dirajam"]},
        {"caption": ("Perang Yahudi", "pola yang sama, 40 tahun kemudian"),
         "dates": ["66 M", "70 M", "73 M"],
         "desc": ["perang dimulai", "bait suci dihancurkan", "perang berakhir"]},
    ],
    "half": "3½ tahun",
    "footer": "Tahun-tahun itu tahun yang sungguhan. Yang berulang adalah pola yang dibawanya.",
}

TR = {
    "alt": "Yetmiş hafta: iki duraklamalı sayım ve üç kez doldurulan son hafta",
    "title": "Yetmiş hafta",
    "subtitle": "İki duraklamayla 7 + 62 hafta — ve üç kez doldurulan bir hafta",
    "panelA": "Sayım",
    "anchors": [
        ("MÖ 588/587", ["Yeruşalim'i yeniden kurma", "sözü (Yer 30:18)"]),
        ("MÖ 539", ["Meshedilmiş Koreş", "sürgünleri geri gönderir"]),
        ("MÖ 440 dolayları", ["Yeruşalim yeniden ayakta,", "surlar Nehemya döneminde"]),
        ("MÖ 6", ["İsa doğar"]),
        ("MS 27", ["son hafta", "başlar"]),
    ],
    "segments": [("7 × 7 = 49 yıl", False), ("sayım durur", True, "yaklaşık 100 yıl"),
                 ("62 × 7 = 434 yıl", False), ("duraklama", True, "yaklaşık 30 yıl")],
    "panelB": "Son hafta, üç kez dolduruldu",
    "rows": [
        {"caption": ("IV. Antiohos", "ilk yerine gelme"),
         "dates": ["MÖ 171", "MÖ Aralık 167", "MÖ Aralık 164"],
         "desc": ["III. Onias öldürülür", "kurbanlar durur", "tapınak yeniden adanır"]},
        {"caption": ("İsa", "haftanın kendisi"),
         "dates": ["MS 27", "MS 30", "MS 34"],
         "desc": ["vaftiz", "çarmıh", "İstefanos taşlanır"]},
        {"caption": ("Yahudi savaşı", "aynı örüntü, 40 yıl sonra"),
         "dates": ["MS 66", "MS 70", "MS 73"],
         "desc": ["savaş başlar", "tapınak yıkılır", "savaş biter"]},
    ],
    "half": "3½ yıl",
    "footer": "Yıllar gerçek yıllardır. Yinelenen şey, onların taşıdığı örüntüdür.",
}

out = r'C:\git\revelation-today\exampleSite\static\images'
for code, data in (("en", EN), ("de", DE), ("id", ID), ("tr", TR)):
    p = os.path.join(out, "seventy-weeks.%s.svg" % code)
    io.open(p, "w", encoding="utf-8", newline="").write(build(data))
    print("wrote", p)
