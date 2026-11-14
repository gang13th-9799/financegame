import os,shutil
URL='file://'+os.path.abspath(os.path.join(os.path.dirname(__file__),'../../index.html'))
_c=shutil.which('google-chrome') or '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'
CHROME={'executable_path':_c} if os.path.exists(_c) else {}
from playwright.sync_api import sync_playwright
import time,sys
shots=[]
with sync_playwright() as p:
    b=p.chromium.launch(**CHROME)
    pg=b.new_page(viewport={'width':390,'height':844},device_scale_factor=1.5);errs=[]
    pg.on('pageerror',lambda e:errs.append(str(e)))
    pg.goto(URL);pg.evaluate("localStorage.clear()");pg.reload()
    pg.evaluate("newGame(30)");time.sleep(.8);pg.click('.mf button');time.sleep(.8)
    def snap(n,el=None):
        f=f'/tmp/u_{n}.png'
        (pg.locator(el).first.screenshot(path=f) if el else pg.screenshot(path=f));shots.append(f)
    # modals
    def modal(js,n,wait=1.4):
        pg.evaluate(f"void ({js})");time.sleep(wait);snap(n,'.modal')
        pg.evaluate("document.querySelectorAll('.mf button').length&&document.querySelector('.mf button:last-child').click()");time.sleep(.6)
        while pg.evaluate("!!MODAL"):
            pg.evaluate("document.querySelector('.mf button:last-child')&&document.querySelector('.mf button:last-child').click()");time.sleep(.4)
    modal("payday(S.players[0])","payday")
    modal("cellInfo('o3')","cell3")
    modal("cellInfo('i5')","cell12")
    # draw cards of each kind
    for k in ['life','learn','opp','net']:
        pg.evaluate("S.phase='card';S.picks=0");
        pg.evaluate(f"void pickPile('{k}')");time.sleep(1.8);snap('card_'+k,'.modal')
        for i in range(8):
            if not pg.evaluate("!!MODAL"):break
            pg.evaluate("document.querySelector('.mf button:last-child').click()");time.sleep(.5)
    # tabs
    tabs=pg.locator('.tabs button, .tab').all_inner_texts()
    print('tabs',tabs)
    for t in ['ผู้เล่น','ทักษะ','งบการเงิน','ธุรกิจ A','ตลาดหุ้นและสินค้า']:
        try:
            pg.click(f'text={t}',timeout=2000);time.sleep(.5);snap('tab_'+t,'.panel, #panel, .tabbody')
        except Exception as e: print('tab fail',t,e)
    print('errors',errs)
print('\n'.join(shots))
