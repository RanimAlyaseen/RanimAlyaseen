import sys, os
from px import *
OUT = sys.argv[1]
MUTED = "#9b92c4"

def save(path, w, h, body):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, "w").write(f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}"><style>.blink{{animation:bl 1.1s steps(1) infinite}}@keyframes bl{{50%{{opacity:0}}}}</style>{body}</svg>')

# ------------------------------------------------------------ language selector pills
def pill(code, label, col, on):
    w, h = 200, 60
    o = [frame(0, 0, w, h, col if on else INK, col if on else col)]
    if not on:
        o = [frame(0, 0, w, h, INK, col)]
    g, tw_ = txt(0, 0, label, 3, INK if on else col)
    # centre the label
    g, tw_ = txt(w // 2, 20 if not AR_RE.search(label) else 14, label, 3, INK if on else col, anchor="middle")
    o.append(g)
    if on:
        o.append(rect(10, h - 10, w - 20, 4, INK))
    save(f"{OUT}/lang-{code}{'-on' if on else ''}.svg", w, h, "".join(o))
for code, label, col in [("en", "ENGLISH", TEAL), ("ar", "العربية", ORANGE), ("tr", "TÜRKÇE", ROSE)]:
    pill(code, label, col, False); pill(code, label, col, True)

# ------------------------------------------------------------ character sheet (3 languages)
D = {
 "en": dict(name="RANIM", cap="CHARACTER SHEET", rows=[("CLASS", "SOFTWARE ENGINEER", AMBER), ("HOBBIES", "GRAPHIC DESIGN + VIDEO EDITING", ROSE),
            ("YEAR", "SOFTWARE ENGINEERING, FINAL YEAR", TEAL), ("UNI", "ISTINYE UNIVERSITY, ISTANBUL", BLUE)],
            langs="LANGUAGES", chips=["ENGLISH", "ARABIC", "TURKISH"], cnt=[("6", "PROJECTS"), ("3", "LANGUAGES")]),
 "tr": dict(name="RANIM", cap="KARAKTER KARTI", rows=[("SINIF", "YAZILIM MÜHENDİSİ", AMBER), ("HOBİLER", "GRAFİK TASARIM + VİDEO KURGU", ROSE),
            ("YIL", "YAZILIM MÜHENDİSLİĞİ, SON SINIF", TEAL), ("OKUL", "İSTİNYE ÜNİVERSİTESİ, İSTANBUL", BLUE)],
            langs="DİLLER", chips=["İNGİLİZCE", "ARAPÇA", "TÜRKÇE"], cnt=[("6", "PROJE"), ("3", "DİL")]),
 "ar": dict(name="رنيم", cap="بطاقة الشخصية", rows=[("التخصص", "هندسة البرمجيات", AMBER), ("هوايات", "التصميم الجرافيكي ومونتاج الفيديو", ROSE),
            ("السنة", "الأخيرة في هندسة البرمجيات", TEAL), ("الجامعة", "جامعة إستينيه، إسطنبول", BLUE)],
            langs="اللغات", chips=["الإنجليزية", "العربية", "التركية"], cnt=[("6", "مشاريع"), ("3", "لغات")]),
}
HELLO = ["HELLO", "مرحبا", "MERHABA"]
COLS = [TEAL, ORANGE, ROSE]

def sheet(lang):
    d = D[lang]; R = lang == "ar"
    W, H = 1200, 400
    M = lambda x, w=0: (W - x - w) if R else x           # mirror a box
    o = [frame(0, 0, W, H, NIGHT, PLUM)]
    # portrait
    px_ = M(30, 300)
    o.append(frame(px_, 30, 300, 340, INK, TEAL))
    for i, c in enumerate(["#321a58", "#6b2a72", "#b8426a", "#ee7a4b"]):
        o.append(rect(px_ + 12, 42 + i * 62, 276, 62, c))
    spr = sprite(CHIBI[:25], CHIBI_LEG, px_ + 54, 84, 8)
    o.append(f'<g transform="translate({2*(px_+150)},0) scale(-1,1)">{spr}</g>' if R else spr)
    o.append(rect(px_ + 12, 290, 276, 68, INK))
    if R:
        g, w, h = apix(d["name"], 26, 3, YELLOW, px_ + 150, 284, "middle", shadow=ORANGE); o.append(g)
    else:
        o.append(ptext(px_ + 150, 296, d["name"], 6, YELLOW, anchor="middle", shadow=ORANGE))
    g, _ = txt(px_ + 150, 340 if not R else 336, d["cap"], 2, CREAM, anchor="middle"); o.append(g)
    # rows
    x0 = 370
    for i, (k, v, c) in enumerate(d["rows"]):
        y = 36 + i * 36
        if R:
            g, kw = txt(W - x0, y, k, 3, MUTED, anchor="end"); o.append(g)
            g, _ = txt(W - x0 - 150, y, v, 3, c, anchor="end"); o.append(g)
        else:
            g, _ = txt(x0, y, k, 3, MUTED); o.append(g)
            g, _ = txt(x0 + 150, y, v, 3, c); o.append(g)
    o.append(rect(M(x0, 800), 190, 800, 4, PLUM))
    g, _ = txt(W - x0 if R else x0, 214, d["langs"], 3, CREAM, anchor="end" if R else "start"); o.append(g)
    # language chips
    cx = x0
    for name, col, hello in zip(d["chips"], COLS, HELLO):
        g, w_ = txt(0, 0, name, 3, col)
        w = w_ + 36
        bx = M(cx, w)
        o.append(frame(bx, 254, w, 48, INK, col))
        g, _ = txt(bx + w // 2, 268 if not AR_RE.search(name) else 262, name, 3, col, anchor="middle"); o.append(g)
        g, _ = txt(bx + w // 2, 322, hello, 2, CREAM, anchor="middle"); o.append(g)
        cx += w + 18
    # counters
    cx0 = M(930, 240) if not R else 30
    for i, ((num, lab), col) in enumerate(zip(d["cnt"], [GREEN, AMBER])):
        y = 222 + i * 70
        o.append(frame(cx0, y, 240, 56, INK, col))
        o.append(ptext(cx0 + 18, y + 14, num, 4, col))
        g, _ = txt(cx0 + 222, y + 21, lab, 2, CREAM, anchor="end"); o.append(g)
    save(f"{OUT}/{lang}/sheet.svg", W, H, "".join(o))
for l in ("en", "tr", "ar"):
    sheet(l)
print("ok")
