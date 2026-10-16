"""Verify each game launches a distinct local entry sound after user click."""
from pathlib import Path
from playwright.sync_api import sync_playwright
html=Path(__file__).with_name('browser_harness.html').read_text()
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox','--disable-dev-shm-usage'])
 page=b.new_page(viewport={'width':1440,'height':900})
 errors=[];page.on('pageerror',lambda e:errors.append(str(e)))
 page.set_content(html,wait_until='domcontentloaded')
 page.evaluate("window.__played=[]; HTMLMediaElement.prototype.play=function(){window.__played.push(this.src);return Promise.resolve()}")
 for mode in ['classic','pixel','quote','ability','emoji','map']:
  page.locator('.gtp2-mode-card[data-mode="'+mode+'"]').click()
  page.wait_for_timeout(75)
  assert any('enter-'+mode+'.wav' in str(src) for src in page.evaluate('window.__played')),mode
  page.locator('.gtp2-brand').click()
 assert len(set(src.rsplit('/',1)[-1] for src in page.evaluate('window.__played') if '/enter-' in str(src)))==6
 assert not errors,errors
 print('PASS all six original mode stingers fire on user click, no JS errors')
 b.close()
