import sys; sys.argv=['x','/tmp']
from px import *
OLD=PLAYER_OLD
def base():
    g=[['.']*22 for _ in range(25)]
    for r,row in enumerate(OLD):
        for c,ch in enumerate(row): g[r][c]=ch
    for r in range(0,11):
        for c in range(22): g[r][c]='.'
    return g
def put(g,r,c,s):
    for i,ch in enumerate(s):
        if ch!=' ': g[r][c+i]=ch
def disc(g,cx,cy,rad,ch):
    for r in range(25):
        for c in range(22):
            if (c-cx)**2+(r-cy)**2<=rad*rad: g[r][c]=ch
LD=dict(PLAYER_OLD_LEG); LD.update(h="#0b0610",H="#2e2540",P="#05020a",o="#ff3d94",O="#7b3fd0",l="#e0197d",
    S="#ff7bbd",V="#b05cff",v="#8a4fe0",f="#ff3d94",w="#ffffff")

def make(style):
    g=base()
    disc(g,8,4.5,4.6,'h')                       # head hair
    if style=="pony":
        # hair pulled up and back: neat nape, tie at the back of the crown, long tail swinging down
        for r in range(5,10): put(g,r,3,"hhhhhhh")
        put(g,0,3,"hh"); put(g,1,2,"hhhh")
        put(g,0,1,"hhh"); put(g,1,0,"hhhh")           # tail rising
        put(g,2,0,"hhh"); put(g,3,0,"hhh")
        put(g,2,3,"SS"); put(g,3,3,"S")               # pink scrunchie at the tie
        for r,(c0,c1) in {4:(0,2),5:(0,2),6:(0,2),7:(0,2),8:(0,1),9:(0,1),10:(0,1),11:(0,1),12:(0,1)}.items():
            for c in range(c0,c1+1): g[r][c]='h'
        for (r,c) in ((1,1),(4,1),(7,1),(10,0)): g[r][c]='H'
    else:  # bob with blunt bangs
        for r in range(5,12): put(g,r,2,"hhhhhhhh")
        put(g,12,2,"hhhhhh"); put(g,13,2,"hhh") if False else None
        put(g,3,10,"hhhh"); put(g,2,11,"hhhh")
        for (r,c) in ((2,5),(4,4),(7,3),(9,4),(11,3)): g[r][c]='H'
    put(g,3,10,"hhh"); put(g,2,11,"hhh"); put(g,3,12,"h")     # fringe
    for (r,c) in ((2,6),(3,8),(5,6)): g[r][c]='H'
    # face
    put(g,3,12,"ssss"); put(g,4,12,"sskss"); put(g,5,12,"sssssd"); put(g,6,12,"sssss")
    put(g,7,11,"sssss"); put(g,7,16,"d"); put(g,8,11,"ssssd"); put(g,9,10,"sssss"); put(g,10,7,"ssssss")
    put(g,7,14,"ll"); put(g,3,13,"vvvv"); put(g,3,14,"kk"); put(g,4,16,"k"); put(g,4,17,"k")
    put(g,8,10,"S"); put(g,9,9,"V"); put(g,10,8,"SSVS")
    # headphones
    put(g,2,4,"OOOOOOOOO"); put(g,3,4,"O"); put(g,4,4,"O"); put(g,5,4,"O")
    put(g,3,8,"OOOO"); put(g,4,8,"OooO"); put(g,5,8,"OSoO"); put(g,6,8,"OooO"); put(g,7,8,"OOOO")
    # outfit
    put(g,11,6,"OOOOOOOO"); put(g,12,5,"OoooooooooO"); put(g,11,5,"S")
    return ["".join(r) for r in g]
pony=make("pony"); bob=make("bob")
dark=pony
if __name__=="__main__":
    S=11; body=""
    for i,(n,spr) in enumerate((("pony",pony),("bob",bob))):
        x=i*270
        body+=rect(x,0,260,16*S+40,"#8a3c6a")+rect(x,120,260,100,"#e8683a")+sprite(spr[:16],LD,x+14,30,S)+ptext(x+10,8,n.upper(),2,"#f6e8c8")
    open('/tmp/hs.svg','w').write(f'<svg xmlns="http://www.w3.org/2000/svg" width="540" height="{16*S+40}" viewBox="0 0 540 {16*S+40}"><rect width="100%" height="100%" fill="#140a26"/>{body}</svg>')
