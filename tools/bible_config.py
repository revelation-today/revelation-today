TYPE_LAW = ["law", 1, {"en": "The Law", "de": "Das Gesetz", "tr": "Yasa", "id": "Hukum"}]
TYPE_HISTORY = ["history", 2, {"en": "The History Books", "de": "Die Geschichtsbücher", "tr": "TARİH", "id": "Buku-buku Sejarah"}]
TYPE_POETRY = ["poetry", 3, {"en": "The poetry", "de": "Die Poesiebücher", "tr": "ŞİİR", "id": "Puisi"}]
TYPE_PROPHETS = ["prophet", 4, {"en": "The Prophets", "de": "Die Propheten", "tr": "peygamberler", "id": "Para Nabi"}]
TYPE_GOSPEL = ["gospel", 5, {"en": "The Gospels", "de": "Die Evangelien", "tr": "İnciller", "id": "Injil"}]
TYPE_ACTS = ["acts", 6, {"en": "The Acts of the Apostels", "de": "Die Apostelgeschichte", "tr": "Havarilerin İşleri", "id": "Kisah Para Rasul"}]
TYPE_LETTERS = ["letter", 7, {"en": "The Letters", "de": "Die Briefe", "tr": "Mektuplar", "id": "Surat-surat"}]
TYPE_REV = ["revelation", 8, {"en": "The Apocalyptic Literature", "de": "Die Apokalypse", "tr": "Apokalypse", "id": "Sastra Apokaliptik"}]
BOOK_TYPES = [TYPE_LAW, TYPE_HISTORY, TYPE_POETRY, TYPE_PROPHETS, TYPE_GOSPEL, TYPE_ACTS, TYPE_LETTERS, TYPE_REV]
INDEX = {"en": "Bible reference", "de": "Bibelstellen", "tr": "İncil pasajları", "id": "Ayat-ayat Alkitab"}

INDEX_LANG = {"en": "{} bible verses have been referenced.", "de": "{} verwendete Bibelstellen wurden verwendet.", "tr": "İncil'de kullanılan {} pasajlar vardır", "id": "{} ayat-ayat Alkitab telah dirujuk."}
TYPE_LANG = {"en": "{} bible verses have been referenced in this category.", "de": "{} Bibelstellen wurden in dieser Kategorie verwendet.", "tr": "Bu kategoride kullanılan {} Kutsal Kitap pasajı vardır", "id": "{} ayat-ayat Alkitab telah dirujuk dalam kategori ini."}
BOOK_LANG = {"en": "{} bible verses have been used in this book.", "de": "{} Bibelstellen wurden in diesem Buch verwendet.", "tr": "Bu kitapta kullanılan {} Kutsal Kitap pasajı vardır", "id": "{} Ayat-ayat Alkitab telah digunakan dalam buku ini."}

BIBLE_HEADER = {"en": "| Verse | Reference |", "de": "| Vers | Referenz |", "tr": "| Ayet | Referans |", "id": "| Segar | Referensi |"}

BOOKS = {
    "gen": {"type": TYPE_LAW[0], "de": "1.Mose", "en": "Genesis", "tr": "Yaratılış", "id": "Kejadian"},
    "exo": {"type": TYPE_LAW[0], "de": "2.Mose", "en": "Exodus", "tr": "Mısırdan Çıkış", "id": "Keluaran"},
    "lev": {"type": TYPE_LAW[0], "de": "3.Mose", "en": "Leviticus", "tr": "Levililer", "id": "Imamat"},
    "num": {"type": TYPE_LAW[0], "de": "4.Mose", "en": "Numbers", "tr": "Çölde Sayım", "id": "Bilangan"},
    "deu": {"type": TYPE_LAW[0], "de": "5.Mose", "en": "Deuteronomy", "tr": "Yasanın Tekrarı", "id": "Ulangan"},
    "jos": {"type": TYPE_HISTORY[0], "de": "Josua", "en": "Joshua", "tr": "Yeş", "id": "Yosua"},
    "jdg": {"type": TYPE_HISTORY[0], "de": "Richter", "en": "Judges", "tr": "Hakimler", "id": "Hakim-hakim"},
    "rut": {"type": TYPE_HISTORY[0], "de": "Ruth", "en": "Ruth", "tr": "Rut", "id": "Rut"},
    "1sa": {"type": TYPE_HISTORY[0], "de": "1.Samuel", "en": "1.Samuel", "tr": "1.Samuel", "id": "1 Samuel"},
    "2sa": {"type": TYPE_HISTORY[0], "de": "2.Samuel", "en": "2.Samuel", "tr": "2.Samuel", "id": "2 Samuel"},
    "1ki": {"type": TYPE_HISTORY[0], "de": "1.Könige", "en": "1.Kings", "tr": "1.Krallar", "id": "1 Raja-raja"},
    "2ki": {"type": TYPE_HISTORY[0], "de": "2.Könige", "en": "2.Kings", "tr": "2.Krallar", "id": "2 Raja-raja"},
    "1ch": {"type": TYPE_HISTORY[0], "de": "1.Chronik", "en": "1.Chronicles", "tr": "1.Tarihler", "id": "1 Tawarikh"},
    "2ch": {"type": TYPE_HISTORY[0], "de": "2.Chronik", "en": "2.Chronicles", "tr": "2.Tarihler", "id": "2 Tawarikh"},
    "ezr": {"type": TYPE_HISTORY[0], "de": "Esra", "en": "Ezra", "tr": "Ezra", "id": "Ezra"},
    "neh": {"type": TYPE_HISTORY[0], "de": "Nehemia", "en": "Nehemiah", "tr": "Nehemya", "id": "Nehemia"},
    "est": {"type": TYPE_HISTORY[0], "de": "Ester", "en": "Esther", "tr": "Ester", "id": "Ester"},
    "job": {"type": TYPE_POETRY[0], "de": "Hiob", "en": "Job", "tr": "Eyüp", "id": "Ayub"},
    "psa": {"type": TYPE_POETRY[0], "de": "Psalm", "en": "Psalm", "tr": "Mezmur", "id": "Mazmur"},
    "pro": {"type": TYPE_POETRY[0], "de": "Sprüche", "en": "Proverbs", "tr": "Özdeyişler", "id": "Amsal"},
    "ecc": {"type": TYPE_POETRY[0], "de": "Prediger", "en": "Ecclesiastes", "tr": "Vaiz", "id": "Pengkhotbah"},
    "sng": {"type": TYPE_POETRY[0], "de": "Hoheslied", "en": "Song of Solomon", "tr": "Ezgiler Ezgisi", "id": "Kidung Agung"},
    "isa": {"type": TYPE_PROPHETS[0], "de": "Jesaja", "en": "Isaiah", "tr": "Yeşaya", "id": "Yesaya"},
    "jer": {"type": TYPE_PROPHETS[0], "de": "Jeremia", "en": "Jeremiah", "tr": "Yeremya", "id": "Yeremia"},
    "lam": {"type": TYPE_PROPHETS[0], "de": "Klagelieder", "en": "Lamentations", "tr": "Ağıtlar", "id": "Ratapan"},
    "ezk": {"type": TYPE_PROPHETS[0], "de": "Hesekiel", "en": "Ezekiel", "tr": "Hezekiel", "id": "Yehezkiel"},
    "dan": {"type": TYPE_PROPHETS[0], "de": "Daniel", "en": "Daniel", "tr": "Daniel", "id": "Daniel"},
    "hos": {"type": TYPE_PROPHETS[0], "de": "Hosea", "en": "Hosea", "tr": "Hoşea", "id": "Hosea"},
    "jol": {"type": TYPE_PROPHETS[0], "de": "Joel", "en": "Joel", "tr": "Yoel", "id": "Yoel"},
    "amo": {"type": TYPE_PROPHETS[0], "de": "Amos", "en": "Amos", "tr": "Amos", "id": "Amos"},
    "oba": {"type": TYPE_PROPHETS[0], "de": "Obadja", "en": "Obadiah", "tr": "Ovadya", "id": "Obaja"},
    "jon": {"type": TYPE_PROPHETS[0], "de": "Jona", "en": "Jonah", "tr": "Yunus", "id": "Yunus"},
    "mic": {"type": TYPE_PROPHETS[0], "de": "Micha", "en": "Micah", "tr": "Mika", "id": "Mikha"},
    "nam": {"type": TYPE_PROPHETS[0], "de": "Nahum", "en": "Nahum", "tr": "Nahum", "id": " Nahum"},
    "hab": {"type": TYPE_PROPHETS[0], "de": "Habakuk", "en": "Habbakuk", "tr": "Habakkuk", "id": "Habakuk"},
    "zep": {"type": TYPE_PROPHETS[0], "de": "Zefanja", "en": "Zephaniah", "tr": "Sefanya", "id": "Zefanya"},
    "hag": {"type": TYPE_PROPHETS[0], "de": "Haggai", "en": "Haggai", "tr": "Hagay", "id": "Hagai"},
    "zec": {"type": TYPE_PROPHETS[0], "de": "Sacharja", "en": "Zechariah", "tr": "Zekeriya", "id": "Zakharia"},
    "mal": {"type": TYPE_PROPHETS[0], "de": "Maleachi", "en": "Malachi", "tr": "Malaki", "id": "Maleakhi"},
    "mat": {"type": TYPE_GOSPEL[0], "de": "Matthäus", "en": "Matthew", "tr": "Matta", "id": "Matius"},
    "mrk": {"type": TYPE_GOSPEL[0], "de": "Markus", "en": "Mark", "tr": "Markos", "id": "Markus"},
    "luk": {"type": TYPE_GOSPEL[0], "de": "Lukas", "en": "Luke", "tr": "Luka", "id": "Lukas"},
    "jhn": {"type": TYPE_GOSPEL[0], "de": "Johannes", "en": "John", "tr": "Yuhanna", "id": "Yohanes"},
    "act": {"type": TYPE_ACTS[0], "de": "Apostelgeschichte", "en": "Acts", "tr": "Elçilerin İşleri", "id": "Kisah Rasul-rasul"},
    "rom": {"type": TYPE_LETTERS[0], "de": "Römer", "en": "Romans", "tr": "Romalılar", "id": "Roma"},
    "1co": {"type": TYPE_LETTERS[0], "de": "1.Korinther", "en": "1.Corinthians", "tr": "1.Korintliler", "id": "1 Korintus"},
    "2co": {"type": TYPE_LETTERS[0], "de": "2.Korinther", "en": "2.Corinthians", "tr": "2.Korintliler", "id": "2 Korintus"},
    "gal": {"type": TYPE_LETTERS[0], "de": "Galater", "en": "Galatians", "tr": "Galatyalılar", "id": "Galatia"},
    "eph": {"type": TYPE_LETTERS[0], "de": "Epheser", "en": "Ephesians", "tr": "Efesliler", "id": "Efesus"},
    "php": {"type": TYPE_LETTERS[0], "de": "Philipper", "en": "Philippians", "tr": "Filipililer", "id": "Filipi"},
    "col": {"type": TYPE_LETTERS[0], "de": "Kolosser", "en": "Colossians", "tr": "Koloseliler", "id": "Kolose"},
    "1ti": {"type": TYPE_LETTERS[0], "de": "1.Timotheus", "en": "1.Timothy", "tr": "1.Timoteos", "id": "1 Timotius"},
    "2ti": {"type": TYPE_LETTERS[0], "de": "2.Timotheus", "en": "2.Timothy", "tr": "2.Timoteos", "id": "2 Timotius"},
    "1th": {"type": TYPE_LETTERS[0], "de": "1.Thessalonicher", "en": "1.Thessalonians", "tr": "1.Selanikliler", "id": "1 Tesalonika"},
    "2th": {"type": TYPE_LETTERS[0], "de": "2.Thessalonicher", "en": "2.Thessalonians", "tr": "2.Selanikliler", "id": "2 Tesalonika"},
    "tit": {"type": TYPE_LETTERS[0], "de": "Titus", "en": "Titus", "tr": "Titus", "id": "Titus"},
    "phm": {"type": TYPE_LETTERS[0], "de": "Philemon", "en": "Philemon", "tr": "Filimon", "id": "Filemon"},
    "heb": {"type": TYPE_LETTERS[0], "de": "Hebräer", "en": "Hebrews", "tr": "İbraniler", "id": "Ibrani"},
    "1jn": {"type": TYPE_LETTERS[0], "de": "1.Johannes", "en": "1.John", "tr": "1.Yuhanna", "id": "1 Yohanes"},
    "2jn": {"type": TYPE_LETTERS[0], "de": "2.Johannes", "en": "2.John", "tr": "2.Yuhanna", "id": "2 Yohanes"},
    "3jn": {"type": TYPE_LETTERS[0], "de": "3.Johannes", "en": "3.John", "tr": "3.Yuhanna", "id": "3 Yohanes"},
    "jas": {"type": TYPE_LETTERS[0], "de": "Jakobus", "en": "James", "tr": "Yakup", "id": "Yakobus"},
    "1pe": {"type": TYPE_LETTERS[0], "de": "1.Petrus", "en": "1.Peter", "tr": "1.Petrus", "id": "1 Petrus"},
    "2pe": {"type": TYPE_LETTERS[0], "de": "2.Petrus", "en": "2.Peter", "tr": "2.Petrus", "id": "2 Petrus"},
    "jud": {"type": TYPE_LETTERS[0], "de": "Judas", "en": "Jude", "tr": "Yahuda", "id": "Yudas"},
    "rev": {"type": TYPE_REV[0], "de": "Offenbarung", "en": "Revelation", "tr": "Vahiy", "id": "Wahyu"},
    }

# Hugo language code -> the lang value the bible shortcode expects.
SHORTCODE_LANG = {"id": "ind"}
