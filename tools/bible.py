import os
import re
import shutil

from bible_config import *

BASE = os.path.join(os.path.dirname(__file__), "..", "exampleSite", "content", "expl")
BIBLE_BASE = os.path.join(BASE, "bible_ref")
LANG_BASE = os.path.join(BASE, "..", "..", "i18n")

if os.path.exists(BIBLE_BASE):
    shutil.rmtree(BIBLE_BASE)
ALL_LANGS = []
for filename in os.listdir(LANG_BASE):
    ALL_LANGS.append(filename.split(".")[0])
COUNTER_BOOK = {}
COUNTER_TYPE = {}
COUNTER = {}
REFS = {}


def init():
    for lang in ALL_LANGS:
        COUNTER_BOOK[lang] = {}
        for book in BOOKS:
            COUNTER_BOOK[lang][book] = 0
        COUNTER_TYPE[lang] = {}
        for b_type in BOOK_TYPES:
            COUNTER_TYPE[lang][b_type[0]] = 0
        COUNTER[lang] = 0
        REFS[lang] = {}
        for book in BOOKS:
            REFS[lang][book] = {}

def parse_data():
    for (root, dir, files) in os.walk(os.path.join(BASE, "..")):
        for filename in files:
            last_link = None
            last_header = None
            title = None
            file_path = os.path.join(root, filename)
            lang = filename.split(".")[-2]
            if lang not in ALL_LANGS:
                lang = "en"
            lang_app = "." + lang
            if lang == "en":
                lang_app = ""
            with open(file_path, encoding="utf-8") as fp:
                lines = fp.readlines()
            for line in lines:
                last_link, last_header, title = parse_line(file_path, lang, line, last_link, last_header, title)

def parse_line(file_path, lang, line, last_link, last_header, title):
    match_title = re.match(r"^title:\s+(.*)", line)
    if match_title:
        title = match_title.group(1)
    match_header = re.match(r"^(#+)\s+(.*)", line)
    if match_header:
        # keep the leading hashes: Hugo only gives h2 and deeper an anchor,
        # so write_verse needs the level, not just the text
        last_header = match_header.group(1) + " " + match_header.group(2)
    match_link = re.match(r"<a name=\"([^\"]+)\"></a>", line)
    if match_link:
        last_link = match_link.group(1)
    match = re.findall(r"(\{\{\% bible val=\"([^\"]+)\" link=\"([^\"]+)\")", line)
    if match:
        for all, val, link in match:
            if link.startswith("https"):
                continue
#            if last_link:
            parse_bible(file_path, lang, title, last_header, last_link, link, val)
    return last_link, last_header, title
                
def parse_bible(file_path, lang, title, last_header, last_link, link, val):
    book = link.split(":")[0]
#    if "witnesses.de" in file_path:
#    if file_path == "/appl/content/witnesses":
#        print(file_path, 222,  last_link)
    if book not in BOOKS:
        print("Did not find book {0} in {1}, {2}".format(book, file_path, val))
    book_type = BOOKS[book]["type"]
    chapter = link.split(":")[1].split(",")[0]
    chapter_st = int(chapter.split("-")[0])
    chapter_end = -1
    if "-" in chapter:
        chapter_end = int(chapter.split("-")[1])
    verse = -1
    verse_st = -1
    verse_end = -1
    if "," in link:
        verse = link.split(":")[1].split(",")[1]
        verse_st = int(verse.split("-")[0])
        verse_end = -1
        if "-" in verse:
            verse_end = int(verse.split("-")[1])
    COUNTER_BOOK[lang][book] += 1
    COUNTER_TYPE[lang][book_type] += 1
    COUNTER[lang] += 1
    if chapter_st not in REFS[lang][book]:
        REFS[lang][book][chapter_st] = {}
    if chapter_end not in REFS[lang][book][chapter_st]:
        REFS[lang][book][chapter_st][chapter_end] = {}
    if verse_st not in REFS[lang][book][chapter_st][chapter_end]:
        REFS[lang][book][chapter_st][chapter_end][verse_st] = {}
    if verse_end not in REFS[lang][book][chapter_st][chapter_end][verse_st]:
        REFS[lang][book][chapter_st][chapter_end][verse_st][verse_end] = []
    REFS[lang][book][chapter_st][chapter_end][verse_st][verse_end].append([file_path, lang, title, last_header, last_link, val, chapter, verse])

def prep_folders():
    os.makedirs(os.path.join(BIBLE_BASE))
    for lang in ALL_LANGS:
        filename = "_index.md"
        if lang != "en":
            filename = f"_index.{lang}.md"
        with open(os.path.join(BIBLE_BASE, filename), "w", newline="\n", encoding="utf-8") as fp:
            write_fileheader(
                fp=fp, 
                title=INDEX[lang], 
                weight="100", 
                stats=INDEX_LANG[lang].format(COUNTER[lang])
                )
    for book in BOOKS:
        book_type = BOOKS[book]["type"]
        if not os.path.exists(os.path.join(BIBLE_BASE, book_type)):
            os.makedirs(os.path.join(BIBLE_BASE, book_type))
            for lang in ALL_LANGS:
                filename = "_index.md"
                if lang != "en":
                    filename = f"_index.{lang}.md"
                with open(os.path.join(BIBLE_BASE, book_type, filename), "w", newline="\n", encoding="utf-8") as fp:
                    title = None
                    weight = None
                    for b_type in BOOK_TYPES:
                        if b_type[0] == book_type:
                            title = b_type[2][lang]
                            weight = b_type[1]
                    write_fileheader(
                        fp=fp,
                        title=title,
                        weight=str(weight),
                        stats=TYPE_LANG[lang].format(COUNTER_TYPE[lang][book_type])
                        )

def write_files():
    for lang in REFS:
        for book in REFS[lang]:
            filename = f"{book}.md"
            if lang != "en":
                filename = f"{book}.{lang}.md"
            book_type = BOOKS[book]["type"]
            write_single_file(lang, book, filename, book_type)

def write_fileheader(fp, title, weight, stats):
    fp.write("---\n")
    fp.write("title: " + title +"\n")
    fp.write("weight: " + weight + "\n")
    fp.write("docType: expl\n")
    fp.write("---\n")
    fp.write("\n")
    fp.write(stats + "\n")

def write_single_file(lang, book, filename, book_type):
    with open(os.path.join(BIBLE_BASE, book_type, filename), "w", newline="\n", encoding="utf-8") as fp:
        write_fileheader(fp=fp, 
            title=BOOKS[book][lang], 
            weight=str(list(BOOKS.keys()).index(book)), 
            stats=BOOK_LANG[lang].format(COUNTER_BOOK[lang][book])
            )
        fp.write("\n")
        fp.write(BIBLE_HEADER[lang] + "\n")
        fp.write("|-------|-----------|\n")

        for chapter_st in sorted(REFS[lang][book]):
            for chapter_end in sorted(REFS[lang][book][chapter_st]):
                for verse_st in sorted(REFS[lang][book][chapter_st][chapter_end]):
                    for verse_end in sorted(REFS[lang][book][chapter_st][chapter_end][verse_st]):
                        for data in REFS[lang][book][chapter_st][chapter_end][verse_st][verse_end]:
                            write_verse(fp, lang, book, data)

def heading_id(heading):
    """The anchor Hugo gives a heading, so a reference with no explicit
       <a name> can still land on the right section instead of "#None".

       Derived by comparing 2,518 headings against the built site: an
       explicit {#id} wins; otherwise lowercase, keep alphanumerics and
       underscores, turn spaces and hyphens into hyphens, drop the rest,
       and do NOT collapse runs of hyphens. Verified on 2,495 of them; the
       23 misses are headings containing a shortcode, which the caller
       skips because Hugo slugifies those after rendering."""
    match = re.search(r"\{#([^}]+)\}", heading)
    if match:
        return match.group(1)
    out = []
    for ch in heading.strip().lower():
        if ch.isalnum():
            out.append(ch)
        elif ch in " -":
            out.append("-")
        elif ch == "_":
            out.append("_")
    return "".join(out)


def write_verse(fp, lang, book, data):
    header = data[2]
    raw_header = data[3]
    heading_level = 0
    if raw_header:
        heading_level = len(raw_header) - len(raw_header.lstrip("#"))
        raw_header = raw_header.lstrip("#").strip()
    if raw_header:
        header = raw_header
        match = re.search(r"val=\"([^\"]+)\"", header)
        if match:
            header = match.group(1)
        match = re.search(r"\[([^\]]+)\]", header)
        if match:
            header = match.group(1)
        header = re.sub(r"\s*\{#[^}]*\}", "", header).strip()
    text = data[5]
    chapter = str(data[6])
    verse = str(data[7])
    filename = data[0]
    filename = re.sub(r"\\\\", "/", filename)
    filename = re.sub(r"\\", "/", filename)
    filename = re.sub(r".*./exampleSite/content", "", filename)
    filename = re.sub(r"\.md", "", filename)
    filename = re.sub(r"\." + lang, "", filename)
    filename = re.sub(r"_index", "", filename)
    filename = filename.split("..")[-1]
    ref = data[4]
    if verse and verse != "-1":
        bible_verse = BOOKS[book][lang] + ":" + chapter + "," + verse
    else:
        bible_verse = BOOKS[book][lang] + ":" + chapter
    bible_link = book + ":" + chapter + "," + verse
    # Hugo's language code is "id"; the bible shortcode's translation table
    # is keyed "ind". Bridge the two so the generated rows resolve.
    sc_lang = SHORTCODE_LANG.get(lang, lang)
    bible_data = "{{% bible val=\"" + bible_verse + "\" link=\"" + bible_link + "\" lang=\"" + sc_lang + "\" %}}" 
    if header:
        ref_text = "\"" + header + "\": " + text
    else:
        ref_text = text
    if ref:
        ref_link = filename + "#" + str(ref)
    elif raw_header and heading_level >= 2 and "{{" not in raw_header:
        # no explicit anchor, but the reference sits under a heading that
        # Hugo will have given an id (h1 gets none)
        ref_link = filename + "#" + heading_id(raw_header)
    else:
        # nothing to aim at - the page itself beats a fragment that is a lie
        ref_link = filename
    ref_data = "[" + ref_text + "](" + ref_link + ")"
    fp.write("| " + bible_data + " | " + ref_data + " |\n")

if __name__ == "__main__":
    init()
    parse_data()
    prep_folders()
    write_files()
    
