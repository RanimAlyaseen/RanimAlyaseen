import sys
OUT = sys.argv[1]
R = "https://github.com/RanimAlyaseen/"
DEMO = "https://orcha-official.up.railway.app"
LI = "https://www.linkedin.com/in/ranim-alyaseen-846522373"
GH = "https://github.com/RanimAlyaseen?tab=repositories"
RES = "https://drive.google.com/drive/folders/1t_D6z8vG5mqFVUuV0Yiw7lJgMr2kazwr?usp=sharing"

def switcher(active):
    out = '<div align="center">\n'
    for code, file, alt in [("en", "README.md", "English"), ("ar", "README.ar.md", "العربية"), ("tr", "README.tr.md", "Türkçe")]:
        img = f"assets/lang-{code}{'-on' if code == active else ''}.svg"
        out += f'<a href="{file}"><img src="{img}" height="40" alt="{alt}"/></a>\n'
    return out + '</div>\n'

def img(lang, name, alt, width="100%"):
    return f'<img src="assets/{lang}/{name}.svg" width="{width}" alt="{alt}"/>'

def build(lang, d):
    rtl = lang == "ar"
    def block(txt):
        return f'<div dir="rtl">\n\n{txt}\n\n</div>' if rtl else txt
    s = []
    s.append(switcher(lang))
    s.append(img(lang, "hero", d["hero_alt"]))
    s.append(block(d["logline"]))
    s.append(img(lang, "s0", d["s0_alt"]))
    s.append(block(d["cold"]))
    s.append(img(lang, "s1", d["s1_alt"]))
    s.append(img(lang, "d-orcha", d["orcha_alt"]))
    s.append(block(d["orcha"] + f'\n\n**{d["stack"]}:** React 18 · Vite · Node.js / Express · Prisma · PostgreSQL · Docker\n\n[{d["demo"]}]({DEMO}) · [{d["code"]}]({R}Orcha-App)'))
    s.append(img(lang, "s2", d["s2_alt"]))
    s.append(img(lang, "d-leak", d["leak_alt"]))
    s.append(block(d["leak"] + f'\n\n[{d["repo"]}]({R}team-ultron-medical-abstract-classification)'))
    s.append(img(lang, "s3", d["s3_alt"]))
    s.append(img(lang, "d-twist", d["twist_alt"]))
    s.append(block(d["twist"] + f'\n\n[{d["repo"]}]({R}book-rating-prediction)'))
    s.append(img(lang, "s4", d["s4_alt"]))
    s.append(img(lang, "d-vault", d["vault_alt"]))
    s.append(block(d["vault"] + f'\n\n[{d["repo"]}]({R}tourism-crm-dbms)'))
    s.append(img(lang, "s5", d["s5_alt"]))
    s.append(img(lang, "d-side", d["side_alt"]))
    s.append(block(f'[CASIE]({R}casie-event-argument-extraction) · [Icelandic ASR]({R}icelandic-asr-project3) · [{d["nodule"]}]({RES})'))
    s.append(img(lang, "s6", d["s6_alt"]))
    s.append(img(lang, "toolbox", d["toolbox_alt"]))
    s.append(img(lang, "s7", d["s7_alt"]))
    s.append(img(lang, "next", d["next_alt"]))
    btns = (f'<div align="center">\n<a href="{LI}"><img src="assets/{lang}/btn-linkedin.svg" height="56" alt="LinkedIn"/></a>\n'
            f'<a href="{R[:-1]}?tab=repositories"><img src="assets/{lang}/btn-github.svg" height="56" alt="GitHub"/></a>\n'
            f'<a href="{RES}"><img src="assets/{lang}/btn-research.svg" height="56" alt="{d["res"]}"/></a>\n</div>')
    s.append(btns)
    s.append(block(f'<sub>{d["foot"]}</sub>'))
    return "\n\n".join(s) + "\n"

EN = dict(
    hero_alt="Ranim: engineer by degree, editor and designer by habit. A short film about building things that hold up.",
    logline="> **Logline:** A final-year software engineer who ships full-stack products, runs ML experiments honestly, and designs and edits the visuals around them.",
    s0_alt="Cold open: who's behind the camera", s1_alt="Scene 1: Orcha, who watches the AI agents?", s2_alt="Scene 2: the day the test set lied",
    s3_alt="Scene 3: the model that didn't win", s4_alt="Scene 4: money can't go negative", s5_alt="Scene 5: side quests",
    s6_alt="Toolbox", s7_alt="Next episode",
    orcha_alt="Diagram: AI agents on WhatsApp, voice, web chat and email flow into Orcha, then through a human review queue (approve, edit, reject) before reaching the customer.",
    leak_alt="Diagram: the original train and test files shared 988 abstracts. The team audited, rebuilt the splits, chose models on validation, and looked at the locked test set once: 0.8603 macro F1.",
    twist_alt="Diagram: the selected model scored ROC-AUC 0.433 on held-out data, below the 0.5 coin-flip line. Published anyway.",
    vault_alt="Diagram: a payment that would overpay a booking is rejected by a database trigger.",
    side_alt="Three side projects: CASIE event extraction with 26 roles, Icelandic speech data with zero shared speakers, and a pulmonary nodule detection design study.",
    toolbox_alt="Toolbox. Programming: JavaScript, Python, SQL. Web: React, Vite, Node.js, Express, Prisma, REST APIs. Data: PostgreSQL, MySQL, SQLite. ML and NLP: PyTorch, Transformers, scikit-learn, pandas. Delivery: Docker, Nginx, Railway, Git, Playwright, pytest. Creative: graphic design, video editing. Spoken: English, Arabic, Turkish.",
    next_alt="Next episode: speech, biomedical NLP, and how to evaluate them honestly.", res="Research",
    cold="I'm Ranim, a final-year software engineering student at Istinye University in Istanbul. I work in English, Arabic and Turkish, and I split my time between three crafts: building software, editing video, and designing visuals. What they share is the part I care about most: making something clear, and making sure it holds up when someone pushes on it. This page is the director's cut.",
    orcha="Companies are putting AI agents on WhatsApp, phone lines, website chat and email. Then a practical question shows up: **who is watching them?** Orcha is my answer. It's one control plane for every agent a team runs, with tasks, customer records, event logs and analytics, plus a review queue where a human approves, edits or rejects flagged output *before* it reaches a customer.\n\nIt's multi-tenant, with role-based access, JWT authentication, email verification and rate limiting. It's deployed on Railway, runs in Docker behind Nginx, and is covered by 7 Playwright end-to-end specs. The live demo follows a fictional clinic with four agents and bilingual Arabic and English event logs (login details are in the repo README).",
    nodule="Pulmonary nodule study",
    stack="Stack", demo="Open the live demo", code="Read the code", repo="Source and docs",
    leak="In a five-person NLP course project at Istinye University, the task was to classify medical abstracts into five disease categories. Before any training, the team audited the data and found a problem: of 14,438 rows, only 11,227 were unique texts, **988 abstracts appeared in both the train and the test files**, and 2,929 groups of abstracts carried conflicting labels. A test set that overlaps the training set measures nothing.\n\nSo the team cleaned the data, rebuilt the splits, chose models on validation only, and looked at the test set exactly once. My part was model training and comparison, BiomedBERT fine-tuning, the benchmark, error analysis and the final evaluation. BiomedBERT won with **0.8672 macro F1 on validation and 0.8603 on the locked test set**. A gap of just 0.0069 suggests the score holds up.",
    twist="Not every experiment wins. In a university ML project that I rebuilt as a reproducible experiment, the goal was to predict from six metadata fields whether a book's rating is 4.6 or higher (348 books). I used group-aware splits, chose models using training data only, and compared everything against a majority-class baseline.\n\nThe result: the selected Logistic Regression scored 0.457 held-out accuracy and 0.433 ROC-AUC, which is **no reliable advantage over the baseline**. I published it exactly like that, with the limits written down, because a clear negative result is still a result. A Streamlit demo and automated tests ship with it.",
    vault="A CRM is only useful if its numbers can be trusted. For a tourism CRM database (a university DBMS project, rebuilt as a reproducible MySQL repository) I put the rules inside the database itself: nine tables, three reporting views, two functions and six triggers.\n\nA payment that would overpay a booking is **rejected by a trigger**. A review has to belong to the customer who owns the booking, enforced with a composite foreign key. SQL test cases and controlled two-session concurrency tests prove it. It's the database layer only, with no web UI.",
    foot="Team and university projects are identified as such in their repositories. Contribution claims follow the published attribution records.",
)

TR = dict(
    hero_alt="Ranim: diplomayla mühendis, alışkanlıkla editör ve tasarımcı. Sağlam şeyler inşa etmek üzerine kısa bir film.",
    logline="> **Özet:** Tam kapsamlı ürünler çıkaran, ML deneylerini dürüstçe yürüten ve çevresindeki görselleri tasarlayıp kurgulayan son sınıf yazılım mühendisliği öğrencisi.",
    s0_alt="Giriş: kameranın arkasındaki kişi", s1_alt="Sahne 1: Orcha, yapay zekâ ajanlarını kim izliyor?", s2_alt="Sahne 2: test setinin yalan söylediği gün",
    s3_alt="Sahne 3: kazanamayan model", s4_alt="Sahne 4: para eksiye düşemez", s5_alt="Sahne 5: yan görevler",
    s6_alt="Alet çantası", s7_alt="Sonraki bölüm",
    orcha_alt="Şema: WhatsApp, sesli arama, web sohbeti ve e-postadaki yapay zekâ ajanları Orcha'ya akar, ardından müşteriye ulaşmadan önce insan incelemesinden (onayla, düzenle, reddet) geçer.",
    leak_alt="Şema: özgün eğitim ve test dosyaları 988 özeti paylaşıyordu. Ekip denetledi, bölümleri yeniden kurdu, modelleri doğrulamada seçti ve kilitli test setine bir kez baktı: 0,8603 makro F1.",
    twist_alt="Şema: seçilen model ayrılmış veride 0,433 ROC-AUC aldı; bu, 0,5 yazı tura çizgisinin altında. Yine de yayınlandı.",
    vault_alt="Şema: bir rezervasyona fazla ödeme yapacak ödeme, veritabanı tetikleyicisi tarafından reddedilir.",
    side_alt="Üç yan proje: 26 rollü CASIE olay çıkarımı, ortak konuşmacısı olmayan İzlandaca konuşma verisi ve akciğer nodülü tespiti tasarım çalışması.",
    toolbox_alt="Alet çantası. Programlama: JavaScript, Python, SQL. Web: React, Vite, Node.js, Express, Prisma, REST API. Veri: PostgreSQL, MySQL, SQLite. ML ve NLP: PyTorch, Transformers, scikit-learn, pandas. Teslimat: Docker, Nginx, Railway, Git, Playwright, pytest. Yaratıcı: grafik tasarım, video kurgu. Diller: İngilizce, Arapça, Türkçe.",
    next_alt="Sonraki bölüm: konuşma, biyomedikal NLP ve bunları dürüstçe değerlendirmek.", res="Araştırma",
    cold="Ben Ranim, İstanbul'da İstinye Üniversitesi'nde yazılım mühendisliği son sınıf öğrencisiyim. İngilizce, Arapça ve Türkçe çalışıyorum ve zamanımı üç zanaat arasında bölüyorum: yazılım geliştirmek, video kurgulamak ve görsel tasarlamak. Üçünün ortak noktası benim için en önemli kısım: bir şeyi anlaşılır kılmak ve biri onu zorladığında ayakta kalmasını sağlamak. Bu sayfa, yönetmen kurgusu.",
    orcha="Şirketler yapay zekâ ajanlarını WhatsApp'a, telefon hatlarına, web sohbetine ve e-postaya yerleştiriyor. Sonra pratik bir soru çıkıyor: **Bu ajanları kim izliyor?** Orcha benim cevabım. Bir ekibin çalıştırdığı her ajan için tek kontrol paneli: görevler, müşteri kayıtları, olay günlükleri ve analitik; ayrıca işaretlenen çıktının müşteriye ulaşmadan *önce* bir insan tarafından onaylandığı, düzenlendiği ya da reddedildiği bir inceleme kuyruğu.\n\nÇok kiracılı (multi-tenant) yapıda; rol tabanlı erişim, JWT kimlik doğrulama, e-posta doğrulama ve hız sınırlama içeriyor. Railway üzerinde yayında, Nginx arkasında Docker ile çalışıyor ve 7 Playwright uçtan uca testiyle kapsanıyor. Canlı demo, dört ajanı ve Arapça/İngilizce iki dilli olay günlükleri olan kurgusal bir klinik etrafında kurulu (giriş bilgileri deponun README dosyasında).",
    stack="Teknolojiler", demo="Canlı demoyu aç", code="Kodu oku", repo="Kaynak ve belgeler",
    leak="İstinye Üniversitesi'ndeki beş kişilik bir NLP ders projesinde görev, tıbbi makale özetlerini beş hastalık kategorisine ayırmaktı. Herhangi bir eğitimden önce ekip veriyi denetledi ve bir sorun buldu: 14.438 satırın yalnızca 11.227'si benzersiz metindi, **988 özet hem eğitim hem test dosyasında yer alıyordu** ve 2.929 özet grubu çelişkili etiketler taşıyordu. Eğitim verisiyle örtüşen bir test seti hiçbir şeyi ölçmez.\n\nBu yüzden ekip veriyi temizledi, bölümleri yeniden kurdu, modelleri yalnızca doğrulama setinde seçti ve test setine tam bir kez baktı. Benim payım model eğitimi ve karşılaştırması, BiomedBERT ince ayarı, kıyaslama kurulumu, hata analizi ve nihai değerlendirmeydi. BiomedBERT, **doğrulamada 0,8672 ve kilitli testte 0,8603 makro F1** ile kazandı. Yalnızca 0,0069'luk fark, skorun sağlam olduğunu gösteriyor.",
    twist="Her deney kazanmaz. Tekrarlanabilir bir deney olarak yeniden kurduğum bir üniversite ML projesinde amaç, altı üstveri alanından bir kitabın puanının 4,6 veya üzeri olup olmadığını tahmin etmekti (348 kitap). Grup duyarlı bölümler kullandım, modelleri yalnızca eğitim verisiyle seçtim ve her şeyi çoğunluk sınıfı referansıyla karşılaştırdım.\n\nSonuç: seçilen Lojistik Regresyon, ayrılmış veride 0,457 doğruluk ve 0,433 ROC-AUC aldı; yani **referansa karşı güvenilir bir üstünlük yok**. Sınırlarını yazarak tam olarak böyle yayınladım, çünkü net bir olumsuz sonuç da bir sonuçtur. Streamlit demosu ve otomatik testler projeyle birlikte geliyor.",
    vault="Sayılara güvenilemiyorsa bir CRM işe yaramaz. Bir turizm CRM veritabanında (üniversite DBMS projesi; tekrarlanabilir bir MySQL deposu olarak yeniden kuruldu) kuralları veritabanının içine koydum: dokuz tablo, üç raporlama görünümü, iki fonksiyon ve altı tetikleyici.\n\nBir rezervasyona fazla ödeme yapacak bir ödemeyi **tetikleyici reddeder**. Bir yorum, rezervasyonun sahibi müşteriye ait olmak zorundadır; bu, bileşik yabancı anahtarla zorunlu kılınır. SQL test senaryoları ve kontrollü iki oturumlu eşzamanlılık testleri bunu kanıtlar. Yalnızca veritabanı katmanı; web arayüzü yok.",
    nodule="Akciğer nodülü çalışması",
    foot="Takım ve üniversite projeleri, depolarında bu şekilde belirtilmiştir. Katkı beyanları yayımlanmış atıf kayıtlarına dayanır.",
)

AR = dict(
    hero_alt="رنيم: هندسة برمجيات بالدراسة، ومونتاج وتصميم بالشغف. فيلم قصير عن بناء أشياء تصمد.",
    logline="> **الخلاصة:** في السنة الأخيرة من دراسة هندسة البرمجيات: أبني منتجات متكاملة، وأجري تجارب تعلّم آلي بأمانة علمية، وأصمم وأُمنتج المحتوى البصري المحيط بها.",
    s0_alt="المقدمة: من وراء الكاميرا", s1_alt="المشهد 1: Orcha، من يراقب وكلاء الذكاء الاصطناعي؟", s2_alt="المشهد 2: اليوم الذي كذبت فيه مجموعة الاختبار",
    s3_alt="المشهد 3: النموذج الذي لم يفز", s4_alt="المشهد 4: المال لا يمكن أن يصبح سالباً", s5_alt="المشهد 5: مهام جانبية",
    s6_alt="الأدوات", s7_alt="الحلقة القادمة",
    orcha_alt="مخطط: وكلاء الذكاء الاصطناعي على واتساب والمكالمات ودردشة الموقع والبريد يتدفقون إلى Orcha، ثم يمرّون بمراجعة بشرية (موافقة، تعديل، رفض) قبل أن يصلوا إلى العميل.",
    leak_alt="مخطط: ملفا التدريب والاختبار الأصليان تشاركا 988 ملخصاً. دقّق الفريق وأعاد بناء التقسيمات واختار النماذج بالتحقق ونظر إلى الاختبار المقفل مرة واحدة: ماكرو F1 بقيمة 0.8603.",
    twist_alt="مخطط: النموذج المختار حقق ROC-AUC بقيمة 0.433 على بيانات الاختبار، أي أقل من خط رمي العملة 0.5. نُشرت النتيجة رغم ذلك.",
    vault_alt="مخطط: الدفعة التي تتجاوز المبلغ المستحق للحجز يرفضها مُشغِّل في قاعدة البيانات.",
    side_alt="ثلاثة مشاريع جانبية: استخراج أحداث CASIE بـ26 دوراً، وبيانات كلام آيسلندية بلا متحدثين مشتركين، ودراسة تصميم لكشف عقيدات الرئة.",
    toolbox_alt="الأدوات. البرمجة: JavaScript وPython وSQL. الويب: React وVite وNode.js وExpress وPrisma وREST APIs. البيانات: PostgreSQL وMySQL وSQLite. ML وNLP: PyTorch وTransformers وscikit-learn وpandas. النشر: Docker وNginx وRailway وGit وPlaywright وpytest. الإبداع: التصميم الجرافيكي ومونتاج الفيديو. اللغات: الإنجليزية والعربية والتركية.",
    next_alt="الحلقة القادمة: الكلام، ومعالجة اللغة الطبية الحيوية، وتقييمها بأمانة.", res="الأبحاث",
    cold="أنا رنيم، في سنتي الأخيرة بدراسة هندسة البرمجيات في جامعة إستينيه في إسطنبول. أعمل بثلاث لغات: العربية والإنجليزية والتركية، وأقسّم وقتي بين ثلاث حِرَف: بناء البرمجيات، ومونتاج الفيديو، وتصميم الجرافيك. ما يجمع بينها هو ما يهمني أكثر: أن يكون الشيء واضحاً، وأن يصمد حين يُختبر. هذه الصفحة هي النسخة الإخراجية الكاملة.",
    orcha="تضع الشركات اليوم وكلاء ذكاء اصطناعي على واتساب والهاتف ودردشة المواقع والبريد. ثم يظهر سؤال عملي: **من يراقب هؤلاء الوكلاء؟** Orcha هو جوابي: لوحة تحكم واحدة لكل وكيل يشغّله الفريق، فيها المهام وسجلات العملاء وسجل الأحداث والتحليلات، مع طابور مراجعة يوافق فيه إنسان على المخرجات المعلَّمة أو يعدّلها أو يرفضها *قبل* أن تصل إلى العميل.\n\nالنظام متعدد المستأجرين مع صلاحيات حسب الدور ومصادقة JWT وتحقق بالبريد وتحديد لمعدل الطلبات. منشور على Railway، ويعمل ضمن Docker خلف Nginx، ومغطّى بسبعة اختبارات شاملة (End-to-End) بـ Playwright. العرض التجريبي يتبع عيادة افتراضية بأربعة وكلاء وسجلات أحداث ثنائية اللغة بالعربية والإنجليزية (بيانات الدخول في ملف README الخاص بالمستودع).",
    stack="التقنيات", demo="افتح العرض التجريبي", code="اقرأ الشيفرة", repo="المصدر والوثائق",
    leak="في مشروع جماعي لمادة معالجة اللغات الطبيعية (خمسة أعضاء في جامعة إستينيه)، كانت المهمة تصنيف ملخصات الأبحاث الطبية إلى خمس فئات مرضية. قبل أي تدريب دقّق الفريق في البيانات فوجد مشكلة: من بين 14,438 صفاً لم يكن هناك سوى 11,227 نصاً فريداً، و**ظهر 988 ملخصاً في ملفي التدريب والاختبار معاً**، وحملت 2,929 مجموعة من الملخصات تصنيفات متعارضة. مجموعة اختبار تتداخل مع التدريب لا تقيس شيئاً.\n\nلذلك نظّف الفريق البيانات وأعاد بناء التقسيمات، واختار النماذج بالتحقق فقط، ونظر إلى مجموعة الاختبار مرة واحدة. دوري كان تدريب النماذج ومقارنتها، وضبط BiomedBERT، وبناء المقياس، وتحليل الأخطاء، والتقييم النهائي. فاز BiomedBERT بـ**ماكرو F1 بلغ 0.8672 في التحقق و0.8603 في الاختبار المقفل**. فجوة 0.0069 فقط تشير إلى أن النتيجة متينة.",
    twist="ليست كل التجارب رابحة. في مشروع تعلّم آلي جامعي أعدت بناءه كتجربة قابلة للتكرار، كان الهدف التنبؤ، من ستة حقول وصفية، بما إذا كان تقييم الكتاب 4.6 أو أكثر (348 كتاباً). استخدمت تقسيمات واعية بالمجموعات، واخترت النماذج باستخدام بيانات التدريب فقط، وقارنت كل شيء بخط أساس يتنبأ بالفئة الأكثر شيوعاً.\n\nالنتيجة: حقق نموذج الانحدار اللوجستي المختار دقة 0.457 على بيانات الاختبار وROC-AUC بقيمة 0.433، أي **بلا أفضلية موثوقة على الخط الأساسي**. نشرت النتيجة كما هي مع توثيق الحدود، لأن النتيجة السلبية الواضحة تظل نتيجة. المشروع يتضمن عرضاً بـ Streamlit واختبارات آلية.",
    vault="لا فائدة من نظام CRM إن لم يكن بالإمكان الوثوق بأرقامه. في قاعدة بيانات CRM سياحية (مشروع جامعي لمادة قواعد البيانات، أعيد بناؤه كمستودع MySQL قابل للتكرار) وضعت القواعد داخل قاعدة البيانات نفسها: تسعة جداول وثلاث واجهات عرض للتقارير ودالتان وستة مُشغِّلات.\n\nأي دفعة تتجاوز المبلغ المستحق للحجز **يرفضها مُشغِّل**. وكل تقييم يجب أن يخص العميل صاحب الحجز، ويُفرض ذلك بمفتاح أجنبي مركّب. وتثبت ذلك اختبارات SQL واختبارات تزامن مضبوطة بجلستين. المشروع طبقة قاعدة البيانات فقط، بلا واجهة ويب.",
    nodule="دراسة عقيدات الرئة",
    foot="المشاريع الجماعية والجامعية موضّحة كذلك في مستودعاتها، وتستند ادعاءات المساهمة إلى سجلات الإسناد المنشورة.",
)
open(f"{OUT}/README.md", "w").write(build("en", EN))
open(f"{OUT}/README.tr.md", "w").write(build("tr", TR))
open(f"{OUT}/README.ar.md", "w").write(build("ar", AR))
print("readmes ok")
