import subprocess,os,pathlib,urllib.parse
from playwright.sync_api import sync_playwright
import imageio_ffmpeg
ff=imageio_ffmpeg.get_ffmpeg_exe()
people=[("aeon","Aeon Bonjé","left"),("rune","Rune Vanhoucke","center"),("arno","Arno Cuyvers","right")]
root=pathlib.Path('/home/user/SDWorx_brand/popups');out=root/'out';out.mkdir(exist_ok=True)
with sync_playwright() as p:
    b=p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1194/chrome-linux/chrome') if os.path.exists('/opt/pw-browsers/chromium-1194/chrome-linux/chrome') else p.chromium.launch()
    pg=b.new_page(viewport={'width':1920,'height':1080})
    for k,n,pos in people:
        q=urllib.parse.urlencode({'n':n,'pos':pos})
        pg.goto(f'file://{root}/pop.html?{q}');pg.evaluate('document.fonts.ready')
        pg.wait_for_timeout(300)
        d=root/'frames'/k;d.mkdir(parents=True,exist_ok=True)
        for f in range(165):
            pg.evaluate(f'document.getAnimations().forEach(a=>{{a.pause();a.currentTime={f}/30*1000}})')
            pg.screenshot(path=str(d/f'{f:04d}.png'),omit_background=True)
        pg.goto(f'file://{root}/pop.html?{q}&still=1');pg.evaluate('document.fonts.ready');pg.wait_for_timeout(300)
        pg.screenshot(path=str(out/f'{k}-still.png'),omit_background=True)
        r=lambda a:subprocess.run([ff,'-y','-loglevel','error']+a,check=True)
        i=str(d/'%04d.png')
        r(['-framerate','30','-i',i,'-c:v','prores_ks','-profile:v','4444','-pix_fmt','yuva444p10le',str(out/f'{k}-alpha.mov')])
        r(['-framerate','30','-i',i,'-c:v','libvpx-vp9','-pix_fmt','yuva420p','-b:v','6M','-auto-alt-ref','0',str(out/f'{k}-alpha.webm')])
        r(['-f','lavfi','-i','color=c=0x00FF00:s=1920x1080:r=30','-framerate','30','-i',i,'-filter_complex','[0][1]overlay=shortest=1,format=yuv420p','-c:v','libx264','-crf','12',str(out/f'{k}-greenscreen.mp4')])
    b.close()
