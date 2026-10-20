"""Black + silver GitHub profile generator.
Edit CONFIG below (or send me your resume and I'll fill it), then run:  python3 generate_profile.py
"""
from xml.sax.saxutils import escape as esc
import os, textwrap

CONFIG = {
  "name": "Poovarasan",
  "role": "SOFTWARE DEVELOPER  ·  UI/UX DESIGNER",
  "tagline": ["Engineering interfaces.", "Designing experiences."],
  "about_lines": [
    "B.E. Computer Science student at KIT, Coimbatore (CGPA 7.91).",
    "I build responsive web apps and machine learning projects,",
    "and sharpen my problem solving daily: 1,490+ questions solved.",
  ],
  "pillars": ["Web Development", "Machine Learning", "Competitive Programming"],
  "projects": [
    {"title": "Loan Approval Prediction", "desc": "Compared Logistic Regression, Decision Tree and Random Forest to predict loan outcomes.", "tags": ["Python", "Scikit-learn", "Pandas", "NumPy"]},
    {"title": "Book Recommendation System", "desc": "Collaborative and content-based filtering for personalized book suggestions.", "tags": ["Python", "Machine Learning", "Pandas", "NumPy"]},
    {"title": "Smart Traffic Management", "desc": "OpenCV vehicle counting plus ML to adjust signal timing from live traffic density.", "tags": ["Python", "OpenCV", "Machine Learning", "IoT"]},
  ],
  "toolkit": {
    "LANGUAGES":  ["Java", "Python", "C", "C++", "SQL", "JavaScript"],
    "WEB & DATA": ["HTML", "CSS", "Node.js", "MongoDB"],
    "ML & TOOLS": ["Scikit-learn", "Pandas", "NumPy", "OpenCV", "Git", "GitHub"],
    "CS CORE":    ["DSA", "DBMS", "OOPS", "Operating Systems", "Networks"],
  },
  "footer": "Building things that feel as good as they work.",
}

SERIF="Georgia, 'Iowan Old Style', 'Palatino Linotype', serif"
MONO='ui-monospace, SFMono-Regular, Menlo, Consolas, monospace'
SANS="-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
BG="#050505"; CARD="#0A0A0B"; MUTED="#8B8B93"; TXT="#D8D8DE"

DEFS = lambda p, w: f'''
<linearGradient id="{p}sil" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#FFFFFF"/><stop offset=".45" stop-color="#D4D4DB"/><stop offset="1" stop-color="#9A9AA3"/></linearGradient>
<linearGradient id="{p}edge" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#E8E8EE" stop-opacity=".75"/><stop offset=".5" stop-color="#5A5A62" stop-opacity=".35"/><stop offset="1" stop-color="#C4C4CC" stop-opacity=".6"/></linearGradient>
<linearGradient id="{p}line" gradientUnits="userSpaceOnUse" x1="60" y1="0" x2="{w-60}" y2="0"><stop offset="0" stop-color="#C4C4CC"/><stop offset=".6" stop-color="#5A5A62"/><stop offset="1" stop-color="#5A5A62" stop-opacity="0"/></linearGradient>
<linearGradient id="{p}sheen" gradientUnits="userSpaceOnUse" x1="-260" y1="0" x2="0" y2="0"><stop offset="0" stop-color="#9A9AA3"/><stop offset=".5" stop-color="#FFFFFF"/><stop offset="1" stop-color="#9A9AA3"/>
<animateTransform attributeName="gradientTransform" type="translate" values="0 0;{w+300} 0;{w+300} 0" keyTimes="0;.45;1" dur="7s" repeatCount="indefinite"/></linearGradient>'''

def svg(w,h,body,p,label):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" aria-label="{esc(label)}"><defs>{DEFS(p,w)}</defs>{body}</svg>'

def chips(items,x,y,size=12):
    out=[];cx=x
    for t in items:
        wd=len(t)*size*.61+26
        out.append(f'<rect x="{cx:.0f}" y="{y}" width="{wd:.0f}" height="28" rx="14" fill="#111113" stroke="#3A3A40"/><text x="{cx+wd/2:.0f}" y="{y+18}" text-anchor="middle" font-family="{MONO}" font-size="{size}" fill="#C4C4CC">{esc(t)}</text>')
        cx+=wd+10
    return ''.join(out)

def write(name,s): open(f'assets/{name}','w').write(s)

# ---------- HERO ----------
b64=open('portrait.b64').read()
c=CONFIG; W,H=1200,560
hero=f'''
<rect width="{W}" height="{H}" rx="18" fill="{BG}"/>
<pattern id="dots" width="28" height="28" patternUnits="userSpaceOnUse"><circle cx="2" cy="2" r="1" fill="#2A2A2E"/></pattern>
<rect width="{W}" height="{H}" rx="18" fill="url(#dots)" opacity=".7"/>
<radialGradient id="glow" cx=".5" cy=".5" r=".5"><stop offset="0" stop-color="#C4C4CC" stop-opacity=".30"/><stop offset=".6" stop-color="#6A6A72" stop-opacity=".08"/><stop offset="1" stop-color="#000" stop-opacity="0"/></radialGradient>
<ellipse cx="900" cy="300" rx="360" ry="330" fill="url(#glow)"><animate attributeName="opacity" values=".8;1;.8" dur="6s" repeatCount="indefinite"/></ellipse>
<circle cx="900" cy="300" r="250" fill="none" stroke="url(#hsil)" stroke-opacity=".35" stroke-dasharray="2 9"><animateTransform attributeName="transform" type="rotate" from="0 900 300" to="360 900 300" dur="90s" repeatCount="indefinite"/></circle>
<circle cx="900" cy="300" r="205" fill="none" stroke="#C4C4CC" stroke-opacity=".12"/>
<image href="data:image/webp;base64,{b64}" x="{900-402*.64/2*1.0:.0f}" y="{H-860*.64+4:.0f}" width="{402*.64:.0f}" height="{860*.64:.0f}" preserveAspectRatio="xMidYMax meet"/>
<linearGradient id="fade" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{BG}" stop-opacity="0"/><stop offset="1" stop-color="{BG}"/></linearGradient>
<rect x="640" y="{H-130}" width="520" height="130" fill="url(#fade)"/>
<g font-family="{MONO}" font-size="13" letter-spacing="3.2" fill="{MUTED}">
  <circle cx="64" cy="112" r="4" fill="#E8E8EE"><animate attributeName="opacity" values="1;.25;1" dur="2.4s" repeatCount="indefinite"/></circle>
  <text x="80" y="117">{esc(c["role"])}</text></g>
<text x="60" y="232" font-family="{SERIF}" font-size="104" font-weight="700" letter-spacing="-2" fill="url(#hsil)">{esc(c["name"])}</text>
<text x="60" y="232" font-family="{SERIF}" font-size="104" font-weight="700" letter-spacing="-2" fill="url(#hsheen)" opacity=".85">{esc(c["name"])}</text>
<rect x="64" y="262" width="120" height="2" fill="url(#hline)"/>
<text x="62" y="318" font-family="{SERIF}" font-style="italic" font-size="32" fill="{TXT}">{esc(c["tagline"][0])}</text>
<text x="62" y="360" font-family="{SERIF}" font-style="italic" font-size="32" fill="{MUTED}">{esc(c["tagline"][1])}</text>
<g font-family="{MONO}" font-size="12" letter-spacing="2" fill="{MUTED}">
  <text x="64" y="440">B.E. COMPUTER SCIENCE  ·  KIT, COIMBATORE  ·  2024-2028</text><text x="64" y="470">PORTFOLIO</text><text x="64" y="492" fill="#C4C4CC" font-size="14">poovarasanportfolio.vercel.app</text></g>
<g font-family="{MONO}" font-size="11" letter-spacing="3" fill="#4A4A52" transform="translate(1160 60) rotate(90)"><text>PORTFOLIO  ·  2026</text></g>
<rect x=".5" y=".5" width="{W-1}" height="{H-1}" rx="18" fill="none" stroke="url(#hedge)" stroke-width="1.2"/>'''
write('hero.svg', svg(W,H,hero,'h',f'{c["name"]} — {c["role"]}'))

# ---------- SECTION TITLES ----------
def title(file,num,head,sub,p):
    body=f'''<rect width="1200" height="100" fill="none"/>
<text x="62" y="44" font-family="{MONO}" font-size="13" letter-spacing="4" fill="{MUTED}">{num}  /  {sub.upper()}</text>
<text x="60" y="86" font-family="{SERIF}" font-size="40" font-weight="700" fill="url(#{p}sil)">{esc(head)}</text>
<text x="60" y="86" font-family="{SERIF}" font-size="40" font-weight="700" fill="url(#{p}sheen)" opacity=".8">{esc(head)}</text>
<rect x="60" y="96" width="1080" height="1.5" fill="url(#{p}line)"/>'''
    write(file, svg(1200,100,body,p,f'{num} {head}'))
title('title-about.svg','01',"Hello, I'm Poovarasan.",'About','a')
title('title-recognition.svg','02','Proof, on the record.','Recognition','r')
title('title-work.svg','03','Selected work.','Projects','w')
title('title-toolkit.svg','04','The tools I reach for.','Toolkit','t')
title('title-commits.svg','05','A year of building.','Commit log','c')
title('title-certs.svg','06','Credentials.','Certifications','e')
title('title-connect.svg','07',"Let's build something.",'Connect','n')

# ---------- ABOUT ----------
H=250
ab=f'<rect x="1" y="1" width="1198" height="{H-2}" rx="16" fill="{CARD}" stroke="url(#aedge)"/>'
ab+=f'<rect x="40" y="40" width="3" height="{H-80}" rx="1.5" fill="url(#asil)"/>'
for i,l in enumerate(c["about_lines"]):
    ab+=f'<text x="68" y="{82+i*38}" font-family="{SERIF}" font-size="23" fill="{TXT}">{esc(l)}</text>'
ab+=f'<line x1="810" y1="40" x2="810" y2="{H-40}" stroke="#2A2A2E"/>'
for i,pl in enumerate(c["pillars"]):
    y=80+i*52
    ab+=f'<text x="850" y="{y}" font-family="{MONO}" font-size="13" fill="{MUTED}">0{i+1}</text><text x="890" y="{y}" font-family="{SANS}" font-size="19" fill="#E8E8EE">{esc(pl)}</text><rect x="850" y="{y+14}" width="290" height="1" fill="#26262A"/>'
write('about.svg', svg(1200,H,ab,'a','About'))

# ---------- PROJECTS ----------
for i,pj in enumerate(c["projects"],1):
    H=200
    s=f'<rect x="1" y="1" width="1198" height="{H-2}" rx="16" fill="{CARD}" stroke="url(#p{i}edge)"/>'
    s+=f'<text x="50" y="118" font-family="{SERIF}" font-size="84" font-weight="700" fill="none" stroke="url(#p{i}sil)" stroke-width="1.2" opacity=".55">0{i}</text>'
    s+=f'<text x="200" y="76" font-family="{SERIF}" font-size="32" font-weight="700" fill="url(#p{i}sil)">{esc(pj["title"])}</text>'
    s+=f'<text x="200" y="110" font-family="{SANS}" font-size="16" fill="{MUTED}">{esc(pj["desc"])}</text>'
    s+=chips(pj["tags"],200,136)
    s+=f'<circle cx="1110" cy="100" r="28" fill="none" stroke="#3A3A40"><animate attributeName="stroke" values="#3A3A40;#C4C4CC;#3A3A40" dur="4s" repeatCount="indefinite"/></circle><text x="1110" y="109" text-anchor="middle" font-family="{SANS}" font-size="26" fill="#C4C4CC">↗</text>'
    write(f'project-{i}.svg', svg(1200,H,s,f'p{i}',pj["title"]))

# ---------- TOOLKIT ----------
rows=c["toolkit"]; H=40+len(rows)*70
t=f'<rect x="1" y="1" width="1198" height="{H-2}" rx="16" fill="{CARD}" stroke="url(#tedge)"/>'
for i,(k,v) in enumerate(rows.items()):
    y=40+i*70
    t+=f'<text x="50" y="{y+20}" font-family="{MONO}" font-size="12" letter-spacing="3" fill="{MUTED}">{esc(k)}</text>'
    t+=chips(v,280,y,13)
    if i<len(rows)-1: t+=f'<rect x="50" y="{y+50}" width="1100" height="1" fill="#1C1C1F"/>'
write('toolkit.svg', svg(1200,H,t,'t','Toolkit'))

# ---------- FOOTER ----------
f=f'''<rect width="1200" height="170" rx="16" fill="{CARD}"/><rect x="1" y="1" width="1198" height="168" rx="16" fill="none" stroke="url(#fedge)"/>
<text x="600" y="82" text-anchor="middle" font-family="{SERIF}" font-style="italic" font-size="28" fill="{TXT}">{esc(c["footer"])}</text>
<rect x="540" y="104" width="120" height="1.5" fill="url(#fsil)"/>
<text x="600" y="140" text-anchor="middle" font-family="{SERIF}" font-size="22" font-weight="700" letter-spacing="6" fill="url(#fsil)">{esc(c["name"].upper())}</text>'''
write('footer.svg', svg(1200,170,f,'f','Footer'))

# ---------- JOURNEY (education + experience) ----------
H=250
j=f'<rect x="1" y="1" width="1198" height="{H-2}" rx="16" fill="{CARD}" stroke="url(#jedge)"/><line x1="600" y1="36" x2="600" y2="{H-36}" stroke="#2A2A2E"/>'
j+=f'<text x="50" y="52" font-family="{MONO}" font-size="12" letter-spacing="3" fill="{MUTED}">EDUCATION</text>'
j+=f'<text x="50" y="92" font-family="{SERIF}" font-size="26" font-weight="700" fill="url(#jsil)">B.E. Computer Science and Engineering</text>'
j+=f'<text x="50" y="122" font-family="{SANS}" font-size="16" fill="{TXT}">Kalaignarkarunanidhi Institute of Technology, Coimbatore</text>'
j+=f'<text x="50" y="148" font-family="{MONO}" font-size="13" fill="{MUTED}">2024 - 2028   ·   CGPA 7.91 / 10</text>'
j+=chips(["Data Structures","DBMS","OS","OOP","Networks","DAA"],50,172,11)
j+=f'<text x="650" y="52" font-family="{MONO}" font-size="12" letter-spacing="3" fill="{MUTED}">EXPERIENCE</text>'
j+=f'<text x="650" y="92" font-family="{SERIF}" font-size="26" font-weight="700" fill="url(#jsil)">Web Development Intern</text>'
j+=f'<text x="650" y="122" font-family="{SANS}" font-size="16" fill="{TXT}">Appin Technology, Coimbatore</text>'
for i,l in enumerate(["Built responsive web pages with HTML, CSS and JavaScript","Basic backend integration and project deployment","Sharpened debugging and UI design skills"]):
    j+=f'<text x="650" y="{156+i*26}" font-family="{SANS}" font-size="14.5" fill="{MUTED}"><tspan fill="#C4C4CC">▸ </tspan>{esc(l)}</text>'
write('journey.svg', svg(1200,H,j,'j','Education and experience'))

# ---------- RECOGNITION ----------
stats=[("1,490+","Problems solved","Across all platforms"),("71","Contests attended","Overall"),("214","Active days","Codolio"),
       ("1,081","CodeChef solved","Max rating 1051"),("1,384","CodeChef DSA peak","Rating 1355 now"),("353","LeetCode solved","Contest rating 1309")]
H=330
r=''
for i,(n,l,sub) in enumerate(stats):
    x=i%3*400+(0 if i%3==0 else 0); y=i//3*165
    r+=f'<rect x="{x+5}" y="{y+5}" width="390" height="155" rx="16" fill="{CARD}" stroke="url(#redge)"/>'
    r+=f'<text x="{x+36}" y="{y+256-165*0-170+0}" font-size="1" fill="none"/>'
    r+=f'<text x="{x+36}" y="{y+88}" font-family="{SERIF}" font-size="60" font-weight="700" fill="url(#rsil)">{n}</text>'
    r+=f'<text x="{x+36}" y="{y+120}" font-family="{SANS}" font-size="17" fill="#E8E8EE">{l}</text>'
    r+=f'<text x="{x+36}" y="{y+142}" font-family="{MONO}" font-size="12" fill="{MUTED}">{sub}</text>'
r+=f'<circle cx="{5+390-34}" cy="34" r="4" fill="#C4C4CC"><animate attributeName="opacity" values="1;.2;1" dur="2.4s" repeatCount="indefinite"/></circle>'
write('recognition.svg', svg(1200,H,r,'r','Competitive programming stats'))

# ---------- CERTIFICATIONS ----------
certs=[("NPTEL","Programming in Java","Elite + Silver"),("DELOITTE","Data Analytics","Job Simulation"),("INFOSYS","Software Engineering","Course"),("CISCO CCNA","Introduction to Networks","Course")]
H=170; cs=''
for i,(a,b,c2) in enumerate(certs):
    x=i*300
    cs+=f'<rect x="{x+5}" y="5" width="290" height="{H-10}" rx="16" fill="{CARD}" stroke="url(#eedge)"/>'
    cs+=f'<text x="{x+28}" y="50" font-family="{MONO}" font-size="12" letter-spacing="3" fill="{MUTED}">{a}</text>'
    cs+=f'<text x="{x+28}" y="90" font-family="{SERIF}" font-size="22" font-weight="700" fill="url(#esil)">{esc(b)}</text>'
    cs+=f'<rect x="{x+28}" y="108" width="40" height="2" fill="url(#esil)"/>'
    cs+=f'<text x="{x+28}" y="138" font-family="{SANS}" font-size="14" fill="{TXT}">{esc(c2)}</text>'
write('certifications.svg', svg(1200,H,cs,'e','Certifications'))
print('ok', os.listdir('assets'))
