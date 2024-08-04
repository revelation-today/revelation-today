TYPE_LAW = ["law", 1, {"en": "The Law", "de": "Das Gesetz", "tr": "Yasa", "ind": "Hukum"}]
TYPE_HISTORY = ["history", 2, {"en": "The History Books", "de": "Die Geschichtsbücher", "tr": "TARİH", "ind": "Buku-buku Sejarah"}]
TYPE_POETRY = ["poetry", 3, {"en": "The poetry", "de": "Die Poesiebücher", "tr": "ŞİİR", "ind": "Puisi"}]
TYPE_PROPHETS = ["prophet", 4, {"en": "The Prophets", "de": "Die Propheten", "tr": "peygamberler", "ind": "Para Nabi"}]
TYPE_GOSPEL = ["gospel", 5, {"en": "The Gospels", "de": "Die Evangelien", "tr": "İnciller", "ind": "Injil"}]
TYPE_ACTS = ["acts", 6, {"en": "The Acts of the Apostels", "de": "Die Apostelgeschichte", "tr": "Havarilerin İşleri", "ind": "Kisah Para Rasul"}]
TYPE_LETTERS = ["letter", 7, {"en": "The Letters", "de": "Die Briefe", "tr": "Mektuplar", "ind": "Surat-surat"}]
TYPE_REV = ["revelation", 8, {"en": "The Apocalyptic Literature", "de": "Die Apokalypse", "tr": "Apokalypse", "ind": "Sastra Apokaliptik"}]
BOOK_TYPES = [TYPE_LAW, TYPE_HISTORY, TYPE_POETRY, TYPE_PROPHETS, TYPE_GOSPEL, TYPE_ACTS, TYPE_LETTERS, TYPE_REV]
INDEX = {"en": "Bible reference", "de": "Bibelstellen", "tr": "İncil pasajları", "ind": "Ayat-ayat Alkitab"}

INDEX_LANG = {"en": "{} bible verses have been referenced.", "de": "{} verwendete Bibelstellen wurden verwendet.", "tr": "İncil'de kullanılan {} pasajlar vardır", "ind": "{} ayat-ayat Alkitab telah dirujuk."}
TYPE_LANG = {"en": "{} bible verses have been referenced in this category.", "de": "{} Bibelstellen wurden in dieser Kategorie verwendet.", "tr": "Bu kategoride kullanılan {} Kutsal Kitap pasajı vardır", "ind": "{} ayat-ayat Alkitab telah dirujuk dalam kategori ini."}
BOOK_LANG = {"en": "{} bible verses have been used in this book.", "de": "{} Bibelstellen wurden in diesem Buch verwendet.", "tr": "Bu kitapta kullanılan {} Kutsal Kitap pasajı vardır", "ind": "{} Ayat-ayat Alkitab telah digunakan dalam buku ini."}

BIBLE_HEADER = {"en": "| Verse | Reference |", "de": "| Vers | Referenz |", "tr": "| Ayet | Referans |", "ind": "| Segar | Referensi |"}

BOOKS = {
    "gen": {"type": TYPE_LAW[0], "de": "1.Mose", "en": "Genesis", "tr": "Yaratılış", "ind": "Kejadian"},
    "exo": {"type": TYPE_LAW[0], "de": "2.Mose", "en": "Exodus", "tr": "Mısırdan Çıkış", "ind": "Keluaran"},
    "lev": {"type": TYPE_LAW[0], "de": "3.Mose", "en": "Leviticus", "tr": "Levililer", "ind": "Imamat"},
    "num": {"type": TYPE_LAW[0], "de": "4.Mose", "en": "Numbers", "tr": "Çölde Sayım", "ind": "Bilangan"},
    "deu": {"type": TYPE_LAW[0], "de": "5.Mose", "en": "Deuteronomy", "tr": "Yasanın Tekrarı", "ind": "Ulangan"},
    "jos": {"type": TYPE_HISTORY[0], "de": "Josua", "en": "Joshua", "tr": "Yeş", "ind": "Yosua"},
    "jdg": {"type": TYPE_HISTORY[0], "de": "Richter", "en": "Judges", "tr": "Hakimler", "ind": "Hakim-hakim"},
    "rut": {"type": TYPE_HISTORY[0], "de": "Ruth", "en": "Ruth", "tr": "Rut", "ind": "Rut"},
    "1sa": {"type": TYPE_HISTORY[0], "de": "1.Samuel", "en": "1.Samuel", "tr": "1.Samuel", "ind": "1 Samuel"},
    "2sa": {"type": TYPE_HISTORY[0], "de": "2.Samuel", "en": "2.Samuel", "tr": "2.Samuel", "ind": "2 Samuel"},
    "1ki": {"type": TYPE_HISTORY[0], "de": "1.Könige", "en": "1.Kings", "tr": "1.Krallar", "ind": "1 Raja-raja"},
    "2ki": {"type": TYPE_HISTORY[0], "de": "2.Könige", "en": "2.Kings", "tr": "2.Krallar", "ind": "2 Raja-raja"},
    "1ch": {"type": TYPE_HISTORY[0], "de": "1.Chronik", "en": "1.Chronicles", "tr": "1.Tarihler", "ind": "1 Tawarikh"},
    "2ch": {"type": TYPE_HISTORY[0], "de": "2.Chronik", "en": "2.Chronicles", "tr": "2.Tarihler", "ind": "2 Tawarikh"},
    "ezr": {"type": TYPE_HISTORY[0], "de": "Esra", "en": "Ezra", "tr": "Ezra", "ind": "Ezra"},
    "neh": {"type": TYPE_HISTORY[0], "de": "Nehemia", "en": "Nehemiah", "tr": "Nehemya", "ind": "Nehemia"},
    "est": {"type": TYPE_HISTORY[0], "de": "Ester", "en": "Esther", "tr": "Ester", "ind": "Ester"},
    "job": {"type": TYPE_POETRY[0], "de": "Hiob", "en": "Job", "tr": "Eyüp", "ind": "Ayub"},
    "psa": {"type": TYPE_POETRY[0], "de": "Psalm", "en": "Psalm", "tr": "Mezmur", "ind": "Mazmur"},
    "pro": {"type": TYPE_POETRY[0], "de": "Sprüche", "en": "Proverbs", "tr": "Özdeyişler", "ind": "Amsal"},
    "ecc": {"type": TYPE_POETRY[0], "de": "Prediger", "en": "Ecclesiastes", "tr": "Vaiz", "ind": "Pengkhotbah"},
    "sng": {"type": TYPE_POETRY[0], "de": "Hoheslied", "en": "Song of Solomon", "tr": "Ezgiler Ezgisi", "ind": "Kidung Agung"},
    "isa": {"type": TYPE_PROPHETS[0], "de": "Jesaja", "en": "Isaiah", "tr": "Yeşaya", "ind": "Yesaya"},
    "jer": {"type": TYPE_PROPHETS[0], "de": "Jeremia", "en": "Jeremiah", "tr": "Yeremya", "ind": "Yeremia"},
    "lam": {"type": TYPE_PROPHETS[0], "de": "Klagelieder", "en": "Lamentations", "tr": "Ağıtlar", "ind": "Ratapan"},
    "ezk": {"type": TYPE_PROPHETS[0], "de": "Hesekiel", "en": "Ezekiel", "tr": "Hezekiel", "ind": "Yehezkiel"},
    "dan": {"type": TYPE_PROPHETS[0], "de": "Daniel", "en": "Daniel", "tr": "Daniel", "ind": "Daniel"},
    "hos": {"type": TYPE_PROPHETS[0], "de": "Hosea", "en": "Hosea", "tr": "Hoşea", "ind": "Hosea"},
    "jol": {"type": TYPE_PROPHETS[0], "de": "Joel", "en": "Joel", "tr": "Yoel", "ind": "Yoel"},
    "amo": {"type": TYPE_PROPHETS[0], "de": "Amos", "en": "Amos", "tr": "Amos", "ind": "Amos"},
    "oba": {"type": TYPE_PROPHETS[0], "de": "Obadja", "en": "Obadiah", "tr": "Ovadya", "ind": "Obaja"},
    "jon": {"type": TYPE_PROPHETS[0], "de": "Jona", "en": "Jonah", "tr": "Yunus", "ind": "Yunus"},
    "mic": {"type": TYPE_PROPHETS[0], "de": "Micha", "en": "Micah", "tr": "Mika", "ind": "Mikha"},
    "nam": {"type": TYPE_PROPHETS[0], "de": "Nahum", "en": "Nahum", "tr": "Nahum", "ind": " Nahum"},
    "hab": {"type": TYPE_PROPHETS[0], "de": "Habakuk", "en": "Habbakuk", "tr": "Habakkuk", "ind": "Habakuk"},
    "zep": {"type": TYPE_PROPHETS[0], "de": "Zefanja", "en": "Zephaniah", "tr": "Sefanya", "ind": "Zefanya"},
    "hag": {"type": TYPE_PROPHETS[0], "de": "Haggai", "en": "Haggai", "tr": "Hagay", "ind": "Hagai"},
    "zec": {"type": TYPE_PROPHETS[0], "de": "Sacharja", "en": "Zechariah", "tr": "Zekeriya", "ind": "Zakharia"},
    "mal": {"type": TYPE_PROPHETS[0], "de": "Maleachi", "en": "Malachi", "tr": "Malaki", "ind": "Maleakhi"},
    "mat": {"type": TYPE_GOSPEL[0], "de": "Matthäus", "en": "Matthew", "tr": "Matta", "ind": "Matius"},
    "mrk": {"type": TYPE_GOSPEL[0], "de": "Markus", "en": "Mark", "tr": "Markos", "ind": "Markus"},
    "luk": {"type": TYPE_GOSPEL[0], "de": "Lukas", "en": "Luke", "tr": "Luka", "ind": "Lukas"},
    "jhn": {"type": TYPE_GOSPEL[0], "de": "Johannes", "en": "John", "tr": "Yuhanna", "ind": "Yohanes"},
    "act": {"type": TYPE_ACTS[0], "de": "Apostelgeschichte", "en": "Acts", "tr": "Elçilerin İşleri", "ind": "Kisah Rasul-rasul"},
    "rom": {"type": TYPE_LETTERS[0], "de": "Römer", "en": "Romans", "tr": "Romalılar", "ind": "Roma"},
    "1co": {"type": TYPE_LETTERS[0], "de": "1.Korinther", "en": "1.Corinthians", "tr": "1.Korintliler", "ind": "1 Korintus"},
    "2co": {"type": TYPE_LETTERS[0], "de": "2.Korinther", "en": "2.Corinthians", "tr": "2.Korintliler", "ind": "2 Korintus"},
    "gal": {"type": TYPE_LETTERS[0], "de": "Galater", "en": "Galatians", "tr": "Galatyalılar", "ind": "Galatia"},
    "eph": {"type": TYPE_LETTERS[0], "de": "Epheser", "en": "Ephesians", "tr": "Efesliler", "ind": "Efesus"},
    "php": {"type": TYPE_LETTERS[0], "de": "Philipper", "en": "Philippians", "tr": "Filipililer", "ind": "Filipi"},
    "col": {"type": TYPE_LETTERS[0], "de": "Kolosser", "en": "Colossians", "tr": "Koloseliler", "ind": "Kolose"},
    "1ti": {"type": TYPE_LETTERS[0], "de": "1.Timotheus", "en": "1.Timothy", "tr": "1.Timoteos", "ind": "1 Timotius"},
    "2ti": {"type": TYPE_LETTERS[0], "de": "2.Timotheus", "en": "2.Timothy", "tr": "2.Timoteos", "ind": "2 Timotius"},
    "1th": {"type": TYPE_LETTERS[0], "de": "1.Thessalonicher", "en": "1.Thessalonians", "tr": "1.Selanikliler", "ind": "1 Tesalonika"},
    "2th": {"type": TYPE_LETTERS[0], "de": "2.Thessalonicher", "en": "2.Thessalonians", "tr": "2.Selanikliler", "ind": "2 Tesalonika"},
    "tit": {"type": TYPE_LETTERS[0], "de": "Titus", "en": "Titus", "tr": "Titus", "ind": "Titus"},
    "phm": {"type": TYPE_LETTERS[0], "de": "Philemon", "en": "Philemon", "tr": "Filimon", "ind": "Filemon"},
    "heb": {"type": TYPE_LETTERS[0], "de": "Hebräer", "en": "Hebrews", "tr": "İbraniler", "ind": "Ibrani"},
    "1jn": {"type": TYPE_LETTERS[0], "de": "1.Johannes", "en": "1.John", "tr": "1.Yuhanna", "ind": "1 Yohanes"},
    "2jn": {"type": TYPE_LETTERS[0], "de": "2.Johannes", "en": "2.John", "tr": "2.Yuhanna", "ind": "2 Yohanes"},
    "3jn": {"type": TYPE_LETTERS[0], "de": "3.Johannes", "en": "3.John", "tr": "3.Yuhanna", "ind": "3 Yohanes"},
    "jas": {"type": TYPE_LETTERS[0], "de": "Jakobus", "en": "James", "tr": "Yakup", "ind": "Yakobus"},
    "1pe": {"type": TYPE_LETTERS[0], "de": "1.Petrus", "en": "1.Peter", "tr": "1.Petrus", "ind": "1 Petrus"},
    "2pe": {"type": TYPE_LETTERS[0], "de": "2.Petrus", "en": "2.Peter", "tr": "2.Petrus", "ind": "2 Petrus"},
    "jud": {"type": TYPE_LETTERS[0], "de": "Judas", "en": "Jude", "tr": "Yahuda", "ind": "Yudas"},
    "rev": {"type": TYPE_REV[0], "de": "Offenbarung", "en": "Revelation", "tr": "Vahiy", "ind": "Wahyu"},
    }
