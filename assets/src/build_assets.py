#!/usr/bin/env python3
"""Build the self-contained, GitHub-compatible visual assets for Mateos's profile.

No dependencies: python3 assets/src/build_assets.py
SVG CSS animations are decorative; every image has a full static fallback.
"""
from pathlib import Path
from html import escape
from math import cos, sin, pi
import random

ROOT = Path(__file__).resolve().parents[2]
ASSETS = ROOT / 'assets'
(ASSETS / 'sections').mkdir(parents=True, exist_ok=True)
(ASSETS / 'projects').mkdir(parents=True, exist_ok=True)

BG='#070D1D'; BASE='#0C1427'; PANEL='#101A30'; BORD='#253757'
WHITE='#EDF6FF'; MUTED='#9DB1CB'; FAINT='#577092'
CYAN='#52E5F9'; VIOLET='#A18CFF'; MINT='#67E9C7'; GOLD='#FFD08B'
MONO="'JetBrains Mono',Consolas,monospace"
SANS="'Segoe UI',Inter,Arial,sans-serif"

CSS=f'''<style>
  .text {{ font-family:{SANS}; }} .mono {{ font-family:{MONO}; }}
  .shimmer {{ animation: shimmer 6s ease-in-out infinite; }}
  .blink {{ animation: blink 1.45s steps(2,end) infinite; }}
  .pulse {{ transform-box:fill-box; transform-origin:center; animation:pulse 3.2s ease-in-out infinite; }}
  .drift {{ animation:drift 7s ease-in-out infinite; }}
  .dash {{ stroke-dasharray:6 11; animation:dash 14s linear infinite; }}
  @keyframes shimmer {{ 0%,100% {{opacity:.45}} 50% {{opacity:1}} }}
  @keyframes blink {{ 0%,48% {{opacity:1}} 49%,100% {{opacity:.1}} }}
  @keyframes pulse {{ 0%,100% {{opacity:.55;transform:scale(.92)}} 50% {{opacity:1;transform:scale(1.16)}} }}
  @keyframes drift {{ 0%,100% {{transform:translateY(0)}} 50% {{transform:translateY(-8px)}} }}
  @keyframes dash {{ from {{stroke-dashoffset:0}} to {{stroke-dashoffset:-170}} }}
  @media (prefers-reduced-motion:reduce) {{ .shimmer,.blink,.pulse,.drift,.dash {{animation:none}} }}
</style>'''

def svg_start(w,h,round=24,background=True):
    v=f'''<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img">
<defs>
  <linearGradient id="nebula" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#101C36"/><stop offset=".55" stop-color="{BG}"/><stop offset="1" stop-color="#100F2B"/></linearGradient>
  <linearGradient id="energy" x1="0" y1="0" x2="1" y2="0"><stop stop-color="{CYAN}"/><stop offset=".52" stop-color="{MINT}"/><stop offset="1" stop-color="{VIOLET}"/></linearGradient>
  <radialGradient id="halo"><stop stop-color="#293E72" stop-opacity=".62"/><stop offset=".65" stop-color="#181E4B" stop-opacity=".2"/><stop offset="1" stop-color="#07101E" stop-opacity="0"/></radialGradient>
  <pattern id="grid" width="36" height="36" patternUnits="userSpaceOnUse"><path d="M36 0H0V36" stroke="#668ABF" stroke-width=".65" opacity=".13" fill="none"/></pattern>
  <filter id="glow"><feGaussianBlur stdDeviation="4"/></filter>
</defs>{CSS}'''
    if background:
        v+=f'<rect width="{w}" height="{h}" rx="{round}" fill="url(#nebula)"/><rect x="1" y="1" width="{w-2}" height="{h-2}" rx="{round}" fill="none" stroke="{BORD}" stroke-width="2"/>'
    return v

def write(name,content):
    f=ASSETS/name; f.parent.mkdir(exist_ok=True,parents=True)
    f.write_text(content+'</svg>',encoding='utf-8')
    print('built',f.relative_to(ROOT))

def t(x,y,s,size=18,color=WHITE,weight=400,mono=False,extra=''):
    return f'<text x="{x}" y="{y}" fill="{color}" font-family="{MONO if mono else SANS}" font-size="{size}" font-weight="{weight}" {extra}>{escape(str(s))}</text>'

def rr(x,y,w,h,r=10,fill='none',stroke='none',op=1,extra=''):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}" stroke="{stroke}" opacity="{op}" {extra}/>'

def line(x1,y1,x2,y2,color=BORD,width=1,op=1,extra=''):
    return f'<path d="M{x1} {y1}L{x2} {y2}" stroke="{color}" stroke-width="{width}" opacity="{op}" fill="none" {extra}/>'

def circle(x,y,r,fill='none',stroke='none',width=1,op=1,extra=''):
    return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{width}" opacity="{op}" {extra}/>'

def polygon(points,stroke=BORD,fill='none',width=1,op=1):
    return f'<polygon points="{points}" stroke="{stroke}" fill="{fill}" stroke-width="{width}" opacity="{op}"/>'

# HERO / a neural computation scene, not a stock photo.
v=svg_start(1200,438,26)
v+=rr(14,14,1172,410,20,'url(#grid)')
v+=circle(930,212,290,'url(#halo)')
v+=rr(44,36,192,29,14,'#12293E',CYAN,.9)
v+=circle(60,50,4,MINT)+t(74,56,'PROFILE / 2026',12,CYAN,600,True)
v+=t(46,139,'MATEOS',77,WHITE,800,extra='letter-spacing="3"')
v+=t(45,220,'SHARKA',86,CYAN,800,extra='letter-spacing="3"')
v+=rr(47,246,85,4,2,CYAN)+rr(137,246,52,4,2,VIOLET)
v+=t(47,282,'Artificial intelligence  /  Machine learning  /  Data science',18,WHITE,500)
v+=t(47,314,'Turning ambitious ideas into tested, usable AI systems.',17,MUTED)
v+=t(47,353,'BUILD  •  EVALUATE  •  DEPLOY  •  REPEAT',15,MINT,600,True)
v+=t(47,400,'TIRANA  /  ALBANIA',12,FAINT,600,True)
v+=t(340,400,'[ LEARNING IN PUBLIC ]',12,FAINT,600,True)
# right quantum-neural lattice
cx,cy=914,210
for r in (78,121,168,206):
    v+=circle(cx,cy,r,'none',BORD,1.5,.86)
for r,theta1,theta2,col in [(205,-110,-24,CYAN),(169,23,110,VIOLET),(120,146,230,MINT),(78,245,328,CYAN)]:
    x1=cx+r*cos(theta1*pi/180);y1=cy+r*sin(theta1*pi/180)
    x2=cx+r*cos(theta2*pi/180);y2=cy+r*sin(theta2*pi/180)
    v+=f'<path d="M{x1:.1f} {y1:.1f} A{r} {r} 0 0 1 {x2:.1f} {y2:.1f}" fill="none" stroke="{col}" stroke-width="3" opacity=".85"/>'
# neural network nodes laid out left-middle-right across the area
layers=[[(760,132),(751,213),(771,295)],[(851,103),(832,164),(830,242),(853,326)],[(938,126),(955,208),(940,290)],[(1034,169),(1049,255)]]
for k in range(len(layers)-1):
    for i,(ax,ay) in enumerate(layers[k]):
        for j,(bx,by) in enumerate(layers[k+1]):
            if (i+j+k)%3!=2:
                v+=line(ax,ay,bx,by,CYAN if k%2==0 else VIOLET,1.1,.27)
for k,layer in enumerate(layers):
    for i,(x,y) in enumerate(layer):
        col=[CYAN,MINT,VIOLET,CYAN][k]
        v+=circle(x,y,9,BG,col,2,.9)
        v+=circle(x,y,3.5,col,op=.98,extra='class="pulse"' if (i+k)%2==0 else '')
v+=circle(cx,cy,50,'#0C1B35',CYAN,2)
v+=circle(cx,cy,36,'none',VIOLET,1.5,.7)
v+=t(cx-24,cy+8,'AI',27,WHITE,800,True)
v+=t(1107,54,'01 / LAB',12,FAINT,600,True)
v+=t(1057,395,'MODEL STATUS: ACTIVE',11,MINT,600,True)
write('hero.svg',v)

# Section titles, short and consistent.
sections=[('01','THE HUMAN BEHIND THE MODELS','about'),('02','AREAS OF FOCUS','focus'),('03','FEATURED BUILDS','work'),('04','RESEARCH NOTES','research'),('05','THE ENGINEERING LOOP','method'),('06','TECHNOLOGY STACK','stack'),('07','SIGNALS & MILESTONES','recognition'),('08','GITHUB TELEMETRY','telemetry'),('09','LET US CONNECT','connect')]
for num,label,slug in sections:
    v=svg_start(1200,85,14)
    v+=rr(19,17,52,52,11,'#153349','#35657C')
    v+=t(27,51,num,23,CYAN,700,True)
    v+=t(93,52,label,26,WHITE,700,extra='letter-spacing="2"')
    v+=line(710,43,1159,43,'#2B4B67',2)
    for j in range(8):
        v+=circle(1092+j*9,43,2,CYAN if j%3==0 else VIOLET,op=.8)
    write(f'sections/{slug}.svg',v)

# Terminal card
v=svg_start(584,307,19)
v+=rr(1,1,582,46,18,'#172137')
v+=rr(1,30,582,17,0,'#172137')
for i,col in enumerate(('#FF748A',GOLD,MINT)): v+=circle(22+19*i,23,5,col)
v+=t(168,29,'~/mateos-ai/identity',13,MUTED,500,True)
v+=t(27,89,'$ whoami',18,CYAN,600,True)
v+=t(27,120,'AI student / applied ML builder',17,WHITE,500,True)
v+=t(27,161,'$ cat mission.txt',18,CYAN,600,True)
v+=t(27,192,'Make intelligence useful,',17,WHITE,500,True)
v+=t(27,218,'measurable, and accessible.',17,WHITE,500,True)
v+=t(27,264,'$ status --now',18,CYAN,600,True)
v+=t(270,264,'experiments running',15,MINT,600,True)
v+=rr(459,247,10,20,1,CYAN,op=.9,extra='class="blink"')
write('terminal.svg',v)

# Focus mapping: thematic rings, deliberately not a numerical proficiency score.
v=svg_start(584,307,19)
v+=t(28,36,'CURRENT RESEARCH VECTORS',13,MUTED,700,True)
cx,cy=289,159
for r in [53,88,120]:v+=circle(cx,cy,r,'none','#294064',1)
for angle in range(0,360,45):
    x=cx+122*cos(angle*pi/180);y=cy+122*sin(angle*pi/180)
    v+=line(cx,cy,x,y,'#28405F',1)
coords=[]
for r,ang in [(107,-90),(78,-25),(104,30),(92,92),(94,151),(109,215)]:
    coords.append((cx+r*cos(ang*pi/180),cy+r*sin(ang*pi/180)))
pnts=' '.join(f'{x:.1f},{y:.1f}' for x,y in coords)
v+=polygon(pnts,CYAN,'#31D5F1',2,.18)
for i,(x,y) in enumerate(coords):
    v+=circle(x,y,5,CYAN if i%2==0 else VIOLET,extra='class="pulse"' if i%3==0 else '')
v+=t(cx-17,cy+6,'AI',23,WHITE,700,True)
v+=t(241,19,'ML / DL',12,MINT,700,True)
v+=t(413,114,'NLP',13,CYAN,700,True)
v+=t(424,213,'RAG',13,VIOLET,700,True)
v+=t(235,299,'DATA SCIENCE',12,MINT,700,True)
v+=t(40,217,'FORECASTING',12,CYAN,700,True)
v+=t(39,113,'AI SYSTEMS',12,VIOLET,700,True)
write('focus.svg',v)

# Operating principle / not a fake skills chart
v=svg_start(1200,190,18)
entries=[('ML','PREDICTION','Baselines before complexity',CYAN),('DL','REPRESENTATION','Networks that earn their cost',VIOLET),('DS','EVIDENCE','Data, uncertainty, insight',MINT),('AI','APPLICATION','Useful systems, not demos',GOLD)]
for i,(big,head,desc,col) in enumerate(entries):
    x=27+i*295
    if i:v+=line(x-15,31,x-15,155,BORD,1.4)
    v+=t(x+4,79,big,47,col,800,True)
    v+=t(x+92,70,head,15,WHITE,700,True)
    v+=t(x+4,126,desc,16,MUTED,500)
    v+=rr(x+4,146,48,3,2,col)
write('pillars.svg',v)

# Project cards with distinct mini illustrations
projects=[
 ('agrosmart','AGROSMART','AI AGRICULTURE / STARTUP','Plant support + an agricultural','marketplace built for farmers.','AI · CV · Product',MINT,'leaf'),
 ('energyshield','ENERGYSHIELD AI','MACHINE LEARNING / ENERGY','Spot suspicious consumption','with explainable risk signals.','ML · Analytics · Streamlit',CYAN,'bolt'),
 ('uniassist','UNIASSIST','NLP / INFORMATION RETRIEVAL','A university search + chatbot','project grounded in a corpus.','NLP · Search · Python',VIOLET,'chat'),
 ('taxilab','NYC TAXI TIP LAB','PREDICTIVE MODELING / ML','Evaluate tipping models with','real costs and decision rules.','ML · Validation · Python',GOLD,'taxi'),
 ('braindrain','ALBANIA BRAIN DRAIN','DATA SCIENCE / ANALYTICS','Explore migration patterns with','data, statistics and dashboards.','SQL · Python · BI',CYAN,'chart'),
 ('ambulance','SMART AMBULANCE ROUTING','ALGORITHMS / SIMULATION','Pathfinding and route comparison','in a JavaFX 3D simulator.','Java · BFS · A*',VIOLET,'route'),
]

def illustration(kind,x,y,col):
    s=circle(x,y,78,'#132541',BORD,1.3)+circle(x,y,57,'none',col,1.5,.45)
    if kind=='leaf':
        s+=f'<path d="M{x-31} {y+30} Q{x-32} {y-47} {x+36} {y-40} Q{x+48} {y+31} {x-31} {y+30}Z" fill="#173D3A" stroke="{col}" stroke-width="3"/>'
        s+=f'<path d="M{x-29} {y+29}Q{x+3} {y+5} {x+32} {y-34}" fill="none" stroke="{col}" stroke-width="3"/>'
        for dx,dy in [(-7,-9),(6,8),(23,-15)]:s+=circle(x+dx,y+dy,3,GOLD)
    elif kind=='bolt':
        pts=f'{x+5},{y-53} {x-35},{y+3} {x-4},{y+3} {x-17},{y+51} {x+38},{y-15} {x+4},{y-15}'
        s+=polygon(pts,col,'#153B56',2)
        s+=f'<path d="M{x-60} {y+36}l20 -8 15 11 19 -17 23 2 16 -14" fill="none" stroke="{MINT}" stroke-width="2" opacity=".55"/>'
    elif kind=='chat':
        s+=rr(x-50,y-29,74,48,11,'#202A54',VIOLET)+rr(x-6,y-2,60,41,9,'#0C2740',CYAN)
        for dx in (-35,-20,-5):s+=circle(x+dx,y-6,4,VIOLET)
        for dx in (9,24,39):s+=circle(x+dx,y+20,3,CYAN)
    elif kind=='taxi':
        s+=f'<path d="M{x-49} {y+21}l14 -36 h64 l16 36 v21 h-94z" fill="#43351E" stroke="{col}" stroke-width="3"/>'
        s+=rr(x-27,y-7,50,20,3,'#152E46',MUTED)
        for dx in (-31,31):s+=circle(x+dx,y+42,9,BG,col,3)
        s+=rr(x-12,y-34,24,12,3,col)
    elif kind=='chart':
        s+=line(x-52,y+45,x+55,y+45,MUTED,2)+line(x-52,y+45,x-52,y-41,MUTED,2)
        pts=[(-40,26),(-22,3),(-1,11),(22,-26),(45,-38)]
        s+=f'<polyline points="{" ".join(f"{x+a},{y+b}" for a,b in pts)}" fill="none" stroke="{col}" stroke-width="4"/>'
        for a,b in pts:s+=circle(x+a,y+b,4,col)
    elif kind=='route':
        pts=[(x-43,y+39),(x-25,y-22),(x+7,y+2),(x+35,y-36)]
        s+=f'<polyline points="{" ".join(f"{a},{b}" for a,b in pts)}" fill="none" stroke="{col}" stroke-width="4" stroke-dasharray="7 6"/>'
        s+=circle(x-43,y+39,11,'#14263E',MINT,3)+circle(x+35,y-36,11,'#14263E',col,3)
        s+=t(x-48,y+44,'A',12,WHITE,700,True)+t(x+30,y-31,'B',12,WHITE,700,True)
    return s

for slug,name,kind,desc1,desc2,tags,col,shape in projects:
    v=svg_start(584,220,20)
    v+=rr(18,18,3,183,2,col)
    v+=t(38,43,kind,11,col,700,True)
    title_size=22 if len(name)>20 else 27
    v+=t(38,81,name,title_size,WHITE,800)
    v+=t(39,117,desc1,15,MUTED,500)
    v+=t(39,139,desc2,15,MUTED,500)
    v+=rr(38,164,278,31,8,'#15263F','#294461')
    v+=t(49,184,tags,12,CYAN,600,True)
    v+=illustration(shape,481,115,col)
    v+=t(552,199,'↗',24,col,700)
    write(f'projects/{slug}.svg',v)

# Research spotlight
v=svg_start(1200,242,22)
v+=rr(18,18,5,206,3,VIOLET)
v+=t(40,54,'ACTIVE RESEARCH / FORECASTING',15,VIOLET,700,True)
v+=t(39,100,'SPIKING NEURAL NETWORKS',33,WHITE,800)
v+=t(40,132,'EUR/ALL + USD/ALL  •  Technical-event representations  •  Robust baselines',17,MUTED)
v+=t(40,170,'Question: do event-coded spikes improve forecasting beyond simpler alternatives?',16,WHITE,500)
v+=rr(39,193,430,26,7,'#222345','#494377')
v+=t(52,210,'RESEARCH NOTE  /  EVIDENCE OVER HYPE',12,MINT,700,True)
# spikes & comparison traces
for j in range(11):
    x=795+j*31; height=[17,36,64,28,86,41,108,55,27,84,39][j]
    v+=line(x,174,x,174-height,CYAN if j%2==0 else VIOLET,4,.85)
    v+=circle(x,174-height,4,MINT)
v+=line(780,179,1156,179,MUTED,1.2,.5)
v+=t(784,211,'EVENT STREAM / OBSERVATIONS',11,FAINT,600,True)
write('research.svg',v)

# Process map
v=svg_start(1200,251,19)
v+=t(34,40,'FROM PROBLEM DEFINITION TO A WORKING SYSTEM',14,MUTED,700,True)
steps=[('01','FRAME','Formulate the question',CYAN),('02','PREPARE','Clean + trace the data',MINT),('03','MODEL','Establish strong baselines',VIOLET),('04','VALIDATE','Stress-test the results',GOLD),('05','SHIP','Build a usable interface',CYAN)]
for i,(num,name,desc,col) in enumerate(steps):
    x=29+i*235
    v+=rr(x,65,213,145,15,'#112038','#2B3B5D')
    v+=circle(x+39,104,22,'#122D43',col,1.6)
    v+=t(x+25,110,num,14,col,700,True)
    v+=t(x+22,153,name,22,WHITE,700,True)
    v+=t(x+22,180,desc,12,MUTED,500)
    if i<4:
        v+=t(x+217,143,'›',27,MINT,700)
v+=t(33,235,'METHOD: REPRODUCIBILITY  /  CAUSAL SPLITS  /  UNCERTAINTY  /  REAL-WORLD UTILITY',12,FAINT,600,True)
write('pipeline.svg',v)

# Recognition visual – user-supplied award and mentoring info, without invented dates
v=svg_start(1200,236,20)
awards=[('01','INNOVATION BOOTCAMP','1st place  ·  Vanguard / Kantora',GOLD),('02','STUDENTOR STARTUP','1st place  ·  AgroSmart',MINT),('03','CIT TECH TREK 2026','2nd place  ·  AgroSmart',VIOLET)]
for i,(num,label,desc,col) in enumerate(awards):
    x=26+i*390
    v+=rr(x,30,368,170,15,'#101D35','#293A5A')
    v+=circle(x+41,80,21,'#283044',col,2)
    v+=t(x+27,85,num,15,col,700,True)
    v+=t(x+77,77,label,16,WHITE,700,True)
    v+=t(x+24,127,desc,16,MUTED)
    v+=rr(x+23,150,55,3,1,col)
v+=t(30,220,'ALSO: JUNCTIONX TIRANA 2026 FINALIST  •  LEAD MENTOR, ROBOTECH ALBANIA',13,MUTED,600,True)
write('recognition.svg',v)

# Bottom footer graphic
v=svg_start(1200,148,19)
v+=circle(1050,75,190,'url(#halo)')
for i in range(16):
    a=i*2*pi/16
    x=1019+69*cos(a);y=77+48*sin(a)
    v+=circle(round(x,2),round(y,2),3,CYAN if i%3==0 else VIOLET,op=.65)
    if i%2==0:v+=line(1019,77,round(x,2),round(y,2),VIOLET,1,.23)
v+=t(41,57,'LET US BUILD SOMETHING INTELLIGENT.',29,WHITE,800)
v+=t(43,92,'Curiosity to prototype. Evidence to production.',18,MUTED)
v+=t(43,124,'MATEOS SHARKA  /  AI · ML · DL · DS',12,CYAN,700,True)
write('footer.svg',v)
