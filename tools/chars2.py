import sys,os,numpy as np
from PIL import Image
from scipy import ndimage
D=os.path.expanduser('~/Downloads/')
N='ดีไซน์ที่ยังไม่ได้ตั้งชื่อ'
def f(x): return D+(f'{N} ({x}).png' if isinstance(x,int) else f'{N} - 2026-11-14T{x}.png')
SHEET={0:94,1:92,2:88,3:91,4:73,5:93,6:89,7:90,'npc':'112036.886'}
STD={0:97,1:'111513.008',2:96,3:100,4:95,5:'111534.231',6:98,7:99,'npc':'111739.938'}
POSES=['happy','shock','sad','work','thumb','think','angry','wave']
OUT=os.path.join(os.path.dirname(__file__),'out/');os.makedirs(OUT,exist_ok=True)
def cutout(im):
    a=np.asarray(im.convert('RGB')).astype(int)
    bg=(a.min(2)>232)&((a.max(2)-a.min(2))<22)
    lab,n=ndimage.label(bg)
    edge=set(np.unique(np.concatenate([lab[0],lab[-1],lab[:,0],lab[:,-1]])))-{0}
    m=np.isin(lab,list(edge))
    fg=~m
    fg=ndimage.binary_opening(fg,iterations=2)
    alpha=ndimage.gaussian_filter(fg.astype(float),0.8)
    alpha=np.clip((alpha-0.15)/0.7,0,1)
    rgba=np.dstack([a,(alpha*255)]).astype('uint8')
    return Image.fromarray(rgba,'RGBA'),fg
def fit(im,H=720):  # ท่าทาง: สูงสุด 720px (ย่ออย่างเดียว ไม่ขยาย) ให้คมบนจอความละเอียดสูง · เดิม 420
    bb=im.getbbox();im=im.crop(bb)
    if im.height<=H:return im
    return im.resize((max(1,round(im.width*H/im.height)),H),Image.LANCZOS)
DIL={5:8,7:5}  # ชีต c5/c7 ตัวละครอยู่ชิดกัน ใช้ขยายมาสก์น้อยลง ไม่งั้นท่าบน-ล่างติดกัน
def split(im,fg,it=12):
    big=ndimage.binary_dilation(fg,iterations=it)
    lab,n=ndimage.label(big);objs=ndimage.find_objects(lab)
    sizes=[(fg[o]&(lab[o]==i+1)).sum() for i,o in enumerate(objs)]
    idx=sorted(range(n),key=lambda i:-sizes[i])[:8]
    boxes=[]
    for i in idx:
        o=objs[i];boxes.append((o[0].start,o[0].stop,o[1].start,o[1].stop,i+1))
    H=fg.shape[0]
    boxes.sort(key=lambda b:((b[0]+b[1])/2>H/2,b[2]))
    out=[]
    for y0,y1,x0,x1,k in boxes:
        sub=np.asarray(im)[y0:y1,x0:x1].copy();sub[...,3]=sub[...,3]*(lab[y0:y1,x0:x1]==k)
        out.append(Image.fromarray(sub,'RGBA'))
    return out,[(b[1]-b[0]) for b in boxes],[b[1] for b in boxes]
def head(std):
    a=np.asarray(std);al=a[...,3]>128;ys=np.where(al.any(1))[0];top=ys[0];h=ys[-1]-top
    hh=int(h*0.17);band=al[top:top+hh];xs=np.where(band.any(0))[0];cx=(xs[0]+xs[-1])//2
    s=int(hh*1.15);x0=cx-s//2;y0=max(0,top-int(s*0.06))
    c=std.crop((x0,y0,x0+s,y0+s));return c.resize((128,128),Image.LANCZOS)
if __name__=='__main__':
    for key in SHEET:
        tag=f'c{key}' if key!='npc' else 'npc'
        sh,fg=cutout(Image.open(f(SHEET[key])))
        parts,hs,bots=split(sh,fg,DIL.get(key,12))
        print(key,'parts',len(parts),'heights',hs,'bottoms',bots,'H',sh.height)
        for p,name in zip(parts,POSES): fit(p).save(OUT+f'{tag}-{name}.webp',quality=88)
        st,_=cutout(Image.open(f(STD[key])));st=st.crop(st.getbbox())
        fit(st).save(OUT+(f'pawn-{key}.webp' if key!='npc' else 'npc-std.webp'),quality=88)
        if key!='npc': head(st).save(OUT+f'head-{key}.webp',quality=90)
