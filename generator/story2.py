"""Storytelling profile assets in English, Turkish and Arabic. Facts come from the repos' READMEs or the user."""
import sys, os, re
from xml.sax.saxutils import escape as esc

ROOT = sys.argv[1]
SANS = "Inter, 'Segoe UI', Tahoma, -apple-system, 'Helvetica Neue', Helvetica, Arial, 'Noto Sans Arabic', 'DejaVu Sans', sans-serif"
MONO = "ui-monospace, SFMono-Regular, Menlo, Consolas, 'Liberation Mono', monospace"
BG, PANEL, LINE, TEXT, MUTED = "#0f1014", "#1a1c23", "#2c2f3a", "#eceef4", "#8d93a6"
AMBER, TEAL, VIOLET, ROSE, BLUE, GREEN, RED = "#ffb23e", "#3ddbc5", "#9a87ff", "#ff6b8b", "#5eb0ff", "#7be28c", "#ff5d5d"
ARABIC = re.compile(r"[؀-ۿ]")

# ---------------------------------------------------------------- translations
S = {
"en": dict(
    name="Ranim", kicker="A SHORT FILM ABOUT BUILDING THINGS THAT HOLD UP",
    tagline="Engineer by degree. Editor and designer by habit.",
    roles="Software engineer  ·  Video editor  ·  Graphic designer",
    final="final-year software engineering student", cap_r="color + cut",
    chapters=["COLD OPEN", "ORCHA", "THE LEAK", "THE TWIST", "THE VAULT", "SIDE QUESTS", "TOOLBOX"],
    slates=[("COLD OPEN", "Who's behind the camera", "INTRO"), ("SCENE 1", "Orcha: who watches the AI agents?", "PRODUCT"),
            ("SCENE 2", "The day the test set lied", "DETECTIVE STORY"), ("SCENE 3", "The model that didn't win", "PLOT TWIST"),
            ("SCENE 4", "Money can't go negative", "SAFETY NET"), ("SCENE 5", "Side quests", "BONUS FEATURES"),
            ("TOOLBOX", "What's in the kit bag", "CREDITS"), ("NEXT EPISODE", "Coming up", "TRAILER")],
    orcha=dict(head="AI AGENTS, EVERY CHANNEL", agents=["WhatsApp", "Voice calls", "Website chat", "Email"], plane="one control plane",
               chips=["Tasks", "Customers", "Event log", "Analytics", "Roles"], review="HUMAN REVIEW", flagged="Flagged output waits here",
               acts=["Approve", "Edit", "Reject"], customer="Customer"),
    leak=dict(train="TRAIN", rows1="11,550 rows", test="TEST", rows2="2,888 rows", same="same abstracts", illus="circle sizes illustrative",
              steps=[("Audit", "Found the overlap and\n2,929 label conflicts"), ("Rebuild", "Clean, deterministic\ntrain / val / test splits"),
                     ("Choose on validation", "Models compared without\ntouching the test set"), ("Look once", "BiomedBERT on the locked\ntest set: 0.8603 macro F1")]),
    twist=dict(hope="THE HOPE", l1="A trained model", l2="beats the dumb baseline.", sub="Predict if a book rates 4.6+ from 6 fields.",
               said="WHAT THE HELD-OUT DATA SAID", coin="0.5 = coin flip", auc="ROC-AUC 0.433",
               acc="Held-out accuracy 0.457. No reliable edge over the baseline.", pub="PUBLISHED ANYWAY"),
    vault=dict(head="BOOKING BALANCE", paid="paid", rem="remaining", inc="INCOMING PAYMENT", pay="+ payment", total="total", rej="REJECTED",
               by="by a database trigger:", would="payment would overpay",
               foot="Reviews are tied to the customer who owns the booking, enforced by a composite foreign key."),
    side=[("26", "event roles", "CASIE event extraction", ["Cybersecurity news: find who attacked", "whom. RoBERTa selected, 0.6196 Arg-C F1.", "Team NLP project. My part: modeling + eval."]),
          ("0", "shared speakers", "Icelandic speech data", ["20h Samromur subset for Whisper and", "wav2vec 2.0. 10,488 / 1,314 / 1,884", "utterances across train / dev / test."]),
          ("R&D", "design only", "Pulmonary nodule study", ["AI-assisted chest CT detection: pipeline,", "evaluation and safety design.", "No trained model or clinical claims."])],
    rows=["Programming", "Web", "Data", "ML + NLP", "Delivery", "Creative", "Spoken"],
    creative=["Graphic design", "Video editing"], spoken=["English", "Arabic", "Turkish"],
    nxt=dict(k="NEXT EPISODE", h="Speech, biomedical NLP, and how to evaluate them honestly.",
             s="Applied NLP  ·  biomedical language models  ·  speech processing  ·  evaluation design"),
    btn=["LinkedIn", "GitHub", "Research"],
),
"tr": dict(
    name="Ranim", kicker="SAĞLAM ŞEYLER İNŞA ETMEK ÜZERİNE KISA BİR FİLM",
    tagline="Diplomayla mühendis. Alışkanlıkla editör ve tasarımcı.",
    roles="Yazılım mühendisi  ·  Video editörü  ·  Grafik tasarımcı",
    final="yazılım mühendisliği son sınıf öğrencisi", cap_r="renk + kurgu",
    chapters=["GİRİŞ", "ORCHA", "SIZINTI", "SÜRPRİZ", "KASA", "YAN GÖREVLER", "ALET ÇANTASI"],
    slates=[("GİRİŞ", "Kameranın arkasındaki kişi", "TANITIM"), ("SAHNE 1", "Orcha: Yapay zekâ ajanlarını kim izliyor?", "ÜRÜN"),
            ("SAHNE 2", "Test setinin yalan söylediği gün", "DEDEKTİF HİKÂYESİ"), ("SAHNE 3", "Kazanamayan model", "SÜRPRİZ SON"),
            ("SAHNE 4", "Para eksiye düşemez", "GÜVENLİK AĞI"), ("SAHNE 5", "Yan görevler", "EKSTRA İÇERİK"),
            ("ALET ÇANTASI", "Çantada neler var", "JENERİK"), ("SONRAKİ BÖLÜM", "Çok yakında", "FRAGMAN")],
    orcha=dict(head="HER KANALDA YAPAY ZEKÂ AJANLARI", agents=["WhatsApp", "Sesli arama", "Web sohbeti", "E-posta"], plane="tek kontrol paneli",
               chips=["Görevler", "Müşteriler", "Olay günlüğü", "Analitik", "Roller"], review="İNSAN İNCELEMESİ", flagged="İşaretlenen çıktı burada bekler",
               acts=["Onayla", "Düzenle", "Reddet"], customer="Müşteri"),
    leak=dict(train="EĞİTİM", rows1="11.550 satır", test="TEST", rows2="2.888 satır", same="aynı özetler", illus="daire boyutları temsilidir",
              steps=[("Denetim", "Çakışma ve 2.929 etiket\nçelişkisi bulundu"), ("Yeniden kur", "Temiz, deterministik\neğitim / doğrulama / test"),
                     ("Doğrulamayla seç", "Test setine dokunmadan\nmodeller karşılaştırıldı"), ("Bir kez bak", "Kilitli test setinde\nBiomedBERT: 0,8603 makro F1")]),
    twist=dict(hope="BEKLENTİ", l1="Eğitilmiş bir model", l2="basit referansı geçer.", sub="Bir kitabın puanı 4,6+ mı? 6 alandan tahmin.",
               said="AYRILMIŞ VERİ NE DEDİ", coin="0,5 = yazı tura", auc="ROC-AUC 0,433",
               acc="Test doğruluğu 0,457. Referansa karşı güvenilir üstünlük yok.", pub="YİNE DE YAYINLANDI"),
    vault=dict(head="REZERVASYON BAKİYESİ", paid="ödenen", rem="kalan", inc="GELEN ÖDEME", pay="+ ödeme", total="toplam", rej="REDDEDİLDİ",
               by="veritabanı tetikleyicisi tarafından:", would="ödeme fazla ödemeye yol açardı",
               foot="Yorumlar, rezervasyonun sahibi müşteriye bağlıdır; bileşik yabancı anahtarla zorunlu kılınır."),
    side=[("26", "olay rolü", "CASIE olay çıkarımı", ["Siber güvenlik haberleri: kim kime", "saldırdı? RoBERTa seçildi, 0,6196 Arg-C F1.", "Takım NLP projesi: modelleme + değerlendirme."]),
          ("0", "ortak konuşmacı", "İzlandaca konuşma verisi", ["Whisper ve wav2vec 2.0 için 20 saatlik", "Samromur alt kümesi. 10.488 / 1.314 / 1.884", "ifade: eğitim / geliştirme / test."]),
          ("AR-GE", "yalnızca tasarım", "Akciğer nodülü çalışması", ["Yapay zekâ destekli BT tespiti: boru hattı,", "değerlendirme ve güvenlik tasarımı.", "Eğitilmiş model veya klinik iddia yok."])],
    rows=["Programlama", "Web", "Veri", "ML + NLP", "Teslimat", "Yaratıcı", "Diller"],
    creative=["Grafik tasarım", "Video kurgu"], spoken=["İngilizce", "Arapça", "Türkçe"],
    nxt=dict(k="SONRAKİ BÖLÜM", h="Konuşma, biyomedikal NLP ve bunları dürüstçe değerlendirmek.",
             s="Uygulamalı NLP  ·  biyomedikal dil modelleri  ·  konuşma işleme  ·  değerlendirme tasarımı"),
    btn=["LinkedIn", "GitHub", "Araştırma"],
),
"ar": dict(
    name="رنيم", kicker="فيلم قصير عن بناء أشياء تصمد",
    tagline="هندسة برمجيات بالدراسة، ومونتاج وتصميم بالشغف",
    roles="هندسة البرمجيات  ·  مونتاج الفيديو  ·  التصميم الجرافيكي",
    final="السنة الأخيرة في هندسة البرمجيات", cap_r="ألوان + مونتاج",
    chapters=["المقدمة", "ORCHA", "التسريب", "المفاجأة", "الخزنة", "مهام جانبية", "الأدوات"],
    slates=[("المقدمة", "من وراء الكاميرا", "تعريف"), ("المشهد 1", "Orcha: من يراقب وكلاء الذكاء الاصطناعي؟", "منتج"),
            ("المشهد 2", "اليوم الذي كذبت فيه مجموعة الاختبار", "قصة تحقيق"), ("المشهد 3", "النموذج الذي لم يفز", "مفاجأة"),
            ("المشهد 4", "المال لا يمكن أن يصبح سالباً", "شبكة أمان"), ("المشهد 5", "مهام جانبية", "مشاهد إضافية"),
            ("الأدوات", "ماذا في حقيبة العمل", "الشارات"), ("الحلقة القادمة", "قريباً", "إعلان")],
    orcha=dict(head="وكلاء الذكاء الاصطناعي في كل قناة", agents=["واتساب", "مكالمات صوتية", "دردشة الموقع", "البريد"], plane="لوحة تحكم واحدة",
               chips=["المهام", "العملاء", "سجل الأحداث", "التحليلات", "الأدوار"], review="مراجعة بشرية", flagged="المخرجات المعلَّمة تنتظر هنا",
               acts=["موافقة", "تعديل", "رفض"], customer="العميل"),
    leak=dict(train="التدريب", rows1="11,550 صفاً", test="الاختبار", rows2="2,888 صفاً", same="ملخصات متطابقة", illus="أحجام الدوائر توضيحية",
              steps=[("التدقيق", "اكتشاف التداخل و2,929\nتعارضاً في التصنيفات"), ("إعادة البناء", "تقسيم نظيف وثابت\nتدريب / تحقق / اختبار"),
                     ("الاختيار بالتحقق", "مقارنة النماذج دون\nلمس مجموعة الاختبار"), ("نظرة واحدة", "BiomedBERT على الاختبار\nالمقفل: 0.8603 ماكرو F1")]),
    twist=dict(hope="التوقع", l1="نموذج مُدرَّب", l2="يتفوق على الخط الأساسي.", sub="هل تقييم الكتاب 4.6 فأكثر؟ من 6 حقول.",
               said="ماذا قالت بيانات الاختبار", coin="0.5 = رمي عملة", auc="ROC-AUC 0.433",
               acc="الدقة 0.457. لا أفضلية موثوقة على الخط الأساسي.", pub="نُشرت رغم ذلك"),
    vault=dict(head="رصيد الحجز", paid="مدفوع", rem="المتبقي", inc="دفعة واردة", pay="+ دفعة", total="الإجمالي", rej="مرفوضة",
               by="بواسطة مُشغِّل في قاعدة البيانات:", would="الدفعة ستتجاوز المبلغ المستحق",
               foot="كل تقييم مرتبط بالعميل صاحب الحجز، ويُفرض ذلك بمفتاح أجنبي مركّب."),
    side=[("26", "دوراً للأحداث", "استخراج أحداث CASIE", ["أخبار الأمن السيبراني: من هاجم", "من؟ اختير RoBERTa، 0.6196 Arg-C F1.", "مشروع فريق. دوري: النمذجة والتقييم."]),
          ("0", "متحدثون مشتركون", "بيانات الكلام الآيسلندية", ["مجموعة Samromur بـ20 ساعة لنموذجي", "Whisper وwav2vec 2.0. 10,488 / 1,314 / 1,884", "مقطعاً: تدريب / تطوير / اختبار."]),
          ("R&D", "تصميم فقط", "دراسة عقيدات الرئة", ["كشف مدعوم بالذكاء الاصطناعي في CT:", "تصميم المسار والتقييم والسلامة.", "بلا نموذج مدرَّب أو ادعاءات سريرية."])],
    rows=["البرمجة", "الويب", "البيانات", "ML + NLP", "النشر", "الإبداع", "اللغات"],
    creative=["التصميم الجرافيكي", "مونتاج الفيديو"], spoken=["الإنجليزية", "العربية", "التركية"],
    nxt=dict(k="الحلقة القادمة", h="الكلام، ومعالجة اللغة الطبية الحيوية، وتقييمها بأمانة.",
             s="معالجة لغات تطبيقية  ·  نماذج لغوية طبية حيوية  ·  معالجة الكلام  ·  تصميم التقييم"),
    btn=["LinkedIn", "GitHub", "الأبحاث"],
),
}

# ---------------------------------------------------------------- helpers (language aware)
LANG = "en"
def t(x, y, s, size=20, weight=500, fill=TEXT, anchor="start", font=SANS, extra=""):
    if ARABIC.search(s):
        extra = re.sub(r'letter-spacing="[^"]*"', "", extra)
        if font == MONO:
            font = SANS
    return f'<text x="{x}" y="{y}" font-family="{font}" font-size="{size}" font-weight="{weight}" fill="{fill}" text-anchor="{anchor}" {extra}>{esc(s)}</text>'

def r(x, y, w, h, fill="none", stroke=None, rx=0, sw=1.5, extra=""):
    st = f' stroke="{stroke}" stroke-width="{sw}"' if stroke else ""
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}"{st} {extra}/>'

def chip(x, y, label, col, size=15, pad=14, filled=False):
    k = 0.66 if ARABIC.search(label) else 0.62
    w = int(len(label) * size * k + pad * 2)
    h = size + 16
    if filled:
        return r(x, y, w, h, col, rx=h / 2) + t(x + w / 2, y + h / 2 + size * 0.35, label, size, 700, BG, "middle"), w
    return r(x, y, w, h, col + "22", col, rx=h / 2, sw=1.2) + t(x + w / 2, y + h / 2 + size * 0.35, label, size, 600, col, "middle"), w

def svg(name, w, h, body, css=""):
    base = ("@keyframes blink{50%{opacity:0}}.blink{animation:blink 1.2s steps(1) infinite}"
            "@keyframes flow{to{stroke-dashoffset:-24}}.flow{stroke-dasharray:6 6;animation:flow 1.2s linear infinite}")
    d = os.path.join(ROOT, LANG)
    os.makedirs(d, exist_ok=True)
    open(f"{d}/{name}.svg", "w").write(
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}"><style>{base}{css}</style>{body}</svg>')

def arrow(x1, y, x2, col, animated=True):
    cls = ' class="flow"' if animated else ""
    return (f'<line x1="{x1}" y1="{y}" x2="{x2 - 8}" y2="{y}" stroke="{col}" stroke-width="2.5"{cls}/>'
            f'<path d="M{x2 - 10} {y - 7} L{x2} {y} L{x2 - 10} {y + 7}" fill="none" stroke="{col}" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>')

def fit(text, size, maxw, minsize=20):
    k = 0.60 if ARABIC.search(text) else 0.56
    while size > minsize and len(text) * size * k > maxw:
        size -= 1
    return size

# ---------------------------------------------------------------- builders
def hero(L):
    W, H = 1200, 480
    o = [r(0, 0, W, H, BG)]
    o.append('<defs><radialGradient id="g1" cx="78%" cy="40%" r="55%"><stop offset="0" stop-color="#ffb23e" stop-opacity=".22"/><stop offset="1" stop-color="#ffb23e" stop-opacity="0"/></radialGradient>'
             '<radialGradient id="g2" cx="10%" cy="100%" r="50%"><stop offset="0" stop-color="#9a87ff" stop-opacity=".14"/><stop offset="1" stop-color="#9a87ff" stop-opacity="0"/></radialGradient></defs>')
    o.append(r(0, 0, W, H, "url(#g1)") + r(0, 0, W, H, "url(#g2)"))
    o.append(r(0, 0, W, 40, "#000") + r(0, H - 40, W, 40, "#000"))
    o.append('<circle cx="34" cy="20" r="6" fill="#ff5d5d" class="blink"/>')
    o.append(t(50, 25, "REC", 13, 700, TEXT, font=MONO) + t(96, 25, "CAM A  ·  ISTANBUL", 13, 500, MUTED, font=MONO))
    o.append(t(W - 34, 25, "TC 00:00:00:00", 13, 500, MUTED, "end", MONO))
    o.append(t(64, 100, L["kicker"], fit(L["kicker"], 14, 640, 12), 600, AMBER, font=MONO, extra='letter-spacing="2.5"'))
    o.append(t(58, 230, L["name"], 150, 800, TEXT, extra='letter-spacing="-5"'))
    o.append(t(64, 282, L["tagline"], fit(L["tagline"], 30, 700, 22), 500, TEXT))
    o.append(t(64, 322, L["roles"], fit(L["roles"], 19, 700, 15), 500, MUTED))
    x = 64
    for lab, col in [("EN", TEAL), ("AR", AMBER), ("TR", ROSE)]:
        c, w = chip(x, 346, lab, col, 15, 16)
        o.append(c); x += w + 10
    o.append(t(x + 6, 368, L["final"], 15, 500, MUTED))
    fx, fy, fw, fh = 790, 96, 340, 210
    o.append(r(fx - 6, fy - 6, fw + 12, fh + 12, "#000", LINE, rx=10))
    o.append(f'<clipPath id="fr"><rect x="{fx}" y="{fy}" width="{fw}" height="{fh}" rx="5"/></clipPath>')
    o.append('<g clip-path="url(#fr)">' + r(fx, fy, fw, fh, "#141622"))
    for i, (w2, col) in enumerate([(120, TEAL), (80, MUTED), (150, VIOLET), (60, MUTED), (110, TEAL), (90, AMBER), (130, MUTED), (70, VIOLET), (100, TEAL)]):
        o.append(r(fx + 18 + (i % 3) * 14, fy + 20 + i * 20, w2, 7, col, rx=3.5, extra='opacity=".85"'))
    o.append(f'<polygon points="{fx + 170},{fy} {fx + fw},{fy} {fx + fw},{fy + fh} {fx + 80},{fy + fh}" fill="#1b1424"/>')
    o.append('<defs><linearGradient id="gr" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#ffb23e"/><stop offset=".55" stop-color="#ff6b8b"/><stop offset="1" stop-color="#6a4cff"/></linearGradient></defs>')
    o.append(f'<polygon points="{fx + 200},{fy + 20} {fx + fw - 16},{fy + 20} {fx + fw - 16},{fy + 120} {fx + 150},{fy + 120}" fill="url(#gr)" opacity=".9"/>')
    for i in range(18):
        hh = 14 + (i * 37 % 40)
        o.append(f'<rect x="{fx + 170 + i * 8}" y="{fy + 190 - hh}" width="4" height="{hh}" rx="2" fill="{AMBER}" style="transform-box:fill-box;transform-origin:bottom;animation:wv {0.9 + (i % 5) * .18:.2f}s ease-in-out infinite alternate"/>')
    o.append(f'<line x1="{fx + 170}" y1="{fy}" x2="{fx + 80}" y2="{fy + fh}" stroke="#ffffff" stroke-opacity=".35" stroke-width="1.5"/></g>')
    o.append(t(fx, fy + fh + 30, "{ code }", 14, 600, TEAL, font=MONO) + t(fx + fw, fy + fh + 30, L["cap_r"], 14, 600, AMBER, "end", MONO))
    ry = 410
    o.append(r(64, ry, 1072, 2, LINE))
    for i in range(0, 54):
        x2 = 64 + i * 20
        o.append(f'<line x1="{x2}" y1="{ry}" x2="{x2}" y2="{ry + (10 if i % 5 == 0 else 5)}" stroke="{LINE}" stroke-width="1.5"/>')
    for i, c in enumerate(L["chapters"]):
        cx = 64 + 20 + i * 168
        o.append(f'<path d="M{cx} {ry - 12} l7 7 l-7 7 l-7 -7z" fill="{AMBER}"/>')
        o.append(t(cx + 14, ry - 3, c, 12, 600, MUTED, font=MONO, extra='letter-spacing="1"'))
    o.append(f'<g><animateTransform attributeName="transform" type="translate" from="0 0" to="1072 0" dur="16s" repeatCount="indefinite"/>'
             f'<line x1="64" y1="{ry - 22}" x2="64" y2="{ry + 18}" stroke="{ROSE}" stroke-width="2"/><path d="M58 {ry - 24} h12 l-6 9z" fill="{ROSE}"/></g>')
    svg("hero", W, H, "".join(o), "@keyframes wv{from{transform:scaleY(.45)}to{transform:scaleY(1)}}")

def slate(name, scene, title, genre, col):
    W, H = 1200, 128
    o = [r(0, 0, W, H, PANEL), r(0, H - 3, W, 3, col)]
    o.append(r(36, 52, 92, 56, "#000", LINE, rx=6))
    stripes = "".join(f'<polygon points="{36 + i * 23},34 {36 + i * 23 + 14},34 {36 + i * 23 + 6},52 {36 + i * 23 - 8},52" fill="{TEXT if i % 2 == 0 else "#000"}"/>' for i in range(5))
    o.append(f'<g style="transform-origin:36px 52px;animation:clap 6s ease-in-out infinite">{stripes}</g>')
    o.append(r(36, 52, 92, 10, TEXT))
    chipw = int(len(genre) * 15 * (0.66 if ARABIC.search(genre) else 0.62) + 28)
    o.append(t(150, 44, scene, 14, 700, col, font=MONO, extra='letter-spacing="3"'))
    size = fit(title, 42, W - 150 - chipw - 70, 24)
    o.append(t(148, 92, title, size, 800, TEXT, extra='letter-spacing="-1"'))
    c, w = chip(W - 40 - chipw, 46, genre, col, 15, 14)
    o.append(c)
    svg(name, W, H, "".join(o), "@keyframes clap{0%,88%{transform:rotate(0)}93%{transform:rotate(-18deg)}100%{transform:rotate(0)}}")

def d_orcha(L):
    D = L["orcha"]
    W, H = 1200, 300
    o = [r(0, 0, W, H, BG)]
    cols = [TEAL, BLUE, VIOLET, AMBER]
    o.append(t(40, 36, D["head"], 13, 700, MUTED, font=MONO, extra='letter-spacing="2"'))
    for i, (a, c) in enumerate(zip(D["agents"], cols)):
        y = 56 + i * 54
        o.append(r(40, y, 200, 42, PANEL, LINE, rx=10) + f'<circle cx="64" cy="{y + 21}" r="7" fill="{c}"/>' + t(84, y + 27, a, 18, 600))
        o.append(f'<path d="M240 {y + 21} C 290 {y + 21}, 290 150, 330 150" fill="none" stroke="{c}" stroke-width="2" class="flow" opacity=".9"/>')
    o.append(r(330, 40, 330, 220, PANEL, TEAL, rx=16, sw=2))
    o.append(t(495, 84, "ORCHA", 34, 800, TEAL, "middle", extra='letter-spacing="2"'))
    o.append(t(495, 112, D["plane"], 16, 500, MUTED, "middle"))
    x, y = 352, 134
    for lab in D["chips"]:
        c, w = chip(x, y, lab, MUTED, 14, 12)
        if x + w > 640:
            x, y = 352, y + 40
            c, w = chip(x, y, lab, MUTED, 14, 12)
        o.append(c); x += w + 8
    o.append(arrow(660, 150, 740, TEAL))
    o.append(r(740, 70, 250, 160, PANEL, AMBER, rx=16, sw=2))
    o.append(t(865, 108, D["review"], 15, 700, AMBER, "middle", MONO, 'letter-spacing="2"'))
    o.append(t(865, 136, D["flagged"], fit(D["flagged"], 15, 224, 11), 500, MUTED, "middle"))
    bx = 754
    for lab, col in zip(D["acts"], [GREEN, AMBER, RED]):
        c, w = chip(bx, 168, lab, col, 14, 10)
        o.append(c); bx += w + 6
    o.append(arrow(990, 150, 1060, AMBER))
    o.append(f'<circle cx="1110" cy="150" r="42" fill="{PANEL}" stroke="{LINE}" stroke-width="2"/>')
    o.append(t(1110, 156, D["customer"], fit(D["customer"], 15, 78, 11), 700, TEXT, "middle"))
    svg("d-orcha", W, H, "".join(o))

def d_leak(L):
    D = L["leak"]
    W, H = 1200, 330
    o = [r(0, 0, W, H, BG)]
    o.append(f'<circle cx="170" cy="170" r="105" fill="{BLUE}" fill-opacity=".22" stroke="{BLUE}" stroke-width="2"/>')
    o.append(f'<circle cx="300" cy="170" r="85" fill="{ROSE}" fill-opacity=".22" stroke="{ROSE}" stroke-width="2"/>')
    o.append(t(112, 160, D["train"], 18, 800, BLUE, "middle") + t(112, 184, D["rows1"], 14, 500, MUTED, "middle"))
    o.append(t(342, 160, D["test"], 18, 800, ROSE, "middle") + t(342, 184, D["rows2"], 14, 500, MUTED, "middle"))
    o.append(t(235, 158, "988", 34, 800, TEXT, "middle") + t(235, 182, D["same"], 13, 600, AMBER, "middle"))
    o.append(t(235, 300, D["illus"], 11, 500, MUTED, "middle"))
    o.append(arrow(430, 170, 520, AMBER))
    for i, ((ttl, sub), col) in enumerate(zip(D["steps"], [AMBER, BLUE, VIOLET, GREEN])):
        x = 530 + i * 162
        o.append(r(x, 100, 150, 140, PANEL, col, rx=14, sw=1.8))
        o.append(f'<circle cx="{x + 24}" cy="126" r="14" fill="{col}"/>' + t(x + 24, 132, str(i + 1), 16, 800, BG, "middle"))
        o.append(t(x + 14, 166, ttl, fit(ttl, 15, 124, 11), 700, TEXT))
        sz = min(fit(ln, 12, 124, 9) for ln in sub.split("\n"))
        for j, ln in enumerate(sub.split("\n")):
            o.append(t(x + 14, 190 + j * 18, ln, sz, 500, MUTED))
    svg("d-leak", W, H, "".join(o))

def d_twist(L):
    D = L["twist"]
    W, H = 1200, 250
    o = [r(0, 0, W, H, BG)]
    o.append(r(40, 30, 440, 190, PANEL, LINE, rx=16))
    o.append(t(64, 66, D["hope"], 13, 700, TEAL, font=MONO, extra='letter-spacing="2"'))
    o.append(t(64, 112, D["l1"], fit(D["l1"], 28, 390, 20), 800) + t(64, 148, D["l2"], fit(D["l2"], 28, 390, 20), 800))
    o.append(t(64, 192, D["sub"], fit(D["sub"], 15, 390, 12), 500, MUTED))
    o.append(r(520, 30, 640, 190, PANEL, ROSE, rx=16, sw=2))
    o.append(t(544, 66, D["said"], 13, 700, ROSE, font=MONO, extra='letter-spacing="2"'))
    gx, gw = 544, 560
    o.append(r(gx, 108, gw, 14, "#0b0c10", LINE, rx=7))
    o.append(f'<rect x="{gx}" y="108" width="{gw * 0.433:.1f}" height="14" rx="7" fill="{ROSE}"/>')
    o.append(f'<line x1="{gx + gw * .5}" y1="96" x2="{gx + gw * .5}" y2="134" stroke="{TEXT}" stroke-width="2"/>')
    o.append(t(gx + gw * .5, 88, D["coin"], 12, 600, MUTED, "middle"))
    o.append(t(gx + gw * .433, 156, D["auc"], 16, 800, ROSE, "middle"))
    o.append(t(544, 196, D["acc"], fit(D["acc"], 16, 600, 12), 600, TEXT))
    o.append(t(1136, 66, D["pub"], 12, 700, AMBER, "end", MONO, 'letter-spacing="2"'))
    svg("d-twist", W, H, "".join(o))

def d_vault(L):
    D = L["vault"]
    W, H = 1200, 260
    o = [r(0, 0, W, H, BG)]
    o.append(t(40, 38, D["head"], 13, 700, MUTED, font=MONO, extra='letter-spacing="2"'))
    bx, bw = 40, 700
    o.append(r(bx, 56, bw, 46, "#0b0c10", AMBER, rx=10, sw=2))
    o.append(r(bx + 3, 59, bw * .72, 40, AMBER, rx=8, extra='opacity=".9"'))
    o.append(t(bx + 18, 87, D["paid"], 18, 800, BG) + t(bx + bw - 14, 87, D["rem"], 16, 600, AMBER, "end"))
    o.append(t(40, 140, D["inc"], 13, 700, MUTED, font=MONO, extra='letter-spacing="2"'))
    o.append(r(bx + bw * .72, 156, bw * .48, 40, ROSE + "33", ROSE, rx=10, sw=2))
    o.append(t(bx + bw * .72 + 16, 182, D["pay"], 16, 700, ROSE))
    o.append(f'<line x1="{bx + bw}" y1="50" x2="{bx + bw}" y2="210" stroke="{TEXT}" stroke-width="2" stroke-dasharray="5 5"/>')
    o.append(t(bx + bw + 10, 130, D["total"], 13, 600, MUTED))
    o.append(arrow(bx + bw + 60, 176, 880, ROSE, False))
    o.append(r(880, 118, 280, 100, PANEL, RED, rx=14, sw=2))
    o.append(t(1020, 158, D["rej"], 22, 800, RED, "middle", extra='letter-spacing="2"'))
    o.append(t(1020, 186, D["by"], fit(D["by"], 14, 258, 10), 500, MUTED, "middle"))
    o.append(t(1020, 206, D["would"], fit(D["would"], 14, 258, 10), 600, TEXT, "middle"))
    o.append(t(40, 244, D["foot"], 14, 500, MUTED))
    svg("d-vault", W, H, "".join(o))

def d_side(L):
    W, H = 1200, 270
    o = [r(0, 0, W, H, BG)]
    for i, ((big, lab, ttl, lines), col) in enumerate(zip(L["side"], [VIOLET, GREEN, AMBER])):
        x = 20 + i * 394
        o.append(r(x, 10, 372, 250, PANEL, LINE, rx=18) + r(x, 10, 372, 5, col, rx=2))
        o.append(t(x + 26, 84, big, 56, 800, col, extra='letter-spacing="-2"'))
        o.append(t(x + 26 + (len(big) * 34 + 14), 84, lab, 16, 600, MUTED))
        o.append(t(x + 26, 124, ttl, fit(ttl, 20, 320, 14), 800))
        for j, ln in enumerate(lines):
            o.append(t(x + 26, 156 + j * 24, ln, fit(ln, 14, 322, 10), 500, MUTED))
    svg("d-side", W, H, "".join(o))

def toolbox(L):
    skills = [(L["rows"][0], TEAL, ["JavaScript", "Python", "SQL"]), (L["rows"][1], AMBER, ["React", "Vite", "Node.js", "Express", "Prisma", "REST APIs"]),
              (L["rows"][2], ROSE, ["PostgreSQL", "MySQL", "SQLite"]), (L["rows"][3], VIOLET, ["PyTorch", "Transformers", "scikit-learn", "pandas"]),
              (L["rows"][4], GREEN, ["Docker", "Nginx", "Railway", "Git", "Playwright", "pytest"]), (L["rows"][5], AMBER, L["creative"]),
              (L["rows"][6], BLUE, L["spoken"])]
    W, rh = 1200, 64
    H = rh * len(skills) + 24
    o = [r(0, 0, W, H, BG)]
    for i, (lab, col, items) in enumerate(skills):
        y = 12 + i * rh
        o.append(f'<circle cx="46" cy="{y + 28}" r="6" fill="{col}"/>')
        o.append(t(66, y + 35, lab, 20, 700))
        x = 250
        for it in items:
            c, w = chip(x, y + 10, it, col, 16, 15)
            o.append(c); x += w + 10
        if i < len(skills) - 1:
            o.append(r(40, y + rh - 2, W - 80, 1, LINE))
    svg("toolbox", W, H, "".join(o))

def nxt(L):
    D = L["nxt"]
    W, H = 1200, 200
    o = [r(0, 0, W, H, PANEL), r(0, 0, W, 4, ROSE)]
    o.append(t(60, 62, D["k"], 14, 700, ROSE, font=MONO, extra='letter-spacing="3"'))
    o.append(t(60, 118, D["h"], fit(D["h"], 34, 1080, 22), 800, TEXT, extra='letter-spacing="-.5"'))
    o.append(t(60, 156, D["s"], fit(D["s"], 17, 1080, 12), 500, MUTED))
    o.append(r(60, 176, 1080, 6, "#0b0c10", rx=3))
    o.append(f'<rect x="60" y="176" width="1080" height="6" rx="3" fill="{ROSE}" style="transform-box:fill-box;transform-origin:left;animation:ld 7s ease-in-out infinite alternate"/>')
    svg("next", W, H, "".join(o), "@keyframes ld{from{transform:scaleX(.12)}to{transform:scaleX(.62)}}")

def buttons(L):
    for name, label, col in zip(["btn-linkedin", "btn-github", "btn-research"], L["btn"], [BLUE, TEAL, ROSE]):
        w, h = 280, 64
        svg(name, w, h, r(1, 1, w - 2, h - 2, PANEL, col, rx=14, sw=2) + t(28, 40, label, 20, 700) + t(w - 30, 41, "→", 24, 700, col, "end"))

for LANG in ["en", "tr", "ar"]:
    L = S[LANG]
    hero(L)
    for i, ((sc, ti, ge), col) in enumerate(zip(L["slates"], [AMBER, TEAL, BLUE, ROSE, AMBER, VIOLET, GREEN, ROSE])):
        slate(f"s{i}", sc, ti, ge, col)
    d_orcha(L); d_leak(L); d_twist(L); d_vault(L); d_side(L); toolbox(L); nxt(L); buttons(L)

# ---------------------------------------------------------------- language switcher pills (shared)
LANG = "en"
def pill(name, label, on, col):
    w, h = 150, 48
    body = (r(1, 1, w - 2, h - 2, col, rx=24) + t(w / 2, 31, label, 19, 800, BG, "middle")) if on else \
           (r(1, 1, w - 2, h - 2, PANEL, col, rx=24, sw=2) + t(w / 2, 31, label, 19, 700, col, "middle"))
    os.makedirs(ROOT, exist_ok=True)
    open(f"{ROOT}/{name}.svg", "w").write(f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">{body}</svg>')
for code, label, col in [("en", "English", TEAL), ("ar", "العربية", AMBER), ("tr", "Türkçe", ROSE)]:
    pill(f"lang-{code}", label, False, col)
    pill(f"lang-{code}-on", label, True, col)
print("story2 ok")
