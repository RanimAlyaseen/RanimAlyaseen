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
            ("GRADUATION", "EXPECTED JUNE 2027", TEAL), ("UNI", "ISTINYE UNIVERSITY, ISTANBUL", BLUE)],
            langs="LANGUAGES", chips=["ENGLISH", "ARABIC", "TURKISH"], cnt=[("6", "PROJECTS"), ("3", "LANGUAGES")]),
 "tr": dict(name="RANİM", cap="KARAKTER KARTI", rows=[("SINIF", "YAZILIM MÜHENDİSİ", AMBER), ("HOBİLER", "GRAFİK TASARIM + VİDEO KURGU", ROSE),
            ("MEZUNİYET", "BEKLENEN: HAZİRAN 2027", TEAL), ("OKUL", "İSTİNYE ÜNİVERSİTESİ, İSTANBUL", BLUE)],
            langs="DİLLER", chips=["İNGİLİZCE", "ARAPÇA", "TÜRKÇE"], cnt=[("6", "PROJE"), ("3", "DİL")]),
 "ar": dict(name="رنيم", cap="بطاقة الشخصية", rows=[("التخصص", "هندسة البرمجيات", AMBER), ("هوايات", "التصميم الجرافيكي ومونتاج الفيديو", ROSE),
            ("التخرج", "متوقع في يونيو 2027", TEAL), ("الجامعة", "جامعة إستينيه، إسطنبول", BLUE)],
            langs="اللغات", chips=["الإنجليزية", "العربية", "التركية"], cnt=[("6", "مشاريع"), ("3", "لغات")]),
}
STATS = {
 "en": [("CODE", 7, TEAL, "7"), ("ARCHITECTURE", 7, BLUE, "7"), ("ML / NLP", 5, GREEN, "5"),
        ("DESIGN", 8, ORANGE, "8"), ("COFFEE", 10, YELLOW, "MAX"), ("SLEEP", 2, RED, "LOW")],
 "tr": [("KOD", 7, TEAL, "7"), ("MİMARİ", 7, BLUE, "7"), ("ML / NLP", 5, GREEN, "5"),
        ("TASARIM", 8, ORANGE, "8"), ("KAHVE", 10, YELLOW, "MAKS"), ("UYKU", 2, RED, "DÜŞÜK")],
 "ar": [("برمجة", 7, TEAL, "7"), ("معمارية", 7, BLUE, "7"), ("ذكاء اصطناعي", 5, GREEN, "5"),
        ("تصميم", 8, ORANGE, "8"), ("قهوة", 10, YELLOW, "أقصى"), ("نوم", 2, RED, "قليل")],
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
            g, _ = txt(W - x0 - 210, y, v, 3, c, anchor="end"); o.append(g)
        else:
            g, _ = txt(x0, y, k, 3, MUTED); o.append(g)
            g, _ = txt(x0 + 210, y, v, 3, c); o.append(g)
    o.append(rect(M(x0, 800), 190, 800, 4, PLUM))
    # languages: heading + small chips on one line
    hy = 208
    g, hw = txt(W - x0 if R else x0, hy, d["langs"], 3, CREAM, anchor="end" if R else "start"); o.append(g)
    cx = x0 + hw + 30
    for name, col in zip(d["chips"], COLS):
        ar = bool(AR_RE.search(name))
        w = (txt(0, 0, name, 2, col)[1] if ar else tw(name, 2)) + 22
        bx = M(cx, w)
        o.append(frame(bx, hy - 8, w, 34, INK, col))
        g, _ = txt(bx + w // 2, hy + (-2 if ar else 2), name, 2, col, anchor="middle"); o.append(g)
        cx += w + 14
    # stat bars: two columns of three
    st = STATS[lang]
    for i, (lab, v, col, vt) in enumerate(st):
        cxx = x0 + (i // 3) * 410
        y = 268 + (i % 3) * 38
        lx = M(cxx)
        g, _ = txt(lx, y + (-4 if AR_RE.search(lab) else 2), lab, 2, CREAM, anchor="end" if R else "start"); o.append(g)
        for k in range(10):
            sx = M(cxx + 168 + k * 18, 16)
            on = k < v
            o.append(rect(sx, y, 16, 18, col if on else PURPLE))
            if on:
                o.append(rect(sx, y, 16, 5, "#ffffff44"))
        vx = M(cxx + 168 + 190)
        g, _ = txt(vx, y + (-4 if AR_RE.search(vt) else 2), vt, 2, col, anchor="end" if R else "start"); o.append(g)
    save(f"{OUT}/{lang}/sheet.svg", W, H, "".join(o))
for l in ("en", "tr", "ar"):
    sheet(l)
print("ok")
