TYPE_LAW = ["law", 1, {"en": "The law", "de": "Das Gesetz", "tr": "Yasa"}]
TYPE_HISTORY = ["history", 2, {"en": "The history book", "de": "Die Geschichtsbücher", "tr": "TARİH"}]
TYPE_POETRY = ["poetry", 3, {"en": "The poetry", "de": "Die Poesiebücher", "tr": "ŞİİR"}]
TYPE_PROPHETS = ["prophet", 4, {"en": "The prophets", "de": "Die Propheten", "tr": "peygamberler"}]
TYPE_GOSPEL = ["gospel", 5, {"en": "The Gospels", "de": "Die Evangelien", "tr": "İnciller"}]
TYPE_ACTS = ["acts", 6, {"en": "The acts of the aostels", "de": "Die Apostelgeschichte", "tr": "Havarilerin İşleri"}]
TYPE_LETTERS = ["letter", 7, {"en": "The Letters", "de": "Die Briefe", "tr": "Mektuplar"}]
TYPE_REV = ["revelation", 8, {"en": "The Apocalyptic", "de": "Die Apokalypse", "tr": "Apokalypse"}]
BOOK_TYPES = [TYPE_LAW, TYPE_HISTORY, TYPE_POETRY, TYPE_PROPHETS, TYPE_GOSPEL, TYPE_ACTS, TYPE_LETTERS, TYPE_REV]
INDEX = {"en": "Bible reference", "de": "Bibelstellen", "tr": "İncil pasajları"}

INDEX_LANG = {"en": "There are {} used bible verses", "de": "Es gibt {} verwendete Bibelstellen", "tr": "İncil'de kullanılan {} pasajlar vardır"}
TYPE_LANG = {"en": "There are {} used bible verses in this category", "de": "Es gibt {} verwendete Bibelstellen in dieser Kategorie", "tr": "Bu kategoride kullanılan {} Kutsal Kitap pasajı vardır"}
BOOK_LANG = {"en": "There are {} used bible verses in this book", "de": "Es gibt {} verwendete Bibelstellen in diesem Buch", "tr": "Bu kitapta kullanılan {} Kutsal Kitap pasajı vardır"}

BIBLE_HEADER = {"en": "| Verse | Reference |", "de": "| Vers | Referenz |", "tr": "| Ayet | Referans |"}

BOOKS = {
    "gen": {"type": TYPE_LAW[0], "de": "1.Mose", "en": "Genesis", "tr": "Yaratılış"},
    "exo": {"type": TYPE_LAW[0], "de": "2.Mose", "en": "Exodus", "tr": "Mısırdan Çıkış"},
    "lev": {"type": TYPE_LAW[0], "de": "3.Mose", "en": "Leviticus", "tr": "Levililer"},
    "num": {"type": TYPE_LAW[0], "de": "4.Mose", "en": "Numbers", "tr": "Çölde Sayım"},
    "deu": {"type": TYPE_LAW[0], "de": "5.Mose", "en": "Deuteronomy", "tr": "Yasanın Tekrarı"},
    "jos": {"type": TYPE_HISTORY[0], "de": "Josua", "en": "Joshua", "tr": "Yeş"},
    "jdg": {"type": TYPE_HISTORY[0], "de": "Richter", "en": "Judges", "tr": "Hakimler"},
    "rut": {"type": TYPE_HISTORY[0], "de": "Ruth", "en": "Ruth", "tr": "Rut"},
    "1sa": {"type": TYPE_HISTORY[0], "de": "1.Samuel", "en": "1.Samuel", "tr": "1.Samuel"},
    "2sa": {"type": TYPE_HISTORY[0], "de": "2.Samuel", "en": "2.Samuel", "tr": "2.Samuel"},
    "1ki": {"type": TYPE_HISTORY[0], "de": "1.Könige", "en": "1.Kings", "tr": "1.Krallar"},
    "2ki": {"type": TYPE_HISTORY[0], "de": "2.Könige", "en": "2.Kings", "tr": "2.Krallar"},
    "1ch": {"type": TYPE_HISTORY[0], "de": "1.Chronik", "en": "1.Chronicles", "tr": "1.Tarihler"},
    "2ch": {"type": TYPE_HISTORY[0], "de": "2.Chronik", "en": "2.Chronicles", "tr": "2.Tarihler"},
    "ezr": {"type": TYPE_HISTORY[0], "de": "Esra", "en": "Ezra", "tr": "Ezra"},
    "neh": {"type": TYPE_HISTORY[0], "de": "Nehemia", "en": "Nehemiah", "tr": "Nehemya"},
    "est": {"type": TYPE_HISTORY[0], "de": "Ester", "en": "Esther", "tr": "Ester"},
    "job": {"type": TYPE_POETRY[0], "de": "Hiob", "en": "Job", "tr": "Eyüp"},
    "psa": {"type": TYPE_POETRY[0], "de": "Psalm", "en": "Psalm", "tr": "Mezmur"},
    "pro": {"type": TYPE_POETRY[0], "de": "Sprüche", "en": "Proverbs", "tr": "Özdeyişler"},
    "ecc": {"type": TYPE_POETRY[0], "de": "Prediger", "en": "Ecclesiastes", "tr": "Vaiz"},
    "sng": {"type": TYPE_POETRY[0], "de": "Hoheslied", "en": "Song of Solomon", "tr": "Ezgiler Ezgisi"},
    "isa": {"type": TYPE_PROPHETS[0], "de": "Jesaja", "en": "Isaiah", "tr": "Yeşaya"},
    "jer": {"type": TYPE_PROPHETS[0], "de": "Jeremia", "en": "Jeremiah", "tr": "Yeremya"},
    "lam": {"type": TYPE_PROPHETS[0], "de": "Klagelieder", "en": "Lamentations", "tr": "Ağıtlar"},
    "ezk": {"type": TYPE_PROPHETS[0], "de": "Hesekiel", "en": "Ezekiel", "tr": "Hezekiel"},
    "dan": {"type": TYPE_PROPHETS[0], "de": "Daniel", "en": "Daniel", "tr": "Daniel"},
    "hos": {"type": TYPE_PROPHETS[0], "de": "Hosea", "en": "Hosea", "tr": "Hoşea"},
    "jol": {"type": TYPE_PROPHETS[0], "de": "Joel", "en": "Joel", "tr": "Yoel"},
    "amo": {"type": TYPE_PROPHETS[0], "de": "Amos", "en": "Amos", "tr": "Amos"},
    "oba": {"type": TYPE_PROPHETS[0], "de": "Obadja", "en": "Obadiah", "tr": "Ovadya"},
    "jon": {"type": TYPE_PROPHETS[0], "de": "Jona", "en": "Jonah", "tr": "Yunus"},
    "mic": {"type": TYPE_PROPHETS[0], "de": "Micha", "en": "Micah", "tr": "Mika"},
    "nam": {"type": TYPE_PROPHETS[0], "de": "Nahum", "en": "Nahum", "tr": "Nahum"},
    "hab": {"type": TYPE_PROPHETS[0], "de": "Habakuk", "en": "Habbakuk", "tr": "Habakkuk"},
    "zep": {"type": TYPE_PROPHETS[0], "de": "Zefanja", "en": "Zephaniah", "tr": "Sefanya"},
    "hag": {"type": TYPE_PROPHETS[0], "de": "Haggai", "en": "Haggai", "tr": "Hagay"},
    "zec": {"type": TYPE_PROPHETS[0], "de": "Sacharja", "en": "Zechariah", "tr": "Zekeriya"},
    "mal": {"type": TYPE_PROPHETS[0], "de": "Maleachi", "en": "Malachi", "tr": "Malaki"},
    "mat": {"type": TYPE_GOSPEL[0], "de": "Matthäus", "en": "Matthew", "tr": "Matta"},
    "mrk": {"type": TYPE_GOSPEL[0], "de": "Markus", "en": "Mark", "tr": "Markos"},
    "luk": {"type": TYPE_GOSPEL[0], "de": "Lukas", "en": "Luke", "tr": "Luka"},
    "jhn": {"type": TYPE_GOSPEL[0], "de": "Johannes", "en": "John", "tr": "Yuhanna"},
    "act": {"type": TYPE_ACTS[0], "de": "Apostelgeschichte", "en": "Acts", "tr": "Elçilerin İşleri"},
    "rom": {"type": TYPE_LETTERS[0], "de": "Römer", "en": "Romans", "tr": "Romalılar"},
    "1co": {"type": TYPE_LETTERS[0], "de": "1.Korinther", "en": "1.Corinthians", "tr": "1.Korintliler"},
    "2co": {"type": TYPE_LETTERS[0], "de": "2.Korinther", "en": "2.Corinthians", "tr": "2.Korintliler"},
    "gal": {"type": TYPE_LETTERS[0], "de": "Galater", "en": "Galatians", "tr": "Galatyalılar"},
    "eph": {"type": TYPE_LETTERS[0], "de": "Epheser", "en": "Ephesians", "tr": "Efesliler"},
    "php": {"type": TYPE_LETTERS[0], "de": "Philipper", "en": "Philippians", "tr": "Filipililer"},
    "col": {"type": TYPE_LETTERS[0], "de": "Kolosser", "en": "Colossians", "tr": "Koloseliler"},
    "1ti": {"type": TYPE_LETTERS[0], "de": "1.Timotheus", "en": "1.Timothy", "tr": "1.Timoteos"},
    "2ti": {"type": TYPE_LETTERS[0], "de": "2.Timotheus", "en": "2.Timothy", "tr": "2.Timoteos"},
    "1th": {"type": TYPE_LETTERS[0], "de": "1.Thessalonicher", "en": "1.Thessalonians", "tr": "1.Selanikliler"},
    "2th": {"type": TYPE_LETTERS[0], "de": "2.Thessalonicher", "en": "2.Thessalonians", "tr": "2.Selanikliler"},
    "tit": {"type": TYPE_LETTERS[0], "de": "Titus", "en": "Titus", "tr": "Titus"},
    "phm": {"type": TYPE_LETTERS[0], "de": "Philemon", "en": "Philemon", "tr": "Filimon"},
    "heb": {"type": TYPE_LETTERS[0], "de": "Hebräer", "en": "Hebrews", "tr": "İbraniler"},
    "1jn": {"type": TYPE_LETTERS[0], "de": "1.Johannes", "en": "1.John", "tr": "1.Yuhanna"},
    "2jn": {"type": TYPE_LETTERS[0], "de": "2.Johannes", "en": "2.John", "tr": "2.Yuhanna"},
    "3jn": {"type": TYPE_LETTERS[0], "de": "3.Johannes", "en": "3.John", "tr": "3.Yuhanna"},
    "jas": {"type": TYPE_LETTERS[0], "de": "Jakobus", "en": "James", "tr": "Yakup"},
    "1pe": {"type": TYPE_LETTERS[0], "de": "1.Petrus", "en": "1.Peter", "tr": "1.Petrus"},
    "2pe": {"type": TYPE_LETTERS[0], "de": "2.Petrus", "en": "2.Peter", "tr": "2.Petrus"},
    "jud": {"type": TYPE_LETTERS[0], "de": "Judas", "en": "Jude", "tr": "Yahuda"},
    "rev": {"type": TYPE_REV[0], "de": "Offenbarung", "en": "Revelation", "tr": "Vahiy"},
    }
