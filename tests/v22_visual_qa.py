"""Browser QA for GTP2 2.2 with real routed local imagery and responsive screenshots."""
from pathlib import Path
from playwright.sync_api import sync_playwright
root=Path(__file__).resolve().parents[1]
html=(root/'tests/browser_harness.html').read_text()
html=html.replace('<head>','<head><base href="https://gtp2.test/">',1)
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox','--disable-dev-shm-usage'])
    for w,h in [(1440,900),(390,844)]:
        page=b.new_page(viewport={'width':w,'height':h},device_scale_factor=1)
        errors=[];page.on('pageerror', lambda error:errors.append(str(error)))
        def assets(route):
            url=route.request.url
            rel=url.split('https://gtp2.test/')[-1].split('?')[0]
            if rel.startswith('assets/') and (root/rel).is_file():
                content=(root/rel).read_bytes()
                suffix=Path(rel).suffix.lower()
                ty={'.webp':'image/webp','.png':'image/png','.jpg':'image/jpeg','.svg':'image/svg+xml','.wav':'audio/wav'}.get(suffix,'application/octet-stream')
                route.fulfill(status=200,body=content,content_type=ty)
            else:route.abort()
        page.route('**/*',assets)
        page.set_content(html,wait_until='domcontentloaded')
        page.screenshot(path=str(root/f'tests/v22_home_{w}.png'),full_page=True)
        page.locator('.gtp2-mode-card[data-mode="map"]').click()
        page.wait_for_function("document.querySelector('.map-photo')?.classList.contains('has-map-art')",timeout=12000)
        assert page.locator('.map-photo.has-map-art').count()==1
        assert page.locator('.map-credit').inner_text().startswith('ORIGINAL STYLIZED RECONSTRUCTIONS')
        assert page.locator('img[data-map-photo]').evaluate('(e)=>e.naturalWidth')==960
        page.screenshot(path=str(root/f'tests/v22_map_{w}.png'),full_page=True)
        page.locator('.gtp2-brand').click()
        page.locator('.gtp2-mode-card[data-mode="quote"]').click()
        assert page.locator('button[data-action="play-voice"]').count()==0
        assert page.locator('.gtp2-quote-rework blockquote').count()==1
        page.screenshot(path=str(root/f'tests/v22_quote_{w}.png'),full_page=True)
        page.locator('button[data-action="picker"]').click()
        assert page.locator('.gtp2-picker').count()==1
        assert page.locator('.gtp2-picker .gtp2-legend-card').count()==28
        page.wait_for_function("Array.from(document.querySelectorAll('.gtp2-picker .portrait-holder img')).every(im=>im.naturalWidth===420)", timeout=12000)
        assert page.locator('.gtp2-picker .portrait-unavailable').count()==0
        page.screenshot(path=str(root/f'tests/v22_picker_{w}.png'),full_page=True)
        assert not errors,(w,errors)
        print(f'PASS {w}x{h}: map artwork loaded (960 px), quote text-only, 28 equal portrait cards, no JS errors')
        page.close()
    b.close()
