from pathlib import Path

path=Path('index.html')
s=path.read_text(encoding='utf-8')

def replace_once(old,new,label):
    global s
    if old not in s:
        raise SystemExit(f'Patch marker not found: {label}')
    s=s.replace(old,new,1)

if 'name="copyright"' not in s:
    old='<meta name="description" content="Project Balboa — una infraestructura monetaria digital para Panamá.">'
    new='''<meta name="description" content="Project Balboa — estabilidad del dólar, infraestructura digital y soberanía panameña.">
<meta name="author" content="Project Balboa">
<meta name="copyright" content="© 2026 Project Balboa. All rights reserved.">
<meta name="robots" content="index,follow,max-image-preview:large">
<link rel="canonical" href="https://project-balboa.github.io/">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Project Balboa">
<meta property="og:title" content="Project Balboa | Digital Sovereign Money Infrastructure">
<meta property="og:description" content="Dollar stability. Digital infrastructure. Panamanian sovereignty.">
<meta property="og:url" content="https://project-balboa.github.io/">
<meta property="og:image" content="https://project-balboa.github.io/assets/hero-panama.webp">
<meta property="og:image:alt" content="Project Balboa — Panama digital monetary infrastructure concept">
<meta property="og:locale" content="en_US">
<meta property="og:locale:alternate" content="es_PA">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="Project Balboa | Digital Sovereign Money Infrastructure">
<meta name="twitter:description" content="Dollar stability. Digital infrastructure. Panamanian sovereignty.">
<meta name="twitter:image" content="https://project-balboa.github.io/assets/hero-panama.webp">'''
    replace_once(old,new,'metadata')

s=s.replace('<title>Project Balboa | Infraestructura Monetaria Digital para Panamá</title>','<title>Project Balboa | Infraestructura Monetaria Digital</title>')

if 'assets/bilingual.css' not in s:
    replace_once('</style>\n</head>','</style>\n<link rel="stylesheet" href="assets/bilingual.css">\n</head>','bilingual stylesheet')

if 'id="langEs"' not in s:
    old='<nav><div class="wrap nav"><a class="brand" href="#inicio"><span class="mark">B/.</span>Project Balboa</a><div class="links"><a href="#oportunidad">Oportunidad</a><a href="#como">Cómo funciona</a><a href="#experiencia">Experiencia</a><a href="#caso">Caso país</a><a href="#riesgos">Riesgos</a><a href="#hoja">Hoja de ruta</a></div><a class="cta" href="#como">Explorar</a></div></nav>'
    new='<nav><div class="wrap nav"><a class="brand" href="#inicio"><span class="mark">B/.</span>Project Balboa</a><div class="links"><a href="#oportunidad">Oportunidad</a><a href="#como">Cómo funciona</a><a href="#experiencia">Experiencia</a><a href="#caso">Caso país</a><a href="#riesgos">Riesgos</a><a href="#hoja">Hoja de ruta</a></div><div class="nav-actions"><div class="lang-toggle" role="group" aria-label="Language selector"><button id="langEs" type="button" aria-pressed="true">ES</button><button id="langEn" type="button" aria-pressed="false">EN</button></div><a class="cta" href="#como">Explorar</a></div></div></nav>'
    replace_once(old,new,'navigation')

if 'id="contact"' not in s:
    contact='''<section id="contact" class="section"><div class="wrap"><div class="contact-card reveal"><div><div class="eyebrow">Conversemos</div><h2>¿Interesado en Project Balboa?</h2><p class="copy">Si estás explorando dinero digital, infraestructura pública, innovación financiera o posibles colaboraciones, nos interesa conversar.</p></div><div class="contact-action"><a id="contactLink" class="btn primary" href="#" data-u="projectdigitalbalboa" data-d="gmail.com">Contactar Project Balboa →</a></div></div></div></section>'''
    replace_once('\n</main>\n<footer>',f'\n{contact}\n</main>\n<footer>','contact section')

if 'footer-meta' not in s:
    old='<footer><div class="wrap foot"><div><b style="color:#dfffea">Project Balboa</b><br>Concept Paper · 2026</div><div>Documento conceptual para discusión. No constituye política pública ni asesoría financiera.</div></div></footer>'
    new='<footer><div class="wrap foot"><div class="footer-meta"><b style="color:#dfffea">Project Balboa</b><span>Versión 1.0 · septiembre de 2026</span><span>© 2026 Project Balboa. Todos los derechos reservados.</span></div><div class="footer-meta"><span>Documento conceptual para discusión. No constituye política pública ni asesoría financiera.</span><div class="footer-links"><a id="termsLink" href="terms.html?lang=es">Términos de uso</a><a href="#contact">Contacto</a></div></div></div></footer>'
    replace_once(old,new,'footer')

if 'assets/i18n.js' not in s:
    replace_once('</script>\n</body>','</script>\n<script src="assets/i18n.js"></script>\n</body>','i18n script')

path.write_text(s,encoding='utf-8')
print('Bilingual Project Balboa patch applied.')
