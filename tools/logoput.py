import sys,numpy as np
from PIL import Image,ImageFilter
from scipy import ndimage
def find_medallion(im,thr=215):
    b=np.asarray(im.convert('RGB')).astype(int);H,W=b.shape[:2]
    top=b[:int(H*.45)]
    wh=(top.min(axis=2)>thr)&((top.max(axis=2)-top.min(axis=2))<40)
    wh=ndimage.binary_opening(wh,iterations=1)
    lab,n=ndimage.label(wh);best=None
    for k,sl in enumerate(ndimage.find_objects(lab),1):
        y0,y1,x0,x1=sl[0].start,sl[0].stop,sl[1].start,sl[1].stop
        if y0==0 or x0==0 or x1>=W: continue
        h,w=y1-y0,x1-x0
        if h<H*.06 or abs(h-w)>max(h,w)*.35: continue
        area=(lab[sl]==k).sum()
        if area<.5*h*w: continue
        if not best or area>best[0]: best=(area,(x0+x1)/2,(y0+y1)/2,min(h,w))
    return best
def put(im,cx,cy,d,color=(190,30,45),scale=.62):
    cx,cy,d=float(cx),float(cy),float(d);m=np.load(__import__('os').path.join(__import__('os').path.dirname(__file__),'logomask.npy'));mh,mw=m.shape
    s=d*scale/max(mh,mw);size=(max(1,int(mw*s)),max(1,int(mh*s)))
    M=Image.fromarray((m*255).astype('uint8')).resize(size,Image.LANCZOS)
    im=im.convert('RGBA');lay=Image.new('RGBA',im.size,(0,0,0,0))
    col=Image.new('RGBA',size,color+(255,));lay.paste(col,(int(cx-size[0]/2),int(cy-size[1]/2)),M)
    # soft shadow for 2.5D feel
    sh=Image.new('RGBA',im.size,(0,0,0,0));sc=Image.new('RGBA',size,(60,20,10,90))
    sh.paste(sc,(int(cx-size[0]/2+d*.015),int(cy-size[1]/2+d*.025)),M);sh=sh.filter(ImageFilter.GaussianBlur(d*.012))
    return Image.alpha_composite(Image.alpha_composite(im,sh),lay)
if __name__=='__main__':
    src,dst=sys.argv[1],sys.argv[2];im=Image.open(src)
    r=find_medallion(im);print(r)
    put(im,r[1],r[2],r[3]).convert('RGB').save(dst)
