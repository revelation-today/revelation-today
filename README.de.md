<div align="center">
  <h1 align="center">Das Buch der Offenbarung</h1>
  <sup align="center"><a href="README.de.md">Deutsch</a> | <a href="README.md">English</a> ｜ <a href="README.tr.md">TÜRKÇE</a></sup>
  <p align="center">Ein Führer durch das faszinierende Buch der Offenbarung in der Bibel.</p>

Die Webseite → [https://revelation-today.net](https://revelation-today.github.io/revelation-today/)
</div>

Dies basiert auf dem Hugo-Framework unter Verwendung der [Hekstra-Vorlage] (https://imfing.github.io/hextra/).

## Mitarbeit

### Einfache Bearbeitung

- [Registrieren bei github](https://github.com/signup?ref_cta=Sign+up&ref_loc=header+logged+out&ref_page=%2F&source=header-home)
- Öffne die [Webseite](https://revelation-today.github.io/revelation-today/)
- Navigiere durch die Seite, bis du eine Seite findest, die du ändern möchtest
- Wenn du einen großen Bildschirm hast, siehst du einen Link "**Änderungsvorschläge**" an der Seite, andernfalls scrolle nach unten und du siehst einen solchen Link
- Klicke auf den Link und melde dich bei github an
- Klicke auf den **kleinen Stift** oben rechts direkt über deinem Text **ODER** wenn du die App installiert hast, gehe auf die drei Punkte und klicke auf "Edit in place".
- Wenn du fertig bist, drücke auf "**Commit changes**".
- Danach gib einen nützlichen Kommentar in "Commit message" und wenn du mehr Details geben willst in "Extended description". 
- Verwende "Create a new branch ..." und drücken "Commit changes".
- Warte, bis der Commit zusammengeführt wurde (ich muss ihn überprüfen) und die Änderung sollte sichtbar sein

## Erweiterte Bearbeitung

Du benötigst eine erweiterte Bearbeitung, wenn du Bilder oder Seiten hinzufügen oder an mehreren Dateien gleichzeitig arbeiten willst. Hierfür mußt du die folgenden Schritte durchführen:
- Installation (Stelle sicher, dass alle Ihre Installationen in deiner **PATH**-Variable enthalten sind.)
    - [github](https://git-scm.com/)
    - [Hugo (erweiterte Version!)](https://gohugo.io/installation/)
    - [go](https://go.dev/)
    - wenn du unter Windows arbeitest, installiere [powershell](https://learn.microsoft.com/en-us/powershell/scripting/install/installing-powershell-on-windows?view=powershell-7.4)
- Öffne das Arbeitsverzeichnis "<my_git>". 
- Öffne eine Befehlszeile wie "cmd" und checke das Repo mit "git clone https://github.com/revelation-today/revelation-today.git" aus
- Wechsle in das Verzeichnis "revelation-today".
- Öffne deine Powershell und führe `npm run dev` aus.
- Du solltest nun deinen [lokalen Webserver](http://localhost:1313/) sehen.

Herzlichen Glückwunsch! Dein lokaler Server läuft, jetzt kannst du Änderungen vornehmen

- Stelle sicher, dass du die neueste Arbeitskopie hast, indem du
    - die alte Arbeitskopie löscht
    - `git clone https://github.com/revelation-today/revelation-today.git`
    
oder bei der bestehenden Arbeitskopie
    - `git checkout main`
    - `git pull`

- Öffne deinen Browser und gehe in den Ordner "<my-git>/revelation-today".
- Dort findest du alle relevanten Inhalte zum Bearbeiten
    - exampleSite/content für den kompletten Inhalt der Webseite
    - exampleSite/static/images für alle referenzierten Bilder
    - exampleSite/i18n für die Übersetzungsdateien
- Nimm deine Änderungen vor und sieh dir das Ergebnis auf Ihrem lokalen Webserver an
- Wenn du mit allen Änderungen zufrieden bist, übertrage sie mit **Powershell** (die installierte Version, nicht die vorinstallierte Windows-Version)
    - `git checkout -b <Name Ihres Zweigs>`
    - `git add .`
    - `git commit -m <Ihre Änderungsnachricht>`
    - `git push`
    
Deine Änderung ist nun sichtbar und kann überprüft werden.

## Markdown-Stil

Alle Seiten sind in Markdown geschrieben. 

Hier sind einige Anleitungen:
- [basics](https://www.markdownguide.org/basic-syntax/)
- [erweitert](https://www.markdownguide.org/extended-syntax/)

Zusammenfassung:
- Kopfzeile: `## <Überschrift>`
- unsortierte Liste: `- <item>`
- Links: `[<Text>](<Link>)`
- Link zur internen Seite: `{{% int_link val="<Text>" link="<Link>" %}}`
- Link zu einem Bibelvers: `{{% bible val="<Text>" link="<Kap>,<Vers>-<Vers>" lang="<Sprache>" %}}`
- Bilder: `![<Bildbeschreibung>](<Pfad zum Bild>)` wie `![](/Bilder/Beispiel.jpg)`
- Tabelle: (Leerzeichen mit \| beibehalten) 
```
| <c1> | <c2> |
|------|------|
| <Zeile> | <Zeile> |
```
