"""Generate 28 ORIGINAL 3D-shaded sci-fi figurine cutouts on transparent backgrounds.
Not EA/Respawn character renders. Distinct costumes based on broad archetypes only.
These prevent the roster from going blank when external sources block hotlinks.
"""
from PIL import Image,ImageDraw,ImageFilter
from pathlib import Path
import random,hashlib,re,math,numpy as np
ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'assets/legends';OUT.mkdir(exist_ok=True)
text=(ROOT/'src/data.mjs').read_text();slugs=re.findall(r'"slug": "([^"\n]+)"',text)
W,H=420,570
roles={}
for mo in re.finditer(r'"name": "[^"]+".*?"role": "([^"]+)".*?"slug": "([^"]+)"',text,re.S):roles[mo.group(2)]=mo.group(1)
styles={'Assault':((201,88,105),(255,170,102)),'Skirmisher':((97,96,195),(118,230,255)),'Recon':((61,127,125),(158,245,227)),'Support':((177,112,95),(239,193,142)),'Controller':((106,91,160),(193,138,255))}
ROBOTS={'ash','pathfinder','revenant'}
MASKS={'bloodhound','caustic','octane','revenant','ash','pathfinder'}
HOODS={'wraith','ash','bloodhound','alter','catalyst','seer'}
VISORS={'valkyrie','ballistic','mirage','vantage','crypto','sparrow','axle'}
BACKPACK={'lifeline','newcastle','gibraltar','wattson','conduit','rampart'}

def shade(base,boost):return tuple(min(255,max(0,int(v*boost))) for v in base)
def grad_poly(canvas,pts,top,bottom):
 mask=Image.new('L',(W,H));ImageDraw.Draw(mask).polygon(pts,fill=255)
 bb=mask.getbbox()
 if bb is None:return
 ya=np.linspace(0,1,H,dtype=np.float32)[:,None,None]
 a=np.array(top,dtype=np.float32)[None,None,:];b=np.array(bottom,dtype=np.float32)[None,None,:]
 rg=(a*(1-ya)+b*ya).astype('uint8')
 r=np.repeat(rg,W,axis=1)
 im=Image.fromarray(r,'RGB').convert('RGBA');im.putalpha(mask)
 canvas.alpha_composite(im)
def ellipse(canvas,box,col,outline=None,w=1):
 ImageDraw.Draw(canvas).ellipse(box,fill=col,outline=outline,width=w)
def poly(canvas,pts,base,line=(9,14,34),w=3):
 ys=[p[1] for p in pts];ymin=min(ys);ymax=max(ys)
 grad_poly(canvas,pts,shade(base,1.24),shade(base,.57))
 ImageDraw.Draw(canvas).line(pts+[pts[0]],fill=line,width=w,joint='curve')
def highlights(canvas,pts,col,w=3):ImageDraw.Draw(canvas).line(pts,fill=(*col,185),width=w,joint='curve')

def figure(slug):
 seed=int(hashlib.md5(slug.encode()).hexdigest()[:8],16);rng=random.Random(seed)
 role=roles.get(slug,'Recon');base,accent=styles.get(role,styles['Recon'])
 # alternate the bases by character while keeping palette coherent
 hue=rng.randint(-24,25);base=tuple(min(220,max(44,c+hue)) for c in base)
 armor=(max(35,base[0]-30),max(28,base[1]-17),max(42,base[2]-9))
 light=tuple(min(255,c+22) for c in accent)
 im=Image.new('RGBA',(W,H),(0,0,0,0))
 # stylized double-soft shadow along silhouette, alpha only
 shade_layer=Image.new('RGBA',(W,H));sd=ImageDraw.Draw(shade_layer)
 sd.ellipse((98,430,326,557),fill=(16,5,39,54))
 shade_layer=shade_layer.filter(ImageFilter.GaussianBlur(20));im.alpha_composite(shade_layer)
 # slender / wide body variation
 width=112+({'gibraltar':39,'newcastle':28,'caustic':20,'wattson':-15,'wraith':-21,'octane':-19,'ash':-15}.get(slug,0))
 center=210+rng.randint(-5,5);shoulder=228+10*bool(slug in BACKPACK)
 # attachment backpack and antenna
 if slug in BACKPACK:
  poly(im,[(center-128,218),(center-169,246),(center-151,405),(center-104,373)],shade(base,.55))
  poly(im,[(center+111,218),(center+165,250),(center+151,400),(center+104,373)],shade(base,.57))
  for xx in [center-148,center+142]:
   ellipse(im,(xx-20,277,xx+20,327),(31,45,70,255),outline=(*accent,255),w=4)
 # cloak silhouette
 if slug in HOODS:
  poly(im,[(center-98,204),(center+105,205),(center+139,503),(center+65,536),(center,485),(center-69,538),(center-155,480)],shade(base,.42),w=2)
 # legs; stylized greaves, mechanical joints
 for side in [-1,1]:
  x=center+side*(width*.43)
  thigh=[(x-32,368),(x+32,367),(x+41,454),(x-31,453)]
  poly(im,thigh,armor)
  ellipse(im,(x-21,430,x+23,477),(33,41,69,255),outline=(*light,255),w=3)
  poly(im,[(x-28,461),(x+26,460),(x+20,544),(x-24,543)],shade(base,.75))
  poly(im,[(x-32,536),(x+24,535),(x+44,558),(x-42,560)],(33,39,64))
  highlights(im,[(x-23,478),(x-21,527)],accent,4)
 # body shadow side slabs
 poly(im,[(center-width,232),(center+width,226),(center+width*.86,380),(center+width*.6,424),(center-width*.66,426),(center-width*.98,373)],base)
 # chest breastplate bevel
 poly(im,[(center-width*.66,257),(center+width*.64,257),(center+width*.44,352),(center,380),(center-width*.48,350)],armor,line=(20,17,42),w=4)
 highlights(im,[(center-width*.57,271),(center,289),(center+width*.57,269)],light,5)
 # colored straps / chest console
 poly(im,[(center-47,306),(center+47,307),(center+35,357),(center-33,358)],shade(accent,.58),w=2)
 ellipse(im,(center-17,315,center+17,349),(10,18,45,255),outline=(*light,255),w=5)
 for k in range(4):
  xx=center-25+k*17;ImageDraw.Draw(im).rectangle((xx,364,xx+9,372),fill=(*light,220))
 # waist belt
 poly(im,[(center-83,382),(center+80,382),(center+70,419),(center-72,418)],(34,38,66))
 ellipse(im,(center-17,384,center+16,414),(69,94,122,255),outline=(*accent,255),w=3)
 # arms / pauldrons
 for side in [-1,1]:
  x=center+side*(width+7)
  # pose difference
  handx=x+side*(rng.randint(-6,22));handy=421+rng.randint(-17,7)
  poly(im,[(x-31,244),(x+30,236),(handx+25,388),(handx-24,389)],shade(base,.66))
  ellipse(im,(x-40,224,x+39,290),(48,61,90,255),outline=(*accent,255),w=5)
  poly(im,[(handx-24,368),(handx+25,369),(handx+23,handy),(handx-19,handy)],shade(base,.82))
  ellipse(im,(handx-23,handy-11,handx+24,handy+37),(46,54,77,255),outline=(*accent,255),w=3)
  highlights(im,[(x-22,289),(handx-19,352)],light,3)
 # neck
 poly(im,[(center-29,203),(center+27,202),(center+25,250),(center-27,252)],(52,60,82))
 # back hood and head shape
 skin=(154+rng.randint(-23,24),119+rng.randint(-26,34),100+rng.randint(-24,25))
 if slug in ROBOTS:skin=(74,89,109)
 headx=center+rng.randint(-4,4);heady=153+rng.randint(-5,5)
 if slug in HOODS:
  ellipse(im,(headx-66,heady-90,headx+67,heady+77),(25,29,59,255),outline=(*accent,255),w=6)
 # ears/head shading
 ellipse(im,(headx-53,heady-70,headx+52,heady+66),(*shade(skin,.72),255),outline=(23,29,48,255),w=4)
 ellipse(im,(headx-42,heady-56,headx+39,heady+54),(*shade(skin,1.24),255))
 if slug in MASKS:
  poly(im,[(headx-43,heady-4),(headx+42,heady-2),(headx+34,heady+52),(headx,heady+64),(headx-35,heady+46)],(30,38,58))
  for x in [headx-24,headx+24]:ellipse(im,(x-13,heady+12,x+13,heady+35),(33,54,68,255),outline=(*accent,255),w=3)
 else:
  # nose + lower face
  poly(im,[(headx-7,heady-6),(headx+7,heady-4),(headx+2,heady+23),(headx-7,heady+24)],shade(skin,.73),w=2)
  highlights(im,[(headx-15,heady+37),(headx+18,heady+36)],(81,40,63),2)
 # helmet / hair / visor
 if slug in VISORS:
  poly(im,[(headx-53,heady-39),(headx+52,heady-40),(headx+43,heady-3),(headx-45,heady-4)],(26,27,55))
  poly(im,[(headx-43,heady-28),(headx+42,heady-29),(headx+33,heady-10),(headx-37,heady-12)],accent,w=2)
 else:
  poly(im,[(headx-50,heady-31),(headx-45,heady-63),(headx-14,heady-78),(headx+42,heady-72),(headx+52,heady-31),(headx+11,heady-44)],armor,w=2)
 # eyes luminous
 ey= heady-9
 for dx in [-23,23]:
  ellipse(im,(headx+dx-13,ey-5,headx+dx+12,ey+10),(14,26,49,255),outline=(*accent,255),w=2)
  ellipse(im,(headx+dx-4,ey-2,headx+dx+4,ey+6),(*light,255))
 # character-specific ornaments
 d=ImageDraw.Draw(im)
 if slug in ['bloodhound','vantage','sparrow']:
  poly(im,[(headx-70,heady-65),(headx-35,heady-85),(headx-57,heady-102)],shade(accent,.8))
  poly(im,[(headx+50,heady-70),(headx+80,heady-85),(headx+60,heady-30)],shade(accent,.9))
 if slug in ['wattson','lifeline','conduit']:
  for x in [center-144,center+150]:
   line=[(x,230),(x,169),(x+13,148)]
   d.line(line,fill=(*accent,255),width=5)
   ellipse(im,(x+3,141,x+22,159),(*light,255))
 if slug in ['fuse','mad-maggie','ballistic']:
  d.line([(headx-32,heady+16),(headx+35,heady+17)],fill=(*accent,255),width=6)
 if slug=='pathfinder':
  ellipse(im,(center-35,300,center+35,369),(27,50,64,255),outline=(*accent,255),w=7)
  ellipse(im,(center-20,316,center+20,356),(96,221,222,255))
 if slug in ['wraith','alter','seer']:
  for x in [center-105,center+104]:
   d.arc((x-18,175,x+24,251),40,275,fill=(*accent,255),width=6)
 if slug in ['octane','axle']:
  for side in [-1,1]:
   x=center+side*50
   d.line((x,477,x+side*29,552),fill=(*light,255),width=8)
 # soft outlined luminescent silhouette with transparency preserved
 # stage color alpha remains 0 outside the figurine
 im.save(OUT/f'{slug}.webp','WEBP',quality=90,method=5)

for slug in slugs:figure(slug)
print(f'Generated {len(slugs)} transparent original role-inspired sci-fi figurines.')
