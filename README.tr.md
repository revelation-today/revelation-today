<div align="center">
  <h1 align="center">Vahiy Kitabı</h1>
  <sup align="center"><a href="README.de.md">Deutsch</a> | <a href="README.md">English</a> ｜ <a href="README.tr.md">TÜRKÇE</a></sup>
  <p align="center">Kutsal Kitap'taki büyüleyici Vahiy Kitabı'nda bir rehber.</p>

Web sayfası → [https://revelation-today.net](https://revelation-today.github.io/revelation-today/)
</div>

Bu, [Hekstra şablonu](https://imfing.github.io/hextra/) kullanılarak Hugo çerçevesine dayanmaktadır.

## Katkı

### Basit düzenleme

- [Github'a kaydolun](https://github.com/signup?ref_cta=Sign+up&ref_loc=header+logged+out&ref_page=%2F&source=header-home)
- [Web sayfasını](https://revelation-today.github.io/revelation-today/) açın
- Değiştirmek istediğiniz sayfayı bulana kadar sayfa içinde gezinin
- Büyük bir ekranınız varsa, yan tarafta "**Değişiklik öner**" bağlantısını görürsünüz, aksi takdirde aşağıya kaydırın ve böyle bir bağlantı görürsünüz
- Bağlantıya tıklayın ve github'a giriş yapın
- Metninizin hemen üzerinde sağ üstteki **küçük kaleme** tıklayın **VEYA** uygulamayı yüklediyseniz, üç noktaya gidin ve "Edit in place" ye tıklayın.
- İşiniz bittiyse, "**Commit changes**" düğmesine basın.
- Bundan sonra "Commit message" kısmında faydalı bir yorum yapın ve eğer isterseniz "Extended description" kısmında daha fazla detay verin. 
- "Yeni bir dal oluştur ..." seçeneğini kullanın ve "Değişiklikleri işle" düğmesine basın.
- İşlem birleştirilene kadar bekleyin (gözden geçirmem gerekiyor) ve değişiklik görünür olmalıdır

## Gelişmiş düzenleme

Resim, sayfa eklemek veya aynı anda birkaç dosya üzerinde çalışmak istiyorsanız gelişmiş bir düzenlemeye ihtiyacınız vardır. Bunun için aşağıdaki adımları uygulamanız gerekir:
- Kurulum (Tüm kurulumlarınızın **PATH** değişkeninize dahil edildiğinden emin olun).
    - [github](https://git-scm.com/)
    - [Hugo (genişletilmiş versiyon!)](https://gohugo.io/installation/)
    - [go](https://go.dev/)
    - Windows üzerinde çalışıyorsanız [powershell](https://learn.microsoft.com/en-us/powershell/scripting/install/installing-powershell-on-windows?view=powershell-7.4) yükleyin
- "<my_git>" çalışma dizinini açın 
- "cmd" gibi bir komut satırı açın ve "git clone https://github.com/revelation-today/revelation-today.git" kullanarak repoyu kontrol edin
- "revelation-today" dizinine geç
- **Powershell'inizi** açın (önceden yüklenmiş windows olanı değil, yüklü olanı) ve `npm run dev` komutunu çalıştırın
- Şimdi [yerel web sunucunuzu](http://localhost:1313/) görmelisiniz

Tebrikler! Yerel sunucunuz çalışıyor, artık değişiklik yapabilirsiniz

- kullanarak en son çalışan kopyaya sahip olduğunuzdan emin olun.
    - eski çalışma kopyasını sil
    - `git clone https://github.com/revelation-today/revelation-today.git`
    
veya mevcut çalışma kopyanızda
    - `git checkout main`
    - `git pull`

- Tarayıcınızı açın ve "<my-git>/revelation-today" klasörüne gidin
- Düzenlemek için ilgili tüm içeriği orada bulacaksınız
    - web sayfasının tüm içeriği için exampleSite/content
    - başvurulan tüm resimler için exampleSite/static/images
    - çeviri dosyaları için exampleSite/i18n
- Değişikliklerinizi yapın ve sonucu yerel web sunucunuzda görün
- Tüm değişikliklerden memnun olduğunuzda, **powershell** üzerinde işleyin (önceden yüklenmiş windows olanı değil, yüklü olanı)
    - `git checkout -b <şube adınız>`
    - `git add .`
    - `git commit -m <değişiklik mesajınız>`
    - `git push`
    
Birleştirmeniz artık görünür ve kontrol edilebilir.

## Markdown stili

Tüm sayfalar markdown ile yazılmıştır. 

İşte bazı kılavuzlar:
- [temel bilgiler](https://www.markdownguide.org/basic-syntax/)
- [genişletilmiş](https://www.markdownguide.org/extended-syntax/)

Özet:
- header: `## <başlık>`
- sırasız liste: `- <Öğe>`
- bağlantılar: `[<bağlantı metni>](<link>)`
- dahili sayfaya bağlantı: `{{% int_link val="<Metin>" link="<link>" %}}`
- İncil ayetine bağlantı: `{{% bible val="<Metin>" link="<bölüm>,<ayet>-<ayet>" lang="<DİL>" %}}`
- resimler: `![<resim açıklaması>](<resme giden yol>)` gibi `![](/images/example.jpg)`
- tablo: (boşlukları \| ile saklayın) 
```
| <c1> | <c2> |
|------|------|
| <satır> | <satır> |
```
