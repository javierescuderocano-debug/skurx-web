import re, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from sectores_data import S
os.chdir('/home/claude/skurx-web')
h=open('index.html').read()
head0=h.split('<body>')[0]
dialog=h[h.index('<dialog'):h.index('</dialog>')+9].replace('src="fini-avatar.svg"','src="../fini-avatar.svg"').replace('<a href="/privacidad.html" target="_blank"','<a href="../privacidad.html" target="_blank"')
close=re.search(r'<section class="contact" id="contacto">.*?</section>',h,re.S).group(0)
head0=re.sub(r'<script type="application/ld\+json">.*?</script>','',head0)
for a in ['href="favicon.svg"','href="favicon-32.png"','href="apple-touch-icon.png"','href="hero-bg.webp"']: head0=head0.replace(a,a.replace('href="','href="../'))
head0=head0.replace('href="styles.css?','href="../styles.css?').replace('src="fini.js?','src="../fini.js?')
os.makedirs('sectores',exist_ok=True)
for s in S:
    plural=s['fini'].split('|')[2]
    title=f'Automatización para {plural} | SKURX SYSTEMS'
    desc=re.sub('<[^>]+>','',s['lead']).split('. ')[0].rstrip('.')+'.'
    url=f"https://skurx.es/sectores/{s['slug']}.html"
    head=head0.replace('<title>SKURX SYSTEMS | Automatización de Recursos</title>',f'<title>{title}</title>')
    head=re.sub(r'<meta name="description" content="[^"]*">',f'<meta name="description" content="Automatización e IA para {plural}. {desc}">',head)
    head=re.sub(r'<link rel="canonical" href="[^"]*">',f'<link rel="canonical" href="{url}">',head)
    head=re.sub(r'<meta property="og:url" content="[^"]*">',f'<meta property="og:url" content="{url}">',head)
    head=re.sub(r'<meta property="og:title" content="[^"]*">',f'<meta property="og:title" content="{title}">',head)
    head=re.sub(r'<meta property="og:description" content="[^"]*">',f'<meta property="og:description" content="Automatización e IA para {plural}. {desc}">',head)
    pains=''.join('<article class="pain"><small>%02d</small><h3>%s</h3><p>%s</p><div class="fix"><b>LO QUE HACEMOS · %s</b><p>%s</p></div></article>'%(i+1,t,d,k.upper(),f) for i,(t,d,f,k) in enumerate(s['pains']))
    F=s['flow']
    flow=''.join('<li%s><b>%s</b>%s</li>'%(' class="result"' if i==len(F)-1 else '',t,x) for i,(t,x) in enumerate(F))
    fe=s.get('feature')
    feature=('<section class="sector-feature"><div class="sf-copy"><p class="eyebrow dark">%s</p><h2>%s</h2><p>%s</p><ul>%s</ul></div><figure class="sf-art"><div class="ba-frame" style="--pos:50%%"><img src="../reforma-antes.webp" width="1586" height="992" alt="Antes: salón y cocina de un piso antiguo, separados por un tabique, con muebles oscuros, azulejo de época y poca luz." loading="lazy"><div class="ba-after"><img src="../reforma-despues.webp" width="1586" height="992" alt="Después: el mismo piso reformado, con cocina abierta al salón, isla, tarima de madera y luz cálida." loading="lazy"></div><span class="ba-tag ba-tag-a">ANTES</span><span class="ba-tag ba-tag-d">DESPUÉS</span><span class="ba-handle" aria-hidden="true"></span><input type="range" min="0" max="100" value="50" aria-label="Comparar el antes y el después"></div><figcaption>Desliza para comparar. Imagen de ejemplo generada por ordenador.</figcaption></figure><script>document.querySelectorAll(".ba-frame input").forEach(function(i){var f=i.parentNode;function u(){var v=+i.value;f.style.setProperty("--pos",v+"%%");f.classList.toggle("ba-solo-antes",v>=85);f.classList.toggle("ba-solo-despues",v<=15)}i.addEventListener("input",u);u()});</script></section>'%(fe['eyebrow'],fe['h2'],fe['p'],''.join('<li>%s</li>'%i for i in fe['items']))) if fe else ''
    body=f'''<body data-fini-sector="{s['fini']}"><a class="skip-link" href="#contenido">Saltar al contenido</a><header class="site-header"><a class="brand-lockup" href="../index.html" aria-label="SKURX SYSTEMS, inicio"><span class="brand-name"><strong>SKURX</strong><span>SYSTEMS</span></span><span class="brand-tagline">CAPACIDAD LIBERADA</span></a><nav aria-label="Navegación principal"><a href="../index.html#inicio">Quiénes somos</a><a href="../index.html#que-hacemos">Qué hacemos</a><a href="../index.html#como-lo-hacemos">Cómo lo hacemos</a><a href="../index.html#sectores">Sectores</a></nav><a class="header-contact" href="#auditoria" data-contact-open aria-haspopup="dialog" aria-controls="panel-contacto"><span class="contact-label">Hablemos</span><span class="contact-arrow" aria-hidden="true">↗</span></a></header><script>if("scrollRestoration" in history)history.scrollRestoration="manual";if(!location.hash)window.scrollTo(0,0);</script><main id="contenido">
<section class="sector-hero"><p class="crumb"><a href="../index.html#sectores">SECTORES</a> · {s['name'].upper()}</p><h1>{s['h1']}</h1><p class="lead">{s['lead']}</p><a class="gold-link" href="#auditoria" data-contact-open aria-haspopup="dialog" aria-controls="panel-contacto">{s['cta']} <span aria-hidden="true">→</span></a></section>
<section class="pains"><p class="eyebrow dark">DÓNDE SE PIERDE CAPACIDAD</p><h2>{s['h2']}</h2><div class="pain-grid">{pains}</div></section>
{feature}<section class="sector-flowsec"><p class="eyebrow">EN LA PRÁCTICA</p><h2>Un día cualquiera,<br>con el sistema funcionando.</h2><p class="note">Escenario ilustrativo basado en situaciones habituales.</p><ul class="sector-flow">{flow}</ul></section>
<section class="sector-audit" id="auditoria"><p class="eyebrow dark">SIN CAJAS NEGRAS</p><div class="process-control sector-control"><article><h3>Documentado</h3><p>Cada flujo explicado en lenguaje claro.</p></article><article><h3>A nombre de tu empresa</h3><p>Cuentas, herramientas y datos son tuyos.</p></article><article><h3>Auditable</h3><p>Puedes ver qué ha hecho cada automatización y cuándo.</p></article><article><h3>Sin dependencia</h3><p>Si dejamos de trabajar juntos, todo sigue siendo tuyo.</p></article></div><div class="process-audit"><div><p class="eyebrow">EL PRIMER PASO</p><h3>Auditoría Operativa Inicial para {plural}</h3><p>{s['audit']} Te entregamos un mapa claro de qué automatizar y en qué orden. El informe es tuyo, decidas lo que decidas.</p></div><a class="gold-link" href="#auditoria" data-contact-open data-fini-intent="auditoria" aria-haspopup="dialog" aria-controls="panel-contacto">Solicitar auditoría <span aria-hidden="true">→</span></a></div></section>
{close}</main><footer><p>SKURX SYSTEMS - AUTOMATIZACIÓN DE RECURSOS<a class="footer-legal" href="../privacidad.html"><span class="sep" aria-hidden="true">· </span>Privacidad</a></p></footer>{dialog}</body></html>'''
    open(f"sectores/{s['slug']}.html",'w').write(head+body)
# Portada: "Más sectores" con los nueve sin tarjeta
extra=[s for s in S if s['slug'] not in ('inmobiliarias','gestorias','automocion')]
lis=''.join(f'<li><a href="sectores/{s["slug"]}.html">{s["name"]}<span aria-hidden="true">→</span></a></li>' for s in extra)
h=re.sub(r'(<p class="eyebrow" id="accede-sector">MÁS SECTORES</p><ul>).*?(</ul>)',lambda m:m.group(1)+lis+m.group(2),h,flags=re.S)
open('index.html','w').write(h)
print('páginas:',len(S))
