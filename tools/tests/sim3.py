import os,shutil
URL='file://'+os.path.abspath(os.path.join(os.path.dirname(__file__),'../../index.html'))
_c=shutil.which('google-chrome') or '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
CHROME={'executable_path':_c} if os.path.exists(_c) else {}
from playwright.sync_api import sync_playwright
import time
with sync_playwright() as p:
    b=p.chromium.launch(**CHROME)
    pg=b.new_page(viewport={'width':412,'height':900})
    errs=[]
    pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto(URL)
    # make all bots, fast
    pg.evaluate("seats.forEach(s=>s.bot=true)")
    pg.evaluate("newGame(30)")
    pg.click('.mf button')
    for i in range(420):
        time.sleep(0.5)
        w=pg.evaluate("S.round>=10||null")
        if w is not None: break
        if pg.evaluate("MODAL"): pg.evaluate("MODAL_CANCEL&&MODAL_CANCEL()")
    print('round',pg.evaluate("S.round"),'lv1',pg.evaluate("S.players.filter(p=>p.badge1).map(p=>p.name+':'+p.badge1).join(',')"))
    print(pg.evaluate("S.players.map(p=>{const f=fin(p);return JSON.stringify(p.st)+' '+p.name+' '+JOBS[p.job].n+' '+f.passive+'/'+f.expenses+' cash '+p.cash+' loan '+p.loan+' net '+f.net+' deals '+f.deals+' board '+f.board+' act '+f.act}).join('\\n')"))
    print('errors',errs[:5])
    pg.screenshot(path='/tmp/shot.png',full_page=False)
    b.close()
