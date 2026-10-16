"""Generate ORIGINAL, clearly stylized non-game environment illustrations.
No Apex screenshots, copied concept art, or external downloads are used.
72 deterministic synthwave scene paintings: 36 POIs x two camera variants.
"""
from pathlib import Path
from PIL import Image,ImageDraw,ImageFilter
import random,math,json,hashlib
import numpy as np
ROOT=Path(__file__).resolve().parents[1]
CAT=json.loads((ROOT/'assets/map-catalog.json').read_text())
OUT=ROOT/'assets/maps';OUT.mkdir(exist_ok=True)
W,H=960,540
PALETTES={
 'Kings Canyon':((19,17,43),(92,43,66),(230,124,70),(255,183,93)),
 'World’s Edge':((10,25,51),(53,40,84),(227,70,68),(94,214,255)),
 'Olympus':((24,39,86),(82,93,143),(251,176,171),(150,247,243)),
 'Storm Point':((4,36,57),(13,83,95),(108,159,127),(255,205,108)),
 'Broken Moon':((20,23,60),(66,50,114),(153,103,181),(246,156,236)),
 'E-District':((9,19,39),(46,23,74),(164,53,123),(80,232,250)),
}

def polygon(draw, pts, fill, outline=None,width=1):draw.polygon(pts,fill=fill);draw.line(pts+[pts[0]],fill=outline or fill,width=width,joint='curve')
def line(draw,pts,col,width=2):draw.line(pts,fill=col,width=width,joint='curve')
def gradient(top,bottom,h=H):
 y=np.linspace(0,1,h,dtype=np.float32)[:,None,None]
 a=np.array(top,dtype=np.float32)[None,None,:];b=np.array(bottom,dtype=np.float32)[None,None,:]
 x=(a*(1-y)+b*y).astype(np.uint8)
 return Image.fromarray(np.repeat(x,W,axis=1),'RGB')
def arcglow(image,x,y,r,col):
 layer=Image.new('RGBA',(W,H));d=ImageDraw.Draw(layer)
 d.ellipse((x-r,y-r,x+r,y+r),fill=(*col,90))
 layer=layer.filter(ImageFilter.GaussianBlur(max(9,r//2)))
 image.paste(Image.alpha_composite(image.convert('RGBA'),layer).convert('RGB')) if False else None
 return Image.alpha_composite(image.convert('RGBA'),layer).convert('RGB')
def tower(d,x,y,h,w,rng,light,main):
 polygon(d,[(x-w//2,y),(x-w//2+9,y-h),(x+w//2-8,y-h),(x+w//2,y)],main)
 d.rectangle((x-w//2+7,y-h+8,x+w//2-7,y-h+15),fill=light)
 for iy in range(y-h+25,y-8,17):
  for ix in range(x-w//2+11,x+w//2-5,14):
   if rng.random()>.26:d.rectangle((ix,iy,ix+5,iy+7),fill=light)
 line(d,[(x,y-h),(x,y-h-18)],light,2)
def mountains(d,rng,horizon,main,light):
 for depth in range(3):
  pts=[(-40,H)]
  for x in range(-40,W+90,50):
   peak=horizon+depth*34+rng.randint(-80,50)
   pts.append((x,peak))
  pts.extend([(W+40,H)])
  alpha=(max(15,main[0]-(2-depth)*10),max(15,main[1]-(2-depth)*7),max(20,main[2]-(2-depth)*6))
  polygon(d,pts,alpha)
  if depth==0:
   for x in range(0,W,105):line(d,[(x,horizon-5),(x+30,horizon-26)],(*light[:2],light[2]),1)
def interior(d,rng,main,light,style,view):
 vx=480+view*38;vy=235+view*4
 # room geometry with actual depth
 polygon(d,[(0,0),(W,0),(vx+270,vy-120),(vx-270,vy-120)],tuple(max(0,c-9) for c in main))
 polygon(d,[(0,0),(vx-270,vy-120),(vx-260,vy+135),(0,H)],tuple(max(0,c-17) for c in main))
 polygon(d,[(W,0),(vx+270,vy-120),(vx+260,vy+135),(W,H)],tuple(max(0,c-15) for c in main))
 polygon(d,[(0,H),(W,H),(vx+260,vy+135),(vx-260,vy+135)],tuple(max(0,c-28) for c in main))
 polygon(d,[(vx-260,vy-120),(vx+270,vy-120),(vx+260,vy+135),(vx-260,vy+135)],tuple(max(0,c+4) for c in main))
 for i in range(8):
  k=(i+1)/9; x=vx-260+k*520
  line(d,[(x,vy-120),(x,vy+135)],tuple(light),1 if i%2 else 2)
 for i in range(11):
  k=i/10;bottomx=vx-260+k*520
  line(d,[(vx,vy+135),(bottomx,H)],tuple(max(0,c//2) for c in light),2)
 for k in [.2,.36,.55,.8]:
  yy=vy+135+(H-vy-135)*k
  line(d,[(vx-(260+vx)*k,yy),(vx+(W-vx-260)*k+260,yy)],light,1)
 # lit ceiling strips
 for i in range(5):
  x=vx-230+i*105
  polygon(d,[(x,vy-105),(x+50,vy-105),(x+37,vy-98),(x-15,vy-98)],light)
 # scenery-dependent landmark
 if 'bunker' in style or 'corridor' in style or 'trials' in style:
  for x in [130,830]:
   polygon(d,[(x-50,145),(x+50,145),(x+70,450),(x-70,450)],(45,52,66),light,4)
   d.ellipse((x-19,225,x+19,262),fill=(110,240,235)); d.rectangle((x-10,228,x+10,247),fill=(11,18,39))
 elif 'club' in style or 'boardwalk' in style or 'galleria' in style:
  for i in range(8):
   x=120+i*97;y=220+(i%3)*19
   polygon(d,[(x,y),(x+65,y),(x+60,y+48),(x+5,y+48)],tuple(int(c*.5) for c in main),light,2)
  for x in range(80,920,115):d.ellipse((x,380,x+35,390),fill=light)
 elif 'villa' in style or 'estate' in style or 'lobby' in style:
  for x in [140,280,640,780]:
   polygon(d,[(x-50,170),(x+55,170),(x+45,345),(x-45,345)],(53,72,108),light,4)
   d.rectangle((x-25,210,x+22,315),fill=(108,181,197))
  d.ellipse((330,335,620,400),fill=(52,89,104),outline=light,width=4)
 else:
  for x in [132,780]:
   d.rectangle((x-30,200,x+75,345),fill=(39,62,74),outline=light,width=4)
   for i in range(6):line(d,[(x-20,221+i*17),(x+61,221+i*17)],light,2)
  d.ellipse((385,243,563,382),fill=(54,76,113),outline=light,width=8)
  for rad in [52,63,79]:d.arc((480-rad,314-rad,480+rad,314+rad),0,280,fill=light,width=4)
 # frame pillars
 for x in [80,220,745,880]:
  polygon(d,[(x-12,0),(x+12,0),(x+21,H),(x-15,H)],tuple(max(0,c-13) for c in main),outline=light,width=3)

def exterior(d,rng,main,light,style,mapname,view):
 hz=245+view*8
 mountains(d,rng,hz,(main[0]+30,main[1]+13,main[2]+24),light)
 polygon(d,[(0,H),(0,hz+110),(W,hz+85),(W,H)],tuple(max(0,c-5) for c in main))
 # ground runway / platform
 polygon(d,[(0,H),(W,H),(610,hz+74),(370,hz+74)],(33,37,60),light,2)
 for i in range(9):
  t=(i+1)/10;y=hz+80+(H-hz-80)*(t*t)
  line(d,[(360-350*t,y),(620+360*t,y)],tuple(int(c*.6) for c in light),2)
 for k in range(7):
  x=70+k*136
  line(d,[(x,H),(480+(x-480)*.12,hz+70)],tuple(int(c*.35) for c in light),2)
 # buildings depend on semantic location
 if any(s in style for s in ['gauntlet','cage','trials','countdown']):
  for k in range(3):
   cx=155+k*310+view*30;cy=285+k%2*15
   d.ellipse((cx-90,cy-54,cx+90,cy+96),outline=light,width=8)
   polygon(d,[(cx-97,cy+91),(cx+97,cy+91),(cx+120,cy+111),(cx-120,cy+111)],(40,40,61))
   for i in [-1,0,1]:line(d,[(cx+i*50,cy-15),(cx+i*50,cy+100)],light,4)
 elif any(s in style for s in ['bon','estate','oasis','plaza']):
  for i in range(6):
   x=65+i*167+view*16; tower(d,x,315,rng.randrange(120,230),rng.randrange(50,90),rng,light,(74,91,132))
  for x in (260,740):
   polygon(d,[(x-95,348),(x+95,348),(x+90,379),(x-88,379)],(151,135,176),light,3)
   d.ellipse((x-39,285,x+38,362),fill=(29,89,91),outline=light,width=2)
 elif any(s in style for s in ['city','neon','boardwalk','galleria']):
  for i in range(11):
   x=i*106+view*18
   tower(d,x,340,rng.randrange(145,255),rng.randrange(68,100),rng,light,(30,38,70))
  for x in range(90,900,170):line(d,[(x,300),(x+90,300)],(233,70,166),8)
 elif any(s in style for s in ['baro','antenna','signal','command']):
  for x in [210,490,775]:
   tower(d,x,345,180,85,rng,light,(42,67,73))
   line(d,[(x,152),(x,67)],light,3)
   d.ellipse((x-51,130,x+51,188),outline=light,width=6)
 elif any(s in style for s in ['lava','refinery','caustic','siphon','terraform','production','mill','climatizer']):
  for x in [180,360,620,810]:
   tower(d,x,348,rng.randrange(125,230),rng.randrange(68,95),rng,light,(62,57,84))
  for x in [112,390,730]:
   d.ellipse((x-43,230,x+43,295),outline=light,width=7)
  line(d,[(0,362),(960,362)],light,9)
 elif any(s in style for s in ['ship','maude','zip','rail']):
  polygon(d,[(190,292),(640,272),(778,350),(750,384),(235,369)],(55,64,98),light,6)
  polygon(d,[(390,287),(450,204),(610,209),(673,292)],(77,85,131),light,5)
  for x in (260,710):d.ellipse((x-45,357,x+46,409),outline=light,width=7)
  for x in range(400,650,45):d.rectangle((x,230,x+25,252),fill=light)
 else:
  for x in [250,460,680]:
   tower(d,x,337,rng.randrange(105,200),rng.randrange(65,125),rng,light,(43,50,77))
 # distinctive environment features
 if mapname=='Storm Point':
  for x in [85,870]:
   line(d,[(x,345),(x+15,155)],(89,87,56),9)
   for a in range(6):
    th=a*math.pi/3
    line(d,[(x+15,165),(x+15+92*math.cos(th),165+55*math.sin(th))],(45,127,112),8)
 if mapname=='Broken Moon':
  for x in [100,840]:
   d.arc((x-120,100,x+120,345),15,170,fill=light,width=6)
 if mapname=='World’s Edge':
  for x in range(0,W,125):
   polygon(d,[(x,525),(x+65,540),(x+135,540),(x+55,493)],(224,73,51),light,1)


def render(entry,angle):
 key=f"{entry['id']}:{angle}";seed=int(hashlib.sha256(key.encode()).hexdigest()[:12],16);rng=random.Random(seed)
 mapname=entry['map'];pal=PALETTES[mapname];top,bot,warm,neon=pal
 interior_mode=entry['kind']=='Interior';style=entry['id'].lower()
 img=gradient(top,bot)
 d=ImageDraw.Draw(img)
 # stars / bokeh
 for i in range(110):
  x=rng.randrange(W);y=rng.randrange(15,270);r=rng.choice([1,1,2,3])
  c=tuple(int(v*.65+120*.35) for v in neon)
  d.ellipse((x-r,y-r,x+r,y+r),fill=c)
 # moon and atmospheric motifs
 mx=680+angle*80; my=90
 d.ellipse((mx-60,my-60,mx+60,my+60),fill=tuple(min(255,int(c*.56+125)) for c in warm))
 for j in range(17):
  xx=mx+rng.randrange(-52,52); yy=my+rng.randrange(-52,52)
  d.ellipse((xx-3,yy-3,xx+5,yy+5),outline=warm,width=1)
 if interior_mode:interior(d,rng,top,neon,style,angle)
 else:exterior(d,rng,top,neon,style,mapname,angle)
 # neon textless HUD corners as part of illustration motif
 for y in [50,440]:
  line(d,[(40,y+32),(40,y),(128,y)],neon,4)
  line(d,[(832,y),(919,y),(919,y+32)],neon,4)
 # particle sparks/fog
 overlay=Image.new('RGBA',(W,H),(0,0,0,0));od=ImageDraw.Draw(overlay)
 for i in range(65):
  x=rng.randrange(W);y=rng.randrange(195,H);r=rng.randrange(2,22)
  od.ellipse((x-r,y-r,x+r,y+r),fill=(*neon,rng.randrange(9,32)))
 overlay=overlay.filter(ImageFilter.GaussianBlur(10))
 img=Image.alpha_composite(img.convert('RGBA'),overlay).convert('RGB')
 # transparent top+bottom subtle cinematic vignette
 a=np.array(img).astype(np.float32)
 xx=np.linspace(-1,1,W)[None,:];yy=np.linspace(-1,1,H)[:,None]
 vig=np.maximum(.63,1-.25*(xx**2)-.16*(yy**2))[:,:,None]
 a=np.uint8(np.clip(a*vig,0,255));img=Image.fromarray(a,'RGB')
 return img

manifest={}
for e in CAT:
 files=[]
 for angle in range(2):
  name=f"{e['id']}-concept-{angle+1}.webp";
  render(e,angle).save(OUT/name,'WEBP',quality=86,method=5)
  files.append(name)
 manifest[e['id']]=files
(ROOT/'src/concept_map_manifest.mjs').write_text('/** Original concept art only: not screenshots or exact in-game POIs. */\nexport const conceptMapManifest=Object.freeze('+json.dumps(manifest,ensure_ascii=False,indent=2)+');\n')
print(f'Created {len(CAT)*2} original illustrations for {len(CAT)} locations in {OUT}')
