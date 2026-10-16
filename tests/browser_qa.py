from pathlib import Path
from playwright.sync_api import sync_playwright
html=Path(__file__).resolve().parent.joinpath('browser_harness.html').read_text()
with sync_playwright() as p:
 browser=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox','--disable-dev-shm-usage'])
 for width,height in [(1600,900),(390,844)]:
  page=browser.new_page(viewport={'width':width,'height':height})
  errors=[];page.on('pageerror',lambda err:errors.append(str(err)))
  page.set_content(html,wait_until='domcontentloaded');page.wait_for_timeout(140)
  assert page.locator('.gtp2-mode-card').count()==6
  assert page.locator('img#gtp2-backdrop').evaluate('(el)=>el.naturalWidth')==1672
  assert page.locator('#mirage-gaze').count()==1
  hero=page.locator('.gtp2-hero').bounding_box()
  assert abs(hero['x'])<2 and abs(hero['width']-width)<2,(width,hero)
  assert page.locator('.gtp2-mode-card[data-mode="map"]').count()==1
  for mode in ('classic','pixel','quote','ability','emoji','map'):
   page.locator(f'.gtp2-mode-card[data-mode="{mode}"]').click()
   assert page.locator('.game').count()==1,mode
   assert not errors,(width,mode,errors)
   page.locator('.gtp2-brand').click()
   assert page.locator('.gtp2-mode-card').count()==6
  page.locator('[data-action="session"][data-session="unlimited"]').click()
  assert 'active' in page.locator('[data-action="session"][data-session="unlimited"]').get_attribute('class')
  # Gaze changes and respects FX OFF
  a=page.evaluate('document.querySelector("#mirage-gaze").toDataURL()')
  page.mouse.move(10,220);page.wait_for_timeout(120)
  b=page.evaluate('document.querySelector("#mirage-gaze").toDataURL()')
  page.mouse.move(width-5,220);page.wait_for_timeout(120)
  c=page.evaluate('document.querySelector("#mirage-gaze").toDataURL()')
  assert a!=b and b!=c,(a==b,b==c)
  page.evaluate('store.settings.motion=false;render({scroll:false})')
  before=page.evaluate('document.querySelector("#mirage-gaze").toDataURL()')
  page.mouse.move(50,90);page.wait_for_timeout(90)
  after=page.evaluate('document.querySelector("#mirage-gaze").toDataURL()')
  assert before==after
  assert not errors,errors
  print(f'PASS {width}x{height}: borderless hero, six modes, Free Play, gaze, FX OFF, zero JS errors')
  page.close()
 browser.close()
