import os,shutil
URL='file://'+os.path.abspath(os.path.join(os.path.dirname(__file__),'../../index.html'))
_c=shutil.which('google-chrome') or '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
CHROME={'executable_path':_c} if os.path.exists(_c) else {}
from playwright.sync_api import sync_playwright
import time
with sync_playwright() as p:
    b=p.chromium.launch(**CHROME);errs=[]
    for w,h,n in [(390,844,'p'),(1106,835,'f')]:
        pg=b.new_page(viewport={'width':w,'height':h},device_scale_factor=1.5);pg.on('pageerror',lambda e:errs.append(str(e)))
        pg.goto(URL);pg.evaluate("localStorage.clear()");pg.reload()
        pg.evaluate("newGame(30)");time.sleep(.8);pg.click('.mf button');time.sleep(1.6)
        pg.locator('#bwrap').screenshot(path=f'/tmp/ct_{n}0.png')
        for i,pos in enumerate([14,25,33]):
            pg.evaluate(f"S.players[0].pos={pos};render()");time.sleep(1.5)
            pg.locator('#bwrap').screenshot(path=f'/tmp/ct_{n}{i+1}.png')
            r=pg.evaluate("""(()=>{const c=document.querySelector('.cell[data-k="o'+S.players[0].pos+'"]').getBoundingClientRect(),w=document.querySelector('#bwrap').getBoundingClientRect();return [Math.round((c.left+c.width/2-w.left)/w.width*100),Math.round((c.top+c.height/2-w.top)/w.height*100)]})()""")
            print(n,pos,r)
    print(errs)
