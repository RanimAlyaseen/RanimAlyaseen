# Original chibi character: short messy black bob, big eyes, headphones, pink/purple accents. 24 x 36 grid.
import math
CHIBI_LEG = dict(k="#16111f", K="#43336a", s="#f7e1d3", d="#e6bfae", m="#c9808a", p="#ff6fb3",
                 e="#1b1530", v="#7a5ad0", w="#ffffff", B="#7b3fd0", C="#7b3fd0", c="#ff7bbd",
                 D="#1d1829", E="#352c52", R="#ff3d94", T="#0e0a16", t="#ff7bbd", o="#120e1a", L="#9a5cf0")
def build():
    W, H = 24, 36
    g = [['.'] * W for _ in range(H)]
    def put(r, c, s):
        for i, ch in enumerate(s):
            if ch != ' ' and 0 <= c + i < W: g[r][c + i] = ch
    def ell(cx, cy, rx, ry, ch):
        for r in range(H):
            for c in range(W):
                if ((c - cx) / rx) ** 2 + ((r - cy) / ry) ** 2 <= 1: g[r][c] = ch
    # hair: messy bob that falls to the shoulders
    ell(11.5, 8.5, 10.2, 8.2, 'k')
    for c, end in zip(range(1, 6), (17, 19, 20, 18, 16)):
        for r in range(9, end + 1): g[r][c] = 'k'
    for c, end in zip(range(18, 23), (16, 18, 20, 19, 17)):
        for r in range(9, end + 1): g[r][c] = 'k'
    # face
    ell(11.5, 11.7, 7.3, 6.0, 's')
    for r in range(15, 18):                                  # soft chin shade
        for c in range(W):
            if g[r][c] == 's' and (c < 6 or c > 17): g[r][c] = 'd'
    # choppy fringe
    fr = [3, 4, 5, 3, 4, 2, 4, 5, 3, 3, 5, 4, 2, 4, 5, 3]
    for i, ln in enumerate(fr):
        c = 4 + i
        for r in range(5, 5 + ln):
            if g[r][c] in 'sd': g[r][c] = 'k'
    # hair shine
    for (r, c) in ((1, 9), (1, 10), (2, 7), (2, 14), (3, 5), (3, 17), (6, 6), (6, 15), (13, 2), (15, 21), (8, 3), (8, 20)):
        if g[r][c] == 'k': g[r][c] = 'K'
    # eyes (big, dark, with a highlight)
    for c0 in (6, 14):
        put(10, c0, "eeee"); put(11, c0, "ewve"); put(12, c0, "evve"); put(13, c0, ".ee.")
    put(14, 11, "d"); put(16, 11, "mm")                      # nose, mouth
    # headphones: pink band over the hair, purple cups with pink centres
    def top(c): return 8.5 - 8.2 * math.sqrt(max(0, 1 - ((c - 11.5) / 10.2) ** 2))
    for c in range(2, 22):
        a = int(round(top(c))) + 1; b = int(round(top(c + 1 if c < 11 else c - 1))) + 1
        for r in range(min(a, b), max(a, b) + 1): g[r][c] = 'B'
    for r in range(6, 9):
        g[r][2] = 'B'; g[r][21] = 'B'
    for c0 in (0, 21):
        for r in range(8, 15):
            for c in range(c0, c0 + 3): g[r][c] = 'C'
        for r in (10, 11, 12): g[r][c0 + 1] = 'c'
    # neck + choker
    put(17, 10, "dsss"); put(18, 9, "TTLTTT")
    # body: shoulders, bare arms, sleeveless dress
    put(19, 8, "sssssss"); put(19, 5, "ss"); put(19, 15, "ss")
    for r in range(20, 28):
        put(r, 5, "ss"); put(r, 17, "ss")
    put(20, 7, "DDsssDDD"[:0] + "DD" + "ssss" + "DD")
    put(21, 7, "DDDDDDDDDD")
    put(22, 7, "LLLLLLLLLL")                      # crop-top hem (purple trim)
    put(23, 7, "ssssssssss")                      # bare midriff
    put(24, 7, "ssssdsssss")                      # (tiny navel)
    put(25, 7, "RRRRRRRRRR")
    for r, (c0, c1) in {26: (6, 17), 27: (5, 18), 28: (5, 18), 29: (4, 19), 30: (4, 19)}.items():
        for c in range(c0, c1 + 1): g[r][c] = 'D'
    for r in (27, 28, 29, 30): put(r, 8, "EE"); put(r, 14, "EE")
    for c in range(4, 20): g[31][c] = 'L' if c % 2 == 0 else 'D'
    put(27, 3, "sss"); put(27, 18, "sss"); put(28, 3, "ss"); put(28, 19, "ss")   # hands
    # legs, socks, boots
    put(32, 9, "ss"); put(32, 13, "ss")
    put(33, 8, "LLLL"); put(33, 12, "LLLL")
    put(34, 8, "oooo"); put(34, 12, "oooo")
    put(35, 6, "ooooo"); put(35, 12, "ooooo")
    # close the see-through gaps around the eyes, jaw and neck
    for (r, c, ch) in ((13,6,'s'),(13,9,'s'),(13,14,'s'),(13,17,'s'),(16,6,'s'),(16,17,'s'),
                       (17,7,'d'),(17,8,'d'),(17,15,'d'),(17,16,'d'),(17,5,'k'),(17,6,'k'),(17,17,'k'),(17,18,'k'),
                       (18,5,'k'),(18,6,'k'),(18,7,'k'),(18,8,'k'),(18,15,'k'),(18,16,'k'),(18,17,'k'),(18,18,'k'),
                       (19,4,'k'),(19,7,'s'),(19,17,'s'),(19,18,'s'),(19,19,'k')):
        g[r][c] = ch
    # cropped tee: short sleeves + round neckline, purple hem, short bare midriff above the pink belt
    put(19, 5, "DDDD"); put(19, 9, "ssssss"); put(19, 15, "DDDD")
    put(20, 5, "DDDDDDDDDDDDDD")
    put(21, 5, "DDEDDDDDDEDDDD")
    put(22, 5, "ss"); put(22, 7, "DDDDDDDDDD"); put(22, 17, "ss")
    put(23, 7, "ssssssssss")
    put(24, 7, "sssdssssss")
    return ["".join(r) for r in g]
CHIBI = build()
if __name__ == "__main__":
    import sys; sys.argv = ['x', '/tmp']
    sys.path.insert(0, '/home/claude/gen3')
    from px import sprite, rect
    S = 12
    body = rect(0, 0, 330, 450, "#8a3c6a") + rect(0, 300, 330, 150, "#e8683a") + sprite(CHIBI, CHIBI_LEG, 20, 10, S)
    open('/tmp/chibi.svg', 'w').write(f'<svg xmlns="http://www.w3.org/2000/svg" width="330" height="450" viewBox="0 0 330 450">{body}</svg>')
    print("\n".join(CHIBI))
