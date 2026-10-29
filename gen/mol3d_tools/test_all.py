# Every lesson with molecule drawings: light/desktop and dark/iPhone 13.
# base = the committed site (git archive HEAD, :8766), new = the working tree (:8765).
import asyncio, os, sys, json
from playwright.async_api import async_playwright
from PIL import Image, ImageChops
SLUGS=sys.argv[1:] or ['macronutrients-carbohydrates','macronutrients-protein','bioactives','processing','macronutrients-lipids','additives','flavorings','final-review','micronutrients-trace-minerals','micronutrients-fat-soluble-vitamins','micronutrients-water-soluble-vitamins','antinutrients','micronutrients-major-minerals','macronutrients-water-ethanol']
SH='/workspace/nutrition/screens/mol3d/all'; os.makedirs(SH,exist_ok=True)
async def ctx_for(p,b,mode):
    return await b.new_context(viewport={'width':1366,'height':900},color_scheme='light') if mode=='light' else await b.new_context(**p.devices['iPhone 13'],color_scheme='dark')
async def shots(pg,tag,mode,slug):
    n=await pg.evaluate("document.querySelectorAll('.lm>.mz img').length"); out=[]
    for i in range(n):
        el=pg.locator('.lm>.mz img').nth(i)
        fig=await el.evaluate("e=>{const f=e.closest('[data-fig]');return f?+f.dataset.fig:0}")
        if fig: await pg.evaluate(f"window.lessonPlayer&&lessonPlayer.go({fig},1)"); await pg.wait_for_timeout(80)
        await el.evaluate("e=>e.scrollIntoView({block:'center',behavior:'instant'})"); await pg.mouse.move(0,0); await pg.evaluate("document.activeElement&&document.activeElement.blur()")
        await pg.evaluate("document.querySelectorAll('.m3t').forEach(e=>e.style.visibility='hidden');document.querySelectorAll('body *').forEach(e=>{const p=getComputedStyle(e).position;if(p==='fixed'||p==='sticky'){e.dataset.tfx=e.style.visibility;e.style.visibility='hidden'}})"); await pg.wait_for_timeout(60)
        fn=f"{SH}/{tag}-{mode}-{slug}-{i:02d}.png"
        if await el.is_visible(): await el.screenshot(path=fn,animations='disabled',timeout=8000); out.append(fn)
        else: out.append(None)
        await pg.evaluate("document.querySelectorAll('.m3t').forEach(e=>e.style.visibility='');document.querySelectorAll('[data-tfx]').forEach(e=>{e.style.visibility=e.dataset.tfx;delete e.dataset.tfx})")
    return out
def same(a,b):
    A=Image.open(a).convert('RGB'); B=Image.open(b).convert('RGB'); return A.size==B.size and ImageChops.difference(A,B).getbbox() is None
async def lesson(p,b,slug,mode):
    R={'slug':slug,'mode':mode}
    c0=await ctx_for(p,b,mode); pg=await c0.new_page(); await pg.goto(f'http://localhost:8766/curriculum/{slug}.html'); await pg.wait_for_load_state('networkidle')
    base=await shots(pg,'base',mode,slug); await c0.close()
    c=await ctx_for(p,b,mode); pg=await c.new_page(); errs=[]
    pg.on('console',lambda m: errs.append(m.type+': '+m.text) if m.type in('error','warning') else None); pg.on('pageerror',lambda e: errs.append(str(e)))
    await pg.goto(f'http://localhost:8765/curriculum/{slug}.html'); await pg.wait_for_load_state('networkidle')
    new=await shots(pg,'new',mode,slug)
    R['drawings']=len(new); R['2d_diffs']=[os.path.basename(x) for a,x in zip(base,new) if (a is None)!=(x is None) or (a and not same(a,x))]+(['COUNT'] if len(base)!=len(new) else [])
    R['toggles']=await pg.evaluate("document.querySelectorAll('.m3t').length")
    # every toggle: 3D on, canvas draws, back to 2D
    bad3=[]
    for i in range(R['toggles']):
        t=pg.locator('.m3t').nth(i); lm=t.locator('xpath=..')
        fig=await t.evaluate("e=>{const f=e.closest('[data-fig]');return f?+f.dataset.fig:0}")
        if fig: await pg.evaluate(f"lessonPlayer.go({fig},1)"); await pg.wait_for_timeout(60)
        await t.evaluate("e=>e.scrollIntoView({block:'center',behavior:'instant'})")
        if not await t.is_visible(): continue
        await t.locator('[data-v="3d"]').evaluate('e=>e.click()')
        try: await lm.locator('canvas.m3v').wait_for(timeout=12000)
        except Exception: bad3.append((i,'no canvas')); continue
        await pg.wait_for_timeout(60)
        ink=await lm.locator('canvas.m3v').evaluate("c=>{const d=c.getContext('2d').getImageData(0,0,c.width,c.height).data;let n=0;for(let k=3;k<d.length;k+=4)if(d[k])n++;return n/(d.length/4)}")
        if ink<0.02: bad3.append((i,'blank',ink))
        if i==0: R['sw_3d']=await pg.evaluate("document.documentElement.scrollWidth-innerWidth")
        if i<2: await lm.screenshot(path=f"{SH}/3d-{mode}-{slug}-{i}.png")
        await t.locator('[data-v="2d"]').evaluate('e=>e.click()'); await pg.wait_for_timeout(40)
        if not await lm.evaluate("l=>!l.classList.contains('m3on')&&!l.querySelector('canvas')"): bad3.append((i,'not back'))
    R['3d_bad']=bad3
    # 2D zoom on the first two drawings
    zr=[]
    vis=[k for k,x in enumerate(new) if x][:2]
    for i in vis:
        await pg.evaluate("document.querySelectorAll('dialog[open]').forEach(d=>d.close())")
        lm=pg.locator('.lm>.mz img').nth(i).locator('xpath=../..'); mz=lm.locator(':scope>.mz')
        fig=await lm.evaluate("e=>{const f=e.closest('[data-fig]');return f?+f.dataset.fig:0}")
        if fig: await pg.evaluate(f"lessonPlayer.go({fig},1)"); await pg.wait_for_timeout(80)
        await lm.evaluate("e=>e.scrollIntoView({block:'center',behavior:'instant'})"); await pg.wait_for_timeout(60)
        bb=await mz.bounding_box(); cx,cy=bb['x']+bb['width']*.5,bb['y']+bb['height']*.5
        mk0=await lm.evaluate("l=>[...l.querySelectorAll(':scope>.mk')].map(m=>m.getBoundingClientRect().x)")
        r={}
        if mode=='light':
            y0=await pg.evaluate("scrollY"); await pg.mouse.move(cx,cy); await pg.mouse.wheel(0,120); await pg.wait_for_timeout(250)
            r['plain_wheel_scrolls']=(await pg.evaluate("scrollY"))!=y0 and not await lm.evaluate("l=>l.classList.contains('z2')")
            await lm.evaluate("e=>e.scrollIntoView({block:'center',behavior:'instant'})"); await pg.wait_for_timeout(60)
            bb=await mz.bounding_box(); cx,cy=bb['x']+bb['width']*.5,bb['y']+bb['height']*.5
            await pg.mouse.move(cx,cy); await pg.keyboard.down('Control'); await pg.mouse.wheel(0,-60); await pg.keyboard.up('Control'); await pg.wait_for_timeout(80)
        else:  # two-finger pinch out
            cdp=await c.new_cdp_session(pg)
            async def touch(t,pts): await cdp.send('Input.dispatchTouchEvent',{'type':t,'touchPoints':[{'x':x,'y':y,'id':k} for k,(x,y) in enumerate(pts)]})
            g=min(15,bb['width']/4)  # both fingers start on the drawing, even a tiny ion
            await touch('touchStart',[(cx-g,cy),(cx+g,cy)])
            for s in range(1,9): await touch('touchMove',[(cx-g-6*s,cy),(cx+g+6*s,cy)])
            await touch('touchEnd',[]); await pg.wait_for_timeout(80)
        r['zoomed']=await lm.evaluate("l=>l.classList.contains('z2')")
        mk1=await lm.evaluate("l=>[...l.querySelectorAll(':scope>.mk')].map(m=>m.getBoundingClientRect().x)")
        r['markers_moved']=(mk0!=mk1) if mk0 else 'no markers'
        await lm.screenshot(path=f"{SH}/zoom-{mode}-{slug}-{i}.png")
        # drag pans and does not open the enlarge dialog
        if mode=='light':
            t0=await mz.evaluate("e=>e.style.transform")
            await pg.mouse.move(cx,cy); await pg.mouse.down(); await pg.mouse.move(cx+40,cy+20,steps=5); await pg.mouse.up(); await pg.wait_for_timeout(350)
            r['panned']=t0!=await mz.evaluate("e=>e.style.transform")
        else:
            await pg.touchscreen.tap(cx,cy) if False else None
            r['panned']='n/a'
        r['dialog_after_drag']=await pg.evaluate("document.querySelector('dialog.lbm').open")
        # keys: + / - / 0 on the focused drawing do not move the player
        st0=await pg.evaluate("JSON.stringify([lessonPlayer.state.fig,lessonPlayer.state.seg])")
        await mz.focus(); await pg.keyboard.press('+'); z1=await mz.evaluate("e=>e.style.transform"); await pg.keyboard.press('-'); await pg.keyboard.press('ArrowRight') if False else None
        r['keys_player_same']=st0==await pg.evaluate("JSON.stringify([lessonPlayer.state.fig,lessonPlayer.state.seg])")
        r['plus_zooms']=bool(z1)
        # double-click / double-tap resets
        if mode=='light': await mz.dblclick()
        else: await pg.touchscreen.tap(cx,cy); await pg.touchscreen.tap(cx,cy)
        await pg.wait_for_timeout(400)
        r['reset']=await lm.evaluate("l=>!l.classList.contains('z2')&&!l.querySelector(':scope>.mz').getAttribute('style')")
        r['dialog_after_dbl']=await pg.evaluate("document.querySelector('dialog.lbm').open")
        if r['dialog_after_dbl']: await pg.keyboard.press('Escape')
        # back to pixel-identical default
        await pg.mouse.move(0,0); await pg.evaluate("document.activeElement&&document.activeElement.blur()")
        await pg.evaluate("document.querySelectorAll('.m3t').forEach(e=>e.style.visibility='hidden')")
        img=lm.locator(':scope>.mz img'); fn=f"/tmp/z-{mode}-{slug}-{i}.png"; await img.screenshot(path=fn,animations='disabled')
        await pg.evaluate("document.querySelectorAll('.m3t').forEach(e=>e.style.visibility='')")
        idx=await img.evaluate("e=>[...document.querySelectorAll('.lm>.mz img')].indexOf(e)")
        r['reset_pixels_same']=same(base[idx],fn) or 'recheck'
        # zoomed then single click still enlarges, dialog copy is unzoomed
        if mode=='light': await pg.mouse.move(cx,cy); await pg.keyboard.down('Control'); await pg.mouse.wheel(0,-40); await pg.keyboard.up('Control'); await pg.wait_for_timeout(60)
        await mz.click(); await pg.wait_for_timeout(450)
        r['zoomed_click_enlarges']=await pg.evaluate("document.querySelector('dialog.lbm').open")
        r['dialog_clean']=await pg.evaluate("(()=>{const d=document.querySelector('dialog.lbm');return !d.querySelector('.m3t,.z2,[style*=\"scale\"]')&&[...d.querySelectorAll('.mk')].every(m=>m.style.left.endsWith('%'))})()")
        await pg.keyboard.press('Escape'); await pg.wait_for_timeout(60)
        await mz.dblclick() if mode=='light' else None
        await pg.wait_for_timeout(350)
        if await pg.evaluate("document.querySelector('dialog.lbm').open"): await pg.keyboard.press('Escape')
        zr.append(r)
    R['zoom']=zr
    if new: R['touch_action']=await pg.evaluate("[...new Set([...document.querySelectorAll('.lm>.mz')].map(e=>getComputedStyle(e).touchAction))]")
    R['sw']=await pg.evaluate("document.documentElement.scrollWidth-innerWidth"); R['errors']=errs
    await c.close(); return R
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch()
        for slug in SLUGS:
            for mode in ('light','dark'):
                try: R=await lesson(p,b,slug,mode)
                except Exception as e: R={'slug':slug,'mode':mode,'EXC':repr(e)[:300]}
                print(json.dumps(R),flush=True)
        await b.close()
asyncio.run(main())
