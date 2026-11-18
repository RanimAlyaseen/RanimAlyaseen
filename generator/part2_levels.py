import sys, os
from px import *
OUT = sys.argv[1]
MUTED = "#9b92c4"
W = 1200

def save(path, w, h, body, css=""):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    base = (".blink{animation:bl 1.1s steps(1) infinite}@keyframes bl{50%{opacity:0}}"
            ".run{animation:run 2.4s steps(6) infinite}@keyframes run{from{transform:translateX(0)}to{transform:translateX(66px)}}"
            ".bob{animation:bob 1.2s steps(1) infinite}@keyframes bob{50%{transform:translateY(-6px)}}"
            ".pulse{animation:pu 1.6s steps(1) infinite}@keyframes pu{50%{opacity:.35}}")
    open(path, "w").write(f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}"><style>{base}{css}</style>{body}</svg>')

def fit(s, sc, maxw):
    while sc > 2 and txt(0, 0, s, sc, INK)[1] > maxw:
        sc -= 1
    return sc

def T(x, y, s, sc, col, anchor="start", maxw=None, shadow=None):
    if maxw: sc = fit(s, sc, maxw)
    return txt(x, y, s, sc, col, anchor, shadow)[0]

# ---------------------------------------------------------------- strings
L = {
"en": dict(
  banner1="> LEVELS", banner2="> SIDE QUESTS", lvl="LEVEL",
  status=["LIVE DEMO", "TEAM PROJECT", "UNIVERSITY PROJECT"],
  titles=["ORCHA", "MEDICAL ABSTRACT CLASSIFIER", "TOURISM CRM DATABASE"],
  rows=[[("WHAT", "AI AGENT CONTROL PLANE"), ("REVIEW", "HUMAN APPROVES / EDITS / REJECTS"), ("BUILT", "MULTI-TENANT, ROLES, JWT AUTH"), ("SHIPPED", "LIVE ON RAILWAY, 7 E2E TESTS")],
        [("WHAT", "5-CLASS DISEASE CLASSIFIER"), ("MY PART", "MODELS, BIOMEDBERT, EVALUATION"), ("FOUND", "988 SHARED TRAIN/TEST ABSTRACTS"), ("RESULT", "0.8603 MACRO F1, LOCKED TEST")],
        [("WHAT", "MYSQL LAYER FOR A TOURISM CRM"), ("BUILT", "9 TABLES, 3 VIEWS, 6 TRIGGERS"), ("GUARDS", "OVERPAYMENT + MISMATCHED REVIEWS"), ("TESTED", "SQL SUITE + 2-SESSION CONCURRENCY")]],
  tags=[["REACT", "NODE", "PRISMA", "POSTGRES", "DOCKER"], ["PYTHON", "PYTORCH", "TRANSFORMERS", "TEAM OF 5"], ["MYSQL 8", "SQL", "POWERSHELL"]],
  side=[("04", "CASIE EVENT EXTRACTION", "0.6196", "ARG-C F1", ["TEAM NLP PROJECT, 26 ROLES.", "MY PART: MODELING + EVAL."]),
        ("05", "ICELANDIC ASR DATA PREP", "0", "SHARED SPEAKERS", ["TEAM PROJECT. 20H SAMROMUR", "SUBSET FOR WHISPER + WAV2VEC."]),
        ("06", "BOOK RATING PREDICTION", "0.433", "ROC-AUC, NO EDGE", ["REPRODUCIBLE ML EXPERIMENT.", "REPORTED AS A NEGATIVE RESULT."])],
  links=["OPEN THE LIVE DEMO", "SOURCE"]),
"tr": dict(
  banner1="> BÖLÜMLER", banner2="> YAN GÖREVLER", lvl="BÖLÜM",
  status=["CANLI DEMO", "TAKIM PROJESİ", "ÜNİVERSİTE PROJESİ"],
  titles=["ORCHA", "TIBBİ ÖZET SINIFLANDIRICI", "TURİZM CRM VERİTABANI"],
  rows=[[("NE", "YAPAY ZEKÂ AJANI KONTROL PANELİ"), ("İNCELEME", "İNSAN ONAYLAR / DÜZENLER / REDDEDER"), ("KURULUM", "ÇOK KİRACILI, ROLLER, JWT"), ("YAYINDA", "RAILWAY'DE CANLI, 7 E2E TESTİ")],
        [("NE", "5 SINIFLI HASTALIK SINIFLANDIRICI"), ("PAYIM", "MODELLER, BIOMEDBERT, DEĞERLENDİRME"), ("BULUNDU", "988 ORTAK EĞİTİM/TEST ÖZETİ"), ("SONUÇ", "0,8603 MAKRO F1, KİLİTLİ TEST")],
        [("NE", "TURİZM CRM İÇİN MYSQL KATMANI"), ("KURULUM", "9 TABLO, 3 GÖRÜNÜM, 6 TETİKLEYİCİ"), ("KORUR", "FAZLA ÖDEME + UYUMSUZ YORUM"), ("TEST", "SQL TESTLERİ + EŞZAMANLILIK")]],
  tags=[["REACT", "NODE", "PRISMA", "POSTGRES", "DOCKER"], ["PYTHON", "PYTORCH", "TRANSFORMERS", "5 KİŞİLİK TAKIM"], ["MYSQL 8", "SQL", "POWERSHELL"]],
  side=[("04", "CASIE OLAY ÇIKARIMI", "0,6196", "ARG-C F1", ["TAKIM NLP PROJESİ, 26 ROL.", "PAYIM: MODELLEME + DEĞERL."]),
        ("05", "İZLANDACA ASR VERİ HAZIRLIĞI", "0", "ORTAK KONUŞMACI", ["TAKIM PROJESİ. 20 SAATLİK", "SAMROMUR: WHISPER + WAV2VEC."]),
        ("06", "KİTAP PUANI TAHMİNİ", "0,433", "ROC-AUC", ["TEKRARLANABİLİR ML DENEYİ.", "SONUÇ: ÜSTÜNLÜK YOK."])],
  links=["CANLI DEMOYU AÇ", "KAYNAK"]),
"ar": dict(
  banner1="المراحل", banner2="مهام جانبية", lvl="المرحلة",
  status=["عرض مباشر", "مشروع فريق", "مشروع جامعي"],
  titles=["ORCHA", "مصنّف الملخصات الطبية", "قاعدة بيانات CRM للسياحة"],
  rows=[[("ما هو", "لوحة تحكم لوكلاء الذكاء الاصطناعي"), ("المراجعة", "إنسان يوافق أو يعدّل أو يرفض"), ("البناء", "متعدد المستأجرين، أدوار، JWT"), ("النشر", "منشور على Railway، 7 اختبارات E2E")],
        [("ما هو", "مصنّف أمراض بخمس فئات"), ("دوري", "تدريب النماذج، BiomedBERT، التقييم"), ("وُجد", "988 ملخصاً مشتركاً بين التدريب والاختبار"), ("النتيجة", "0.8603 ماكرو F1 على اختبار مقفل")],
        [("ما هو", "طبقة MySQL لنظام CRM سياحي"), ("البناء", "9 جداول و3 واجهات و6 مشغّلات"), ("الحماية", "يمنع الدفع الزائد والتقييم غير المطابق"), ("الاختبار", "اختبارات SQL وتزامن بجلستين")]],
  tags=[["REACT", "NODE", "PRISMA", "POSTGRES", "DOCKER"], ["PYTHON", "PYTORCH", "TRANSFORMERS", "TEAM OF 5"], ["MYSQL 8", "SQL", "POWERSHELL"]],
  side=[("04", "استخراج أحداث CASIE", "0.6196", "ARG-C F1", ["مشروع فريق لمعالجة اللغة، 26 دوراً.", "دوري: النمذجة والتقييم."]),
        ("05", "تجهيز بيانات ASR الآيسلندية", "0", "متحدثون مشتركون", ["مشروع فريق: 20 ساعة", "من Samromur لنموذجي", "Whisper وwav2vec."]),
        ("06", "التنبؤ بتقييم الكتب", "0.433", "ROC-AUC بلا أفضلية", ["تجربة تعلّم آلي قابلة للتكرار.", "نُشرت كنتيجة سلبية."])],
  links=["افتح العرض المباشر", "المصدر"]),
}
LV = [("01", TEAL, TEAL, GREEN), ("02", BLUE, BLUE, BLUE), ("03", AMBER, AMBER, AMBER)]
SIDE = [ROSE, GREEN, YELLOW]

# ---------------------------------------------------------------- sprites
BUBBLE = [".######.", "########", "########", "########", ".######.", "..##...."]
PHONE = ["..####..", ".#....#.", ".#....#.", ".#....#.", ".#....#.", ".######."]
MAIL = ["########", "##....##", "#.#..#.#", "#..##..#", "#......#", "########"]
CHECK = ["......#", ".....##", "#...##.", "##.##..", ".###...", "..#...."]
DOC = ["#######.", "#.....##", "#.###.#.", "#.....#.", "#.###.#.", "#.....#.", "#.###.#.", "#.....#.", "#######."]
BOLT = ["...##", "..##.", ".###.", "#####", "..##.", ".##..", ".#..."]
COIN = ["..###..", ".#####.", "###.###", "###.###", "###.###", ".#####.", "..###.."]
LENS = [".#####.", "##...##", "#.....#", "#.....#", "#.....#", "##...##", ".#####.", "......##", ".......##"]
SHIELD = ["..######..", ".########.", "##.####.##", "##.####.##", "##..##..##", ".##....##.", "..######..", "...####...", "....##...."]
BOOK = ["########..", "#......#..", "#.####.#..", "#......#..", "#.###..#..", "#......#..", "########.."]

def panel(ox, oy, w, h, c1, c2, c3, c4):
    o = []
    bh = (h - 48) // 4
    for i, c in enumerate([c1, c2, c3, c4]):
        o.append(rect(ox, oy + i * bh, w, bh + 1, c))
    o.append(rect(ox, oy + h - 48, w, 48, "#0e0720"))
    for x in range(0, w, 24):
        o.append(rect(ox + x, oy + h - 48, 12, 6, "#1d1038"))
    return o

def scene_orcha(ox, oy):
    o = panel(ox, oy, 300, 240, "#1b1033", "#2d1b4e", "#3d2a6a", "#5b2a6e")
    o.append(rect(ox + 106, oy + 78, 100, 114, "#2b2d4e") + rect(ox + 110, oy + 82, 92, 106, "#1a1c3a"))
    for r_ in range(4):
        for c_ in range(3):
            col = [TEAL, AMBER, ROSE, BLUE][(r_ + c_) % 4]
            o.append(rect(ox + 118 + c_ * 28, oy + 94 + r_ * 24, 16, 12, col, f'class="pulse" style="animation-delay:-{(r_ * 3 + c_) * .2:.1f}s"'))
    o.append(rect(ox + 150, oy + 44, 8, 34, "#2b2d4e") + rect(ox + 144, oy + 32, 20, 12, RED, 'class="blink"'))
    for i, (spr, col) in enumerate([(BUBBLE, GREEN), (PHONE, BLUE), (MAIL, AMBER)]):
        yy = oy + 60 + i * 48
        o.append(sprite(spr, {"#": col}, ox + 18, yy, 5))
        o.append(f'<g class="run" style="animation-delay:-{i*.7:.1f}s">{rect(ox + 56, yy + 12, 6, 6, col)}</g>')
    o.append(rect(ox + 214, oy + 88, 6, 100, AMBER))                       # review gate
    o.append(rect(ox + 208, oy + 82, 18, 8, AMBER) + rect(ox + 208, oy + 186, 18, 6, AMBER))
    o.append(sprite(PLAYER[:11], PLAYER_LEG, ox + 238, oy + 142, 3))
    o.append(rect(ox + 240, oy + 172, 28, 20, TEAL))
    o.append(sprite(CHECK, {"#": GREEN}, ox + 246, oy + 114, 4, 'class="bob"'))
    return "".join(o)

def scene_med(ox, oy):
    o = panel(ox, oy, 300, 240, "#10213a", "#16345c", "#1e4a7a", "#2a6a9a")
    o.append(rect(ox + 30, oy + 48, 140, 126, "#4cc9f0") + rect(ox + 34, oy + 52, 132, 118, "#12305a"))
    o.append(rect(ox + 110, oy + 66, 140, 126, ROSE) + rect(ox + 114, oy + 70, 132, 118, "#4a1d3a"))
    o.append(rect(ox + 110, oy + 66, 60, 108, AMBER) + rect(ox + 114, oy + 70, 52, 100, "#6b3a1a"))
    for i in range(5):
        o.append(rect(ox + 44, oy + 66 + i * 20, 60 if i % 2 else 80, 6, BLUE))
        o.append(rect(ox + 178, oy + 84 + i * 20, 56 if i % 2 else 40, 6, "#ff9db5"))
    o.append(ptext(ox + 140, oy + 108, "988", 4, YELLOW, anchor="middle", shadow=INK))
    o.append(f'<g class="bob">{sprite(LENS, {"#": CREAM}, ox + 190, oy + 24, 6)}</g>')
    return "".join(o)

def scene_crm(ox, oy):
    o = panel(ox, oy, 300, 240, "#2a1608", "#4a2410", "#7a3a1a", "#a8541e")
    for i in range(3):
        yy = oy + 80 + i * 34
        o.append(rect(ox + 28, yy, 100, 30, "#5e311c") + rect(ox + 28, yy, 100, 8, "#e8a35a") + rect(ox + 28, yy + 26, 100, 4, "#3a1d0e"))
        o.append(rect(ox + 100, yy + 14, 8, 6, GREEN, 'class="pulse"') + rect(ox + 112, yy + 14, 8, 6, AMBER))
    o.append(f'<g class="run">{sprite(COIN, {"#": YELLOW}, ox + 134, oy + 118, 4)}</g>')
    o.append(rect(ox + 214, oy + 70, 12, 120, RED))
    for i in range(6):
        o.append(rect(ox + 214, oy + 70 + i * 20, 12, 10, CREAM))
    o.append(rect(ox + 206, oy + 62, 28, 8, RED) + rect(ox + 206, oy + 190, 28, 6, RED))
    o.append(sprite(BOLT, {"#": YELLOW}, ox + 244, oy + 40, 6, 'class="blink"'))
    o.append(sprite(["#...#", ".#.#.", "..#..", ".#.#.", "#...#"], {"#": RED}, ox + 252, oy + 130, 6))
    return "".join(o)

SCENES = [scene_orcha, scene_med, scene_crm]

# ---------------------------------------------------------------- level cards
def card(lang, i):
    d = L[lang]; R = lang == "ar"
    num, col, tagcol, stcol = LV[i]
    CW, CH = W, 300
    M = lambda x, w=0: (CW - x - w) if R else x
    o = [frame(0, 0, CW, CH, NIGHT, col, hi="#ffffff22")]
    # scene
    sx = M(28, 300)
    o.append(f'<clipPath id="c{i}"><rect x="{sx}" y="30" width="300" height="240"/></clipPath>')
    o.append(f'<g clip-path="url(#c{i})">{SCENES[i](sx, 30)}</g>')
    o.append(rect(sx - 4, 26, 308, 4, col) + rect(sx - 4, 270, 308, 4, col) + rect(sx - 4, 26, 4, 248, col) + rect(sx + 300, 26, 4, 248, col))
    # text column
    tx0 = 28 + 300 + 30                   # distance from the near edge
    right = CW - tx0 if R else tx0
    anc = "end" if R else "start"
    avail = CW - tx0 - 28
    # header
    o.append(T(right, 24, f"{d['lvl']} {num}", 3, col, anc))
    status = d["status"][i]
    sw = txt(0, 0, status, 2, INK)[1] + 24
    sbx = (28 if R else CW - 28 - sw)
    o.append(rect(sbx, 22, sw, 28, stcol) + T(sbx + sw // 2, 29 if not AR_RE.search(status) else 24, status, 2, INK, "middle"))
    o.append(T(right, 64 if (R and AR_RE.search(d["titles"][i])) else 60, d["titles"][i], 3 if (R and AR_RE.search(d["titles"][i])) else 4, CREAM, anc, maxw=avail, shadow=PURPLE))
    o.append(rect(M(tx0, avail), 108, avail, 4, PURPLE))
    # rows
    for r_, (k, v) in enumerate(d["rows"][i]):
        y = 128 + r_ * 32
        if R:
            o.append(T(right, y + 3, k, 2, MUTED, "end"))
            o.append(T(right - 120, y + 1, v, 2, CREAM, "end", maxw=avail - 120))
        else:
            o.append(T(right, y + 3, k, 2, MUTED))
            o.append(T(right + 130, y, v, 3, CREAM, maxw=avail - 130))
    # tags
    x = right
    for t in d["tags"][i]:
        w = tw(t.upper(), 2) + 20 if not AR_RE.search(t) else txt(0, 0, t, 2, INK)[1] + 20
        bx = x - w if R else x
        o.append(rect(bx, 256, w, 26, tagcol) + rect(bx + 2, 258, w - 4, 22, INK) + T(bx + w // 2, 263, t, 2, tagcol, "middle"))
        x = bx - 8 if R else x + w + 8
    save(f"{OUT}/{lang}/level-{num}.svg", CW, CH, "".join(o))

def banner(lang, name, label, col):
    R = lang == "ar"
    b = rect(0, 0, W, 64, NIGHT) + rect(0, 56, W, 8, col) + rect(0, 52, W, 4, PURPLE)
    if AR_RE.search(label):
        _, aw, ah = apix(label, 22, 2, col, 0, 0)
        g, _, _ = apix(label, 22, 2, col, W - 24, (52 - ah) // 2, "end", shadow=PLUM); b += g
    else:
        b += T(W - 24 if R else 24, 14, label, 5, col, "end" if R else "start", shadow=PLUM)
    save(f"{OUT}/{lang}/{name}.svg", W, 64, b)

# ---------------------------------------------------------------- side-quest cards
def side(lang, i):
    d = L[lang]; R = lang == "ar"
    n, title, big, lab, lines = d["side"][i]
    col = SIDE[i]
    CW, CH = 392, 250
    M = lambda x, w=0: (CW - x - w) if R else x
    anc = "end" if R else "start"
    xa = CW - 24 if R else 24
    o = [frame(0, 0, CW, CH, NIGHT, col)]
    o.append(T(xa, 22, n, 3, col, anc))
    icon = [SHIELD, None, BOOK][i]
    ix = M(CW - 24 - 60, 60) if False else (24 if R else CW - 24 - 60)
    if icon:
        o.append(sprite(icon, {"#": col}, ix, 20, 6 if i == 0 else 6))
    else:  # sound wave
        for k, hh in enumerate([14, 30, 46, 22, 38, 16, 28, 10]):
            o.append(rect(ix + k * 8, 20 + 48 - hh, 6, hh, col, f'class="pulse" style="animation-delay:-{k*.2:.1f}s"'))
    o.append(T(xa, 86, title, 3, CREAM, anc, maxw=CW - 48))
    o.append(rect(M(24, CW - 48), 118, CW - 48, 4, PURPLE))
    bw = tw(big.upper(), 5)
    o.append(ptext(M(24, bw), 134, big, 5, col, shadow=PLUM))
    lx = (CW - 24 - bw - 14) if R else (24 + bw + 14)
    o.append(T(lx, 146, lab, 2, MUTED, "end" if R else "start", maxw=CW - 24 - bw - 14 - 24))
    for j, ln in enumerate(lines):
        o.append(T(xa, 178 + j * 22, ln, 2, CREAM, anc, maxw=CW - 48))
    save(f"{OUT}/{lang}/side-{n}.svg", CW, CH, "".join(o))

for lang in ("en", "tr", "ar"):
    for i in range(3):
        card(lang, i); side(lang, i)
    banner(lang, "b-levels", L[lang]["banner1"], AMBER)
    banner(lang, "b-side", L[lang]["banner2"], BLUE)
print("ok")
