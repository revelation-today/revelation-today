<div align="center">
  <h1 align="center">The Book of Revelation</h1>
  <sup align="center"><a href="README.de.md">Deutsch</a> | <a href="README.md">English</a> ｜ <a href="README.tr.md">TÜRKÇE</a></sup>
  <p align="center">A guide through the fascinating Book of Revelation in the Bible.</p>

The webpage → [https://revelation-today.net](https://revelation-today.github.io/revelation-today/)
</div>

This is based on the Hugo framework using the [Hekstra template](https://imfing.github.io/hextra/).

## Contribution

### Simple edit

- [Register at github](https://github.com/signup?ref_cta=Sign+up&ref_loc=header+logged+out&ref_page=%2F&source=header-home)
- Open the [webpage](https://revelation-today.github.io/revelation-today/)
- Navigate through the page until you find a page you want to change
- If you have a big screen you see a link "**Suggest changes**" on the side, otherwise scroll to the bottom and you see such a link
- Click on the link and login to github
- Click on the **little pen** at the top right just above your text
- If you are done, press "**Commit changes**".
- After this make a useful comment in "Commit message" and if you want ot give more detail in "Extended description". 
- Use "Create a new branch ..." and press "Commit changes"
- Wait until the commit is merged (I need to review) and the change should be visible

## Advanced edit

You need an advanced edit if you want to add pictures, pages or want to work on several files at the same time. For this you need to do the following steps:
- Installation (Make sure that all your installations are included in your **PATH** variable.)
    - [github](https://git-scm.com/)
    - [Hugo (extended version!)](https://gohugo.io/installation/)
    - [go](https://go.dev/)
    - if you work on windows install [powershell](https://learn.microsoft.com/en-us/powershell/scripting/install/installing-powershell-on-windows?view=powershell-7.4)
- Open working directory "<my_git>" 
- Open a command line like "cmd" and check out the repo using "git clone https://github.com/revelation-today/revelation-today.git"
- change to directory "revelation-today"
- Open your powershell and run `npm run dev`
- You should see now your [local webserver](http://localhost:1313/)

Congratulation! Your local server is runnning, now you can make changes

- Open your browser and go into the folder "<my-git>/revelation-today"
- You will find all relevant content there to edit
    - exampleSite/content for the complete content of the webpage
    - static/images for all referenced pictures
    - i18n for translation files
- Make your changes and see the result on your local webserver
- When you are happy with all the changes, commit it on the **powershell** (the installed one not the pre installed windows one)
    - `git checkout -b <your branch name>`
    - `git add .`
    - `git commit -m <your change message>`
    - `git push`
    
Your merge is now visible and can be checked.

## Markdown style

All the pages are written in markdown. 

Here are some guide:
- [basics](https://www.markdownguide.org/basic-syntax/)
- [extended](https://www.markdownguide.org/extended-syntax/)

Summary:
- header: `## <header>`
- unordered list: `- <item>`
- links: `[<link text>](<link>)`
- pictures: `![<picture description>](<path to picture>)` like `![](/images/example.jpg)`
- table: (keep spaces with \|) 
```
| <c1> | <c2> |
|------|------|
| <row> | <row> |
```
