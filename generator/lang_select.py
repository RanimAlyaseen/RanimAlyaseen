# Compact "language" dropdown pill (used as the <summary> of a <details> in the READMEs)
import sys, os, re
from px import *
OUT = sys.argv[1]
AR_RE = re.compile(r'[؀-ۿ]')

def save(path, w, h, body):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, "w").write(f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}">{body}</svg>')

W, H = 200, 60
for code, label in [("en", "LANGUAGE"), ("tr", "DİL"), ("ar", "اللغة")]:
    o = [frame(0, 0, W, H, INK, YELLOW)]
    ar = bool(AR_RE.search(label))
    g, _ = txt(W // 2, 14 if ar else 20, label, 3, YELLOW, anchor="middle")
    o.append(g)
    save(f"{OUT}/lang-select-{code}.svg", W, H, "".join(o))
