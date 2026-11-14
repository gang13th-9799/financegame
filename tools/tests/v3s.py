import os,shutil
URL='file://'+os.path.abspath(os.path.join(os.path.dirname(__file__),'../../index.html'))
_c=shutil.which('google-chrome') or '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
CHROME={'executable_path':_c} if os.path.exists(_c) else {}
from playwright.sync_api import sync_playwright
import time
with sync_playwright() as p:
    b=p.chromium.launch(**CHROME);errs=[]
    pg=b.new_page(viewport={'width':390,'height':844},device_scale_factor=2);pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto(URL);pg.evaluate("localStorage.clear()");pg.reload()
    pg.evaluate("newGame(30)");time.sleep(.8);pg.click('.mf button');time.sleep(.5)
    for i,pos in enumerate([3,14,25,35]):
        pg.evaluate(f"S.players.forEach((q,j)=>{{q.ring='o';q.pos={pos}+(j%2)}});S.players[0].pos={pos};render()");time.sleep(1.6)
        pg.locator('#bwrap').screenshot(path=f'/tmp/v3s{i}.png')
    print(errs)
