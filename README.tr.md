<div align="center">
<a href="README.md"><img src="assets/lang-en.svg" height="40" alt="English"/></a>
<a href="README.ar.md"><img src="assets/lang-ar.svg" height="40" alt="العربية"/></a>
<a href="README.tr.md"><img src="assets/lang-tr-on.svg" height="40" alt="Türkçe"/></a>
</div>


<img src="assets/tr/hero.svg" width="100%" alt="Ranim: diplomayla mühendis, alışkanlıkla editör ve tasarımcı. Sağlam şeyler inşa etmek üzerine kısa bir film."/>

> **Özet:** Tam kapsamlı ürünler çıkaran, ML deneylerini dürüstçe yürüten ve çevresindeki görselleri tasarlayıp kurgulayan son sınıf yazılım mühendisliği öğrencisi.

<img src="assets/tr/s0.svg" width="100%" alt="Giriş: kameranın arkasındaki kişi"/>

Ben Ranim, İstanbul'da İstinye Üniversitesi'nde yazılım mühendisliği son sınıf öğrencisiyim. İngilizce, Arapça ve Türkçe çalışıyorum ve zamanımı üç zanaat arasında bölüyorum: yazılım geliştirmek, video kurgulamak ve görsel tasarlamak. Üçünün ortak noktası benim için en önemli kısım: bir şeyi anlaşılır kılmak ve biri onu zorladığında ayakta kalmasını sağlamak. Bu sayfa, yönetmen kurgusu.

<img src="assets/tr/s1.svg" width="100%" alt="Sahne 1: Orcha, yapay zekâ ajanlarını kim izliyor?"/>

<img src="assets/tr/d-orcha.svg" width="100%" alt="Şema: WhatsApp, sesli arama, web sohbeti ve e-postadaki yapay zekâ ajanları Orcha'ya akar, ardından müşteriye ulaşmadan önce insan incelemesinden (onayla, düzenle, reddet) geçer."/>

Şirketler yapay zekâ ajanlarını WhatsApp'a, telefon hatlarına, web sohbetine ve e-postaya yerleştiriyor. Sonra pratik bir soru çıkıyor: **Bu ajanları kim izliyor?** Orcha benim cevabım. Bir ekibin çalıştırdığı her ajan için tek kontrol paneli: görevler, müşteri kayıtları, olay günlükleri ve analitik; ayrıca işaretlenen çıktının müşteriye ulaşmadan *önce* bir insan tarafından onaylandığı, düzenlendiği ya da reddedildiği bir inceleme kuyruğu.

Çok kiracılı (multi-tenant) yapıda; rol tabanlı erişim, JWT kimlik doğrulama, e-posta doğrulama ve hız sınırlama içeriyor. Railway üzerinde yayında, Nginx arkasında Docker ile çalışıyor ve 7 Playwright uçtan uca testiyle kapsanıyor. Canlı demo, dört ajanı ve Arapça/İngilizce iki dilli olay günlükleri olan kurgusal bir klinik etrafında kurulu (giriş bilgileri deponun README dosyasında).

**Teknolojiler:** React 18 · Vite · Node.js / Express · Prisma · PostgreSQL · Docker

[Canlı demoyu aç](https://orcha-official.up.railway.app) · [Kodu oku](https://github.com/RanimAlyaseen/Orcha-App)

<img src="assets/tr/s2.svg" width="100%" alt="Sahne 2: test setinin yalan söylediği gün"/>

<img src="assets/tr/d-leak.svg" width="100%" alt="Şema: özgün eğitim ve test dosyaları 988 özeti paylaşıyordu. Ekip denetledi, bölümleri yeniden kurdu, modelleri doğrulamada seçti ve kilitli test setine bir kez baktı: 0,8603 makro F1."/>

İstinye Üniversitesi'ndeki beş kişilik bir NLP ders projesinde görev, tıbbi makale özetlerini beş hastalık kategorisine ayırmaktı. Herhangi bir eğitimden önce ekip veriyi denetledi ve bir sorun buldu: 14.438 satırın yalnızca 11.227'si benzersiz metindi, **988 özet hem eğitim hem test dosyasında yer alıyordu** ve 2.929 özet grubu çelişkili etiketler taşıyordu. Eğitim verisiyle örtüşen bir test seti hiçbir şeyi ölçmez.

Bu yüzden ekip veriyi temizledi, bölümleri yeniden kurdu, modelleri yalnızca doğrulama setinde seçti ve test setine tam bir kez baktı. Benim payım model eğitimi ve karşılaştırması, BiomedBERT ince ayarı, kıyaslama kurulumu, hata analizi ve nihai değerlendirmeydi. BiomedBERT, **doğrulamada 0,8672 ve kilitli testte 0,8603 makro F1** ile kazandı. Yalnızca 0,0069'luk fark, skorun sağlam olduğunu gösteriyor.

[Kaynak ve belgeler](https://github.com/RanimAlyaseen/team-ultron-medical-abstract-classification)

<img src="assets/tr/s3.svg" width="100%" alt="Sahne 3: kazanamayan model"/>

<img src="assets/tr/d-twist.svg" width="100%" alt="Şema: seçilen model ayrılmış veride 0,433 ROC-AUC aldı; bu, 0,5 yazı tura çizgisinin altında. Yine de yayınlandı."/>

Her deney kazanmaz. Tekrarlanabilir bir deney olarak yeniden kurduğum bir üniversite ML projesinde amaç, altı üstveri alanından bir kitabın puanının 4,6 veya üzeri olup olmadığını tahmin etmekti (348 kitap). Grup duyarlı bölümler kullandım, modelleri yalnızca eğitim verisiyle seçtim ve her şeyi çoğunluk sınıfı referansıyla karşılaştırdım.

Sonuç: seçilen Lojistik Regresyon, ayrılmış veride 0,457 doğruluk ve 0,433 ROC-AUC aldı; yani **referansa karşı güvenilir bir üstünlük yok**. Sınırlarını yazarak tam olarak böyle yayınladım, çünkü net bir olumsuz sonuç da bir sonuçtur. Streamlit demosu ve otomatik testler projeyle birlikte geliyor.

[Kaynak ve belgeler](https://github.com/RanimAlyaseen/book-rating-prediction)

<img src="assets/tr/s4.svg" width="100%" alt="Sahne 4: para eksiye düşemez"/>

<img src="assets/tr/d-vault.svg" width="100%" alt="Şema: bir rezervasyona fazla ödeme yapacak ödeme, veritabanı tetikleyicisi tarafından reddedilir."/>

Sayılara güvenilemiyorsa bir CRM işe yaramaz. Bir turizm CRM veritabanında (üniversite DBMS projesi; tekrarlanabilir bir MySQL deposu olarak yeniden kuruldu) kuralları veritabanının içine koydum: dokuz tablo, üç raporlama görünümü, iki fonksiyon ve altı tetikleyici.

Bir rezervasyona fazla ödeme yapacak bir ödemeyi **tetikleyici reddeder**. Bir yorum, rezervasyonun sahibi müşteriye ait olmak zorundadır; bu, bileşik yabancı anahtarla zorunlu kılınır. SQL test senaryoları ve kontrollü iki oturumlu eşzamanlılık testleri bunu kanıtlar. Yalnızca veritabanı katmanı; web arayüzü yok.

[Kaynak ve belgeler](https://github.com/RanimAlyaseen/tourism-crm-dbms)

<img src="assets/tr/s5.svg" width="100%" alt="Sahne 5: yan görevler"/>

<img src="assets/tr/d-side.svg" width="100%" alt="Üç yan proje: 26 rollü CASIE olay çıkarımı, ortak konuşmacısı olmayan İzlandaca konuşma verisi ve akciğer nodülü tespiti tasarım çalışması."/>

[CASIE](https://github.com/RanimAlyaseen/casie-event-argument-extraction) · [Icelandic ASR](https://github.com/RanimAlyaseen/icelandic-asr-project3) · [Akciğer nodülü çalışması](https://drive.google.com/drive/folders/1t_D6z8vG5mqFVUuV0Yiw7lJgMr2kazwr?usp=sharing)

<img src="assets/tr/s6.svg" width="100%" alt="Alet çantası"/>

<img src="assets/tr/toolbox.svg" width="100%" alt="Alet çantası. Programlama: JavaScript, Python, SQL. Web: React, Vite, Node.js, Express, Prisma, REST API. Veri: PostgreSQL, MySQL, SQLite. ML ve NLP: PyTorch, Transformers, scikit-learn, pandas. Teslimat: Docker, Nginx, Railway, Git, Playwright, pytest. Yaratıcı: grafik tasarım, video kurgu. Diller: İngilizce, Arapça, Türkçe."/>

<img src="assets/tr/s7.svg" width="100%" alt="Sonraki bölüm"/>

<img src="assets/tr/next.svg" width="100%" alt="Sonraki bölüm: konuşma, biyomedikal NLP ve bunları dürüstçe değerlendirmek."/>

<div align="center">
<a href="https://www.linkedin.com/in/ranim-alyaseen-846522373"><img src="assets/tr/btn-linkedin.svg" height="56" alt="LinkedIn"/></a>
<a href="https://github.com/RanimAlyaseen?tab=repositories"><img src="assets/tr/btn-github.svg" height="56" alt="GitHub"/></a>
<a href="https://drive.google.com/drive/folders/1t_D6z8vG5mqFVUuV0Yiw7lJgMr2kazwr?usp=sharing"><img src="assets/tr/btn-research.svg" height="56" alt="Araştırma"/></a>
</div>

<sub>Takım ve üniversite projeleri, depolarında bu şekilde belirtilmiştir. Katkı beyanları yayımlanmış atıf kayıtlarına dayanır.</sub>
