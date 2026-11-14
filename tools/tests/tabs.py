import os,shutil
URL='file://'+os.path.abspath(os.path.join(os.path.dirname(__file__),'../../index.html'))
_c=shutil.which('google-chrome') or '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
CHROME={'executable_path':_c} if os.path.exists(_c) else {}
from playwright.sync_api import sync_playwright
import time
with sync_playwright() as p:
    b=p.chromium.launch(**CHROME)
    pg=b.new_page(viewport={'width':390,'height':844},device_scale_factor=1.5);errs=[]
    pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto(URL);pg.evaluate("localStorage.clear()");pg.reload()
    pg.evaluate("newGame(30)");time.sleep(.8);pg.click('.mf button');time.sleep(.8)
    # give player some assets for richer panels
    pg.evaluate("""(()=>{const q=S.players[0];q.cash+=500000;q.loan=30000;q.stocks.TTEC={q:2000,c:38000};q.stocks.GOLD={q:2,c:41000};})()""")
    for t in ['pl','sk','fin','net','mkt','log']:
        pg.click('#t-'+t);time.sleep(.5);pg.locator('#panel').screenshot(path=f'/tmp/tab_{t}.png')
    print(errs)
