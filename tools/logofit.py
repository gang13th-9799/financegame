import numpy as np
from PIL import Image,ImageFilter
from scipy import ndimage
LM=np.load(__import__('os').path.join(__import__('os').path.dirname(__file__),'logomask.npy')).astype(float)
def fit_sign(a,X,Y,R,thr=None):
    H,W=a.shape[:2];k=int(R*1.3)
    x0,y0=max(0,int(X-k)),max(0,int(Y-k));win=a[y0:int(Y+k),x0:int(X+k)].astype(int)
    lum=win.mean(2);sat=win.max(2)-win.min(2)
    best=None
    for t in ([thr] if thr else [235,225,215,205,195,185,175]):
        wh=(lum>t)&(sat<46);wh=ndimage.binary_opening(wh,iterations=3);wh=ndimage.binary_fill_holes(wh)
        lab,n=ndimage.label(wh)
        for i in range(1,n+1):
            m=lab==i;ar=m.sum()
            if ar<(R*.3)**2: continue
            ys,xs=np.nonzero(m);h=np.ptp(ys)+1;w=np.ptp(xs)+1
            if ys.min()==0 or xs.min()==0 or ys.max()==m.shape[0]-1 or xs.max()==m.shape[1]-1: continue
            fill=ar/(np.pi*h*w/4);asp=min(h,w)/max(h,w)
            if fill<.85 or asp<.6: continue
            sc=ar*fill
            if best is None or sc>best[0]: best=(sc,m,t)
    m=best[1];ys,xs=np.nonzero(m);cy,cx=ys.mean(),xs.mean()
    cov=np.cov(np.vstack([xs-cx,ys-cy]));ev,evec=np.linalg.eigh(cov)
    ax=4*np.sqrt(ev)
    ang=np.degrees(np.arctan2(evec[1,1],evec[0,1]))
    full=np.zeros(a.shape[:2],bool);full[y0:y0+m.shape[0],x0:x0+m.shape[1]]=m
    full=ndimage.binary_erosion(full,iterations=3)
    return cx+x0,cy+y0,ax[1],ax[0],ang,full
def place(im,sign,color,scale=.62):
    cx,cy,maj,mnr,ang,mask=sign
    a=np.asarray(im.convert('RGB')).astype(float)
    mh,mw=LM.shape;base=max(mh,mw)
    # logo as square image, scaled to fit unit circle then stretched to ellipse
    L=Image.fromarray((LM*255).astype('uint8'))
    sz=int(mnr*scale);L=L.resize((max(1,int(mw/base*sz)),max(1,int(mh/base*sz))),Image.LANCZOS)
    # stretch along major axis direction: rotate so major is horizontal, stretch, rotate back
    st=maj/mnr
    L=L.rotate(ang,expand=True,resample=Image.BICUBIC)
    L=L.resize((int(L.width*st),L.height),Image.LANCZOS)
    L=L.rotate(-ang,expand=True,resample=Image.BICUBIC)
    A=np.zeros(a.shape[:2]);x=int(cx-L.width/2);y=int(cy-L.height/2)
    A[y:y+L.height,x:x+L.width]=np.asarray(L)/255.
    A=ndimage.gaussian_filter(A,0.6)*mask
    # shading from sign luminance
    lum=a.mean(2);ref=np.median(lum[mask]);shade=np.clip(lum/ref,0.75,1.12)[...,None]
    col=np.array(color,float)[None,None,:]*shade
    out=a*(1-A[...,None])+col*A[...,None]
    return Image.fromarray(np.clip(out,0,255).astype('uint8'))
