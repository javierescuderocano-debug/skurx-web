"""Genera las páginas de sector (español) y todas las páginas de otros idiomas.

Uso:  python3 tools/build_site.py

- Fuente única en español: index.html y privacidad.html (se editan a mano),
  tools/sectores_data.py (contenido de las 12 páginas de sector).
- Cada idioma: tools/i18n_<código>.py (textos) y tools/sectores_data_<código>.py.
- El script comprueba que no queda ningún texto sin traducir y falla si lo hay.
"""
import html as H, importlib, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
SITE = 'https://skurx.es'
LANGS = ['en', 'ca', 'fr', 'de', 'nl', 'it', 'pt', 'uk', 'ru', 'zh', 'ar', 'sr', 'pl']                      # idiomas además del español

from sectores_data import S as S_ES
SECTOR_UI_ES = {
    'title': 'Automatización para {plural} | SKURX SYSTEMS',
    'desc': 'Automatización e IA para {plural}. {desc}',
    'crumb': 'SECTORES', 'pains_eyebrow': 'DÓNDE SE PIERDE CAPACIDAD', 'fix': 'LO QUE HACEMOS',
    'flow_eyebrow': 'EN LA PRÁCTICA', 'flow_h2': 'Un día cualquiera,<br>con el sistema funcionando.',
    'flow_note': 'Escenario ilustrativo basado en situaciones habituales.', 'control_eyebrow': 'SIN CAJAS NEGRAS',
    'audit_h3': 'Auditoría Operativa Inicial para {plural}',
    'audit_tail': 'Te entregamos un mapa claro de qué automatizar y en qué orden. El informe es tuyo, decidas lo que decidas.',
    'audit_btn': 'Solicitar auditoría',
    'ba_before_alt': 'Antes: salón y cocina de un piso antiguo, separados por un tabique, con muebles oscuros, azulejo de época y poca luz.',
    'ba_after_alt': 'Después: el mismo piso reformado, con cocina abierta al salón, isla, tarima de madera y luz cálida.',
    'ba_before': 'ANTES', 'ba_after': 'DESPUÉS', 'ba_aria': 'Comparar el antes y el después',
    'ba_caption': 'Desliza para comparar. Imagen de ejemplo generada por ordenador.',
}
CONTROL_ES = [('Documentado', 'Cada flujo explicado en lenguaje claro.'), ('A nombre de tu empresa', 'Cuentas, herramientas y datos son tuyos.'),
              ('Auditable', 'Puedes ver qué ha hecho cada automatización y cuándo.'), ('Sin dependencia', 'Si dejamos de trabajar juntos, todo sigue siendo tuyo.')]


# ------------------------------------------------------------------ utilidades
LANG_NAMES = {'es': 'Español', 'en': 'English', 'ca': 'Català', 'fr': 'Français', 'de': 'Deutsch', 'nl': 'Nederlands', 'it': 'Italiano',
              'pt': 'Português', 'uk': 'Українська', 'ru': 'Русский', 'zh': '中文', 'ar': 'العربية', 'sr': 'Srpski', 'pl': 'Polski'}
GLOBE = ('<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c2.5 2.6 3.8 5.6 3.8 9s-1.3 6.4-3.8 9'
         'M12 3c-2.5 2.6-3.8 5.6-3.8 9s1.3 6.4 3.8 9"/></svg>')


def switcher(label, es_href, others, current):
    """Desplegable de idioma. others: [(código, href)]. current: idioma de la página."""
    items = [('es', es_href)] + others
    links = ''.join('<li><a href="%s" hreflang="%s" lang="%s"%s><span>%s</span><b>%s</b></a></li>' % (
        h, c, c, ' aria-current="page"' if c == current else '', LANG_NAMES[c], c.upper()) for c, h in items)
    return ('<nav class="lang-switch" aria-label="%s"><details class="lang-menu"><summary>%s<span>%s</span></summary><ul>%s</ul></details>'
            '<script>document.addEventListener("click",function(e){document.querySelectorAll(".lang-menu[open]").forEach(function(d){if(!d.contains(e.target))d.removeAttribute("open")})});</script></nav>'
            ) % (label, GLOBE, current.upper(), links)


def alternates(urls):
    """urls: {código: url absoluta}"""
    out = ''.join('<link rel="alternate" hreflang="%s" href="%s">' % (c, u) for c, u in urls.items())
    return out + '<link rel="alternate" hreflang="x-default" href="%s">' % urls['es']


def set_alternates(page, urls):
    page = re.sub(r'<link rel="alternate" hreflang="[^"]*" href="[^"]*">', '', page)
    return page.replace('</head>', alternates(urls) + '</head>', 1)


def set_switcher(page, sw):
    """Envuelve el botón de contacto del header con el selector de idioma (idempotente)."""
    page = re.sub(r'<div class="header-actions"><nav class="lang-switch".*?</nav>', '<div class="header-actions">' + sw, page, flags=re.S)
    if '<div class="header-actions">' not in page:
        page = re.sub(r'(<a class="header-contact".*?</a>)(</header>)', '<div class="header-actions">' + sw + r'\1</div>\2', page, count=1, flags=re.S)
    return page


def translate(page, table, fname):
    """Sustituye nodos de texto y atributos cuyo contenido exacto está en la tabla."""
    table = {k.strip(): v.strip() for k, v in table.items()}
    missing = set()

    def tx(m):
        raw = m.group(1)
        key = H.unescape(raw).strip()
        if not key or key in table:
            if not key:
                return m.group(0)
            lead = raw[:len(raw) - len(raw.lstrip())]
            trail = raw[len(raw.rstrip()):]
            return '>' + lead + H.escape(table[key], quote=False) + trail + '<'
        if re.search(r'[a-záéíóúñ]{3,}', key, re.I) and key not in KEEP:
            missing.add(key)
        return m.group(0)

    def at(m):
        key = H.unescape(m.group(2))
        if key in table:
            return '%s="%s"' % (m.group(1), H.escape(table[key]))
        return m.group(0)

    head, body = page.split('<body', 1)
    # scripts y estilos fuera de la traducción
    parts = re.split(r'(<script.*?</script>|<style.*?</style>)', '<body' + body, flags=re.S)
    parts = [p if p.startswith(('<script', '<style')) else re.sub(r'>([^<>]+)<', tx, p) for p in parts]
    body = ''.join(parts)
    head = re.sub(r'<title>(.*?)</title>', lambda m: '<title>%s</title>' % H.escape(table.get(H.unescape(m.group(1)), m.group(1)), quote=False), head)
    page = head + body
    page = re.sub(r'\b(alt|aria-label|placeholder|content|title|data-next-label|data-top-label)="([^"]*)"', at, page)
    if missing:
        raise SystemExit('Sin traducir en %s:\n  - %s' % (fname, '\n  - '.join(sorted(missing))))
    return page


KEEP = {'SKURX', 'SYSTEMS', 'SKURX SYSTEMS', 'info@skurx.es', 'Javier Escudero Cano', 'Web3Forms', 'Microsoft 365', 'GitHub Pages', 'www.aepd.es', 'Fini', 'Auditable'} | set(LANG_NAMES.values())


# ------------------------------------------------------------------ páginas de sector
def sector_pages(lang, S, UI, CONTROL, pre, close, dialog, head0, sw_for, alt_for, talk, audit, priv_href, fini):
    for s in S:
        plural = s['fini'].split('|')[2]
        title = UI['title'].format(plural=plural)
        desc = re.sub('<[^>]+>', '', s['lead']).split('. ')[0].rstrip('.') + '.'
        mdesc = UI['desc'].format(plural=plural, desc=desc)
        url = alt_for(s)[lang]
        head = head0.replace(re.search(r'<title>.*?</title>', head0).group(0), '<title>%s</title>' % title)
        head = re.sub(r'<meta name="description" content="[^"]*">', '<meta name="description" content="%s">' % H.escape(mdesc), head)
        head = re.sub(r'<link rel="canonical" href="[^"]*">', '<link rel="canonical" href="%s">' % url, head)
        head = re.sub(r'<meta property="og:url" content="[^"]*">', '<meta property="og:url" content="%s">' % url, head)
        head = re.sub(r'<meta property="og:title" content="[^"]*">', '<meta property="og:title" content="%s">' % title, head)
        head = re.sub(r'<meta property="og:description" content="[^"]*">', '<meta property="og:description" content="%s">' % H.escape(mdesc), head)
        pains = ''.join('<article class="pain"><small>%02d</small><h3>%s</h3><p>%s</p><div class="fix"><b>%s · %s</b><p>%s</p></div></article>' % (i + 1, t, d, UI['fix'], k.upper(), f) for i, (t, d, f, k) in enumerate(s['pains']))
        F = s['flow']
        flow = ''.join('<li%s><b>%s</b>%s</li>' % (' class="result"' if i == len(F) - 1 else '', t, x) for i, (t, x) in enumerate(F))
        fe = s.get('feature')
        feature = ''
        if fe:
            feature = ('<section class="sector-feature"><div class="sf-copy"><p class="eyebrow dark">%s</p><h2>%s</h2><p>%s</p><ul>%s</ul></div>'
                       '<figure class="sf-art"><div class="ba-frame" style="--pos:50%%"><img src="%sreforma-antes.webp" width="1586" height="992" alt="%s" loading="lazy">'
                       '<div class="ba-after"><img src="%sreforma-despues.webp" width="1586" height="992" alt="%s" loading="lazy"></div>'
                       '<span class="ba-tag ba-tag-a">%s</span><span class="ba-tag ba-tag-d">%s</span><span class="ba-handle" aria-hidden="true"></span>'
                       '<input type="range" min="0" max="100" value="50" aria-label="%s"></div><figcaption>%s</figcaption></figure>'
                       '<script>document.querySelectorAll(".ba-frame input").forEach(function(i){var f=i.parentNode;function u(){var v=+i.value;f.style.setProperty("--pos",v+"%%");f.classList.toggle("ba-solo-antes",v>=85);f.classList.toggle("ba-solo-despues",v<=15)}i.addEventListener("input",u);u()});</script></section>'
                       ) % (fe['eyebrow'], fe['h2'], fe['p'], ''.join('<li>%s</li>' % i for i in fe['items']), pre, UI['ba_before_alt'], pre, UI['ba_after_alt'],
                            UI['ba_before'], UI['ba_after'], UI['ba_aria'], UI['ba_caption'])
        if fini:
            talk_a = '<a class="header-contact" href="#auditoria" data-contact-open aria-haspopup="dialog" aria-controls="panel-contacto">'
            cta_a = '<a class="gold-link" href="#auditoria" data-contact-open aria-haspopup="dialog" aria-controls="panel-contacto">'
            aud_a = '<a class="gold-link" href="#auditoria" data-contact-open data-fini-intent="auditoria" aria-haspopup="dialog" aria-controls="panel-contacto">'
            body_attr = ' data-fini-sector="%s"' % s['fini']
        else:
            talk_a = '<a class="header-contact" href="%s">' % talk
            cta_a = '<a class="gold-link" href="%s">' % talk
            aud_a = '<a class="gold-link" href="%s">' % audit
            body_attr = ''
        L = UI['labels']
        home = '../index.html'
        body = (f'<body{body_attr}><a class="skip-link" href="#contenido">{L["skip"]}</a><header class="site-header"><a class="brand-lockup" href="{home}" aria-label="{L["home_aria"]}"><span class="brand-name"><strong>SKURX</strong><span>SYSTEMS</span></span><span class="brand-tagline">{L["tagline"]}</span></a>'
                f'<nav aria-label="{L["nav_aria"]}"><a href="{home}#inicio">{L["nav"][0]}</a><a href="{home}#que-hacemos">{L["nav"][1]}</a><a href="{home}#como-lo-hacemos">{L["nav"][2]}</a><a href="{home}#sectores">{L["nav"][3]}</a></nav>'
                f'<div class="header-actions">{sw_for(s)}{talk_a}<span class="contact-label">{L["talk"]}</span><span class="contact-arrow" aria-hidden="true">↗</span></a></div></header>'
                '<script>if("scrollRestoration" in history)history.scrollRestoration="manual";if(!location.hash)window.scrollTo(0,0);</script><main id="contenido">\n'
                f'<section class="sector-hero"><p class="crumb"><a href="{home}#sectores">{UI["crumb"]}</a> · {s["name"].upper()}</p><h1>{s["h1"]}</h1><p class="lead">{s["lead"]}</p>{cta_a}{s["cta"]} <span aria-hidden="true">→</span></a></section>\n'
                f'<section class="pains"><p class="eyebrow dark">{UI["pains_eyebrow"]}</p><h2>{s["h2"]}</h2><div class="pain-grid">{pains}</div></section>\n'
                f'{feature}<section class="sector-flowsec"><p class="eyebrow">{UI["flow_eyebrow"]}</p><h2>{UI["flow_h2"]}</h2><p class="note">{UI["flow_note"]}</p><ul class="sector-flow">{flow}</ul></section>\n'
                f'<section class="sector-audit" id="auditoria"><p class="eyebrow dark">{UI["control_eyebrow"]}</p><div class="process-control sector-control">'
                + ''.join('<article><h3>%s</h3><p>%s</p></article>' % c for c in CONTROL) +
                f'</div><div class="process-audit"><div><p class="eyebrow">{L["first_step"]}</p><h3>{UI["audit_h3"].format(plural=plural)}</h3><p>{s["audit"]} {UI["audit_tail"]}</p></div>{aud_a}{UI["audit_btn"]} <span aria-hidden="true">→</span></a></div></section>\n'
                f'{close}<div class="back-home"><a href="{home}"><span aria-hidden="true">←</span> {L["back"]}</a></div></main><footer><p>{L["footer"]}<a class="footer-legal" href="{priv_href}"><span class="sep" aria-hidden="true">· </span>{L["privacy"]}</a></p></footer>{dialog}{nav_snippet(pre, L["next"], L["top"])}</body></html>')
        page = set_alternates(head, alt_for(s)) + body
        open(os.path.join(sector_dir(lang), s['slug'] + '.html'), 'w').write(page)


def sector_dir(lang):
    return 'sectores' if lang == 'es' else os.path.join(LANG_MOD[lang].DIR, LANG_MOD[lang].SECTORS_DIR)


# ------------------------------------------------------------------ construcción
LANG_MOD = {l: importlib.import_module('i18n_' + l) for l in LANGS}
DATA = {l: importlib.import_module('sectores_data_' + l).S for l in LANGS}
by_es = {l: {s['es_slug']: s for s in DATA[l]} for l in LANGS}


def sector_urls(es_slug):
    u = {'es': '%s/sectores/%s.html' % (SITE, es_slug)}
    for l in LANGS:
        M = LANG_MOD[l]
        u[l] = '%s/%s/%s/%s.html' % (SITE, M.DIR, M.SECTORS_DIR, by_es[l][es_slug]['slug'])
    return u


home_urls = {'es': SITE + '/'}
priv_urls = {'es': SITE + '/privacidad.html'}
for l in LANGS:
    home_urls[l] = '%s/%s/' % (SITE, LANG_MOD[l].DIR)
    priv_urls[l] = '%s/%s/%s' % (SITE, LANG_MOD[l].DIR, LANG_MOD[l].PRIVACY)

# 1. Portada y privacidad en español: selector de idioma y alternates
idx = open('index.html').read()
idx = set_switcher(idx, switcher('Idioma', 'index.html', [(l, '%s/index.html' % LANG_MOD[l].DIR) for l in LANGS], 'es'))
idx = set_alternates(idx, home_urls)
priv = open('privacidad.html').read()
priv = set_switcher(priv, switcher('Idioma', 'privacidad.html', [(l, '%s/%s' % (LANG_MOD[l].DIR, LANG_MOD[l].PRIVACY)) for l in LANGS], 'es'))
priv = set_alternates(priv, priv_urls)

# «Más sectores» de la portada desde los datos
extra = [s for s in S_ES if s['slug'] not in ('inmobiliarias', 'gestorias', 'automocion')]
lis = ''.join('<li><a href="sectores/%s.html">%s<span aria-hidden="true">→</span></a></li>' % (s['slug'], s['name']) for s in extra)
idx = re.sub(r'(<p class="eyebrow" id="accede-sector">[^<]*</p><ul>).*?(</ul>)', lambda m: m.group(1) + lis + m.group(2), idx, flags=re.S)
def set_back(page, href, text, arrow):
    page = re.sub(r'<div class="back-home">.*?</div>', '', page, flags=re.S)
    return page.replace('</main>', '<div class="back-home"><a href="%s"><span aria-hidden="true">%s</span> %s</a></div></main>' % (href, arrow, text), 1)


def nav_snippet(pre, nxt, top):
    return ('<button class="next-section" type="button" aria-label="%s" data-next-label="%s" data-top-label="%s"><span aria-hidden="true"></span></button>'
            '<script src="%snav.js?v=20260927a" defer></script>') % (nxt, nxt, top, pre)


def set_nav(page, snippet):
    page = re.sub(r'<button class="next-section".*?</button><script src="[^"]*nav\.js[^"]*" defer></script>', '', page, flags=re.S)
    return page.replace('</body>', snippet + '</body>', 1)


idx = set_nav(idx, nav_snippet('', 'Siguiente sección', 'Volver arriba'))
idx = set_back(idx, '#inicio', 'Volver arriba', '↑')
priv = set_back(priv, 'index.html', 'Volver a la página principal', '←')
open('index.html', 'w').write(idx)
open('privacidad.html', 'w').write(priv)

# 2. Páginas de sector en español
head0 = idx.split('<body>')[0]
head0 = re.sub(r'<script type="application/ld\+json">.*?</script>', '', head0)
head0 = re.sub(r'<link rel="alternate" hreflang="[^"]*" href="[^"]*">', '', head0)
for a in ['href="favicon.svg"', 'href="favicon-32.png"', 'href="apple-touch-icon.png"', 'href="hero-bg.webp"']:
    head0 = head0.replace(a, a.replace('href="', 'href="../'))
head0 = head0.replace('href="styles.css?', 'href="../styles.css?').replace('src="fini.js?', 'src="../fini.js?')
dialog_es = idx[idx.index('<dialog'):idx.index('</dialog>') + 9].replace('src="fini-avatar.svg"', 'src="../fini-avatar.svg"').replace('<a href="/privacidad.html" target="_blank"', '<a href="../privacidad.html" target="_blank"')
close_es = re.search(r'<section class="contact" id="contacto">.*?</section>', idx, re.S).group(0)
UI_ES = dict(SECTOR_UI_ES, labels=dict(skip='Saltar al contenido', home_aria='SKURX SYSTEMS, inicio', tagline='CAPACIDAD LIBERADA', nav_aria='Navegación principal',
                                        nav=['Quiénes somos', 'Qué hacemos', 'Cómo lo hacemos', 'Sectores'], talk='Hablemos', first_step='EL PRIMER PASO',
                                        footer='SKURX SYSTEMS - AUTOMATIZACIÓN DE RECURSOS', privacy='Privacidad', back='Volver a la página principal', next='Siguiente sección', top='Volver arriba'))


def sw_es(s):
    return switcher('Idioma', '%s.html' % s['slug'], [(l, '../%s/%s/%s.html' % (LANG_MOD[l].DIR, LANG_MOD[l].SECTORS_DIR, by_es[l][s['slug']]['slug'])) for l in LANGS], 'es')


sector_pages('es', S_ES, UI_ES, CONTROL_ES, '../', close_es, dialog_es, head0, sw_es, lambda s: sector_urls(s['slug']), None, None, '../privacidad.html', True)

# 3. Otros idiomas
for l in LANGS:
    M = LANG_MOD[l]
    T = dict(M.COMMON, **M.HOME)
    os.makedirs(os.path.join(M.DIR, M.SECTORS_DIR), exist_ok=True)
    # nombres de sector (listado y tarjetas) y enlaces a sus páginas
    for s in S_ES:
        T[s['name']] = by_es[l][s['slug']]['name']

    # --- portada
    p = idx
    p = p.replace('<html lang="es">', '<html lang="%s"%s>' % (l, ' dir="rtl"' if getattr(M, 'RTL', False) else ''))
    p = re.sub(r'<script type="application/ld\+json">.*?</script>', lambda m: m.group(0).replace(
        'SKURX SYSTEMS libera la capacidad que las empresas pierden en trabajo manual con automatización, conexión de herramientas e IA aplicada. Para empresas de toda España.',
        T['SKURX SYSTEMS libera la capacidad que las empresas pierden en trabajo manual con automatización, conexión de herramientas e IA aplicada. Para empresas de toda España.'])
        .replace('"url":"https://skurx.es/"', '"url":"%s"' % home_urls[l]).replace('"España"', '"%s"' % M.JSONLD['country']).replace('"Automatización de Recursos","Automatización de procesos","Inteligencia artificial aplicada","Integración de herramientas"', ','.join('"%s"' % k for k in M.JSONLD['knows'])), p, flags=re.S)
    p = p.replace('<meta property="og:locale" content="es_ES">', '<meta property="og:locale" content="%s">' % M.LOCALE)
    p = re.sub(r'<link rel="canonical" href="[^"]*">', '<link rel="canonical" href="%s">' % home_urls[l], p)
    p = re.sub(r'<meta property="og:url" content="[^"]*">', '<meta property="og:url" content="%s">' % home_urls[l], p)
    # sin Fini por ahora: contacto por correo
    p = re.sub(r'<script src="fini\.js[^"]*" defer></script>', '', p)
    p = re.sub(r'<dialog.*?</dialog>', '', p, flags=re.S)
    p = re.sub(r'<a class="header-contact" href="#contacto"[^>]*>', '<a class="header-contact" href="%s">' % M.CONTACT_TALK, p)
    p = re.sub(r'<a class="gold-link" href="#contacto"[^>]*data-fini-intent="auditoria"[^>]*>', '<a class="gold-link" href="%s">' % M.CONTACT_AUDIT, p)
    # rutas relativas desde la subcarpeta
    for a in ['favicon.svg', 'favicon-32.png', 'apple-touch-icon.png', 'hero-bg.webp']:
        p = p.replace('href="%s"' % a, 'href="../%s"' % a)
    p = p.replace('href="styles.css?', 'href="../styles.css?').replace('src="nav.js?', 'src="../nav.js?')
    p = p.replace('srcset="capacity-funnel-mobile.svg"', 'srcset="capacity-funnel-mobile-%s.svg"' % l).replace('src="capacity-funnel.svg"', 'src="capacity-funnel-%s.svg"' % l)
    p = p.replace('href="/privacidad.html"', 'href="%s"' % M.PRIVACY)
    p = re.sub(r'href="sectores/([a-z-]+)\.html"', lambda m: 'href="%s/%s.html"' % (M.SECTORS_DIR, by_es[l][m.group(1)]['slug']), p)
    p = set_switcher(p, switcher(M.COMMON['Idioma'], '../index.html', [(x, ('index.html' if x == l else '../%s/index.html' % LANG_MOD[x].DIR)) for x in LANGS], l))
    p = translate(p, T, 'portada ' + l)
    open(os.path.join(M.DIR, 'index.html'), 'w').write(p)
    home_l = p

    # --- ilustración
    for src in ['capacity-funnel.svg', 'capacity-funnel-mobile.svg']:
        svg = open(src).read()
        svg = re.sub(r'(<text[^>]*>)([^<]+)', lambda m: m.group(1) + M.SVG.get(m.group(2).strip(), m.group(2)), svg)
        open(os.path.join(M.DIR, src.replace('.svg', '-%s.svg' % l)), 'w').write(svg)

    # --- privacidad
    q = priv.replace('<html lang="es">', '<html lang="%s"%s>' % (l, ' dir="rtl"' if getattr(M, 'RTL', False) else ''))
    for a in ['favicon.svg', 'favicon-32.png', 'apple-touch-icon.png']:
        q = q.replace('href="%s"' % a, 'href="../%s"' % a).replace('href="/%s"' % a, 'href="../%s"' % a)
    q = q.replace('href="styles.css?', 'href="../styles.css?').replace('href="/styles.css?', 'href="../styles.css?')
    q = re.sub(r'<link rel="canonical" href="[^"]*">', '<link rel="canonical" href="%s">' % priv_urls[l], q)
    q = re.sub(r'<meta property="og:url" content="[^"]*">', '<meta property="og:url" content="%s">' % priv_urls[l], q)
    q = q.replace('href="/"', 'href="index.html"').replace('href="index.html" aria-label', 'href="index.html" aria-label')
    q = set_switcher(q, switcher(M.COMMON['Idioma'], '../privacidad.html', [(x, M.PRIVACY if x == l else '../%s/%s' % (LANG_MOD[x].DIR, LANG_MOD[x].PRIVACY)) for x in LANGS], l))
    q = translate(q, dict(M.COMMON, **M.PRIVACY_TEXT), 'privacidad ' + l)
    open(os.path.join(M.DIR, M.PRIVACY), 'w').write(q)

    # --- sectores
    h0 = home_l.split('<body>')[0]
    h0 = re.sub(r'<script type="application/ld\+json">.*?</script>', '', h0)
    h0 = re.sub(r'<link rel="alternate" hreflang="[^"]*" href="[^"]*">', '', h0)
    h0 = h0.replace('href="../', 'href="../../').replace('<link rel="preload" as="image" href="../../hero-bg.webp" type="image/webp">', '<link rel="preload" as="image" href="../../hero-bg.webp" type="image/webp">')
    close_l = re.search(r'<section class="contact" id="contacto">.*?</section>', home_l, re.S).group(0)
    Tn = M.COMMON
    UI = dict(M.SECTOR_UI, labels=dict(skip=Tn['Saltar al contenido'], home_aria=Tn['SKURX SYSTEMS, inicio'], tagline=Tn['CAPACIDAD LIBERADA'], nav_aria=Tn['Navegación principal'],
                                       nav=[Tn['Quiénes somos'], Tn['Qué hacemos'], Tn['Cómo lo hacemos'], Tn['Sectores']], talk=Tn['Hablemos'],
                                       first_step=M.HOME['EL PRIMER PASO'], footer=Tn['SKURX SYSTEMS - AUTOMATIZACIÓN DE RECURSOS'], privacy=Tn['Privacidad'], back=Tn['Volver a la página principal'], next=Tn['Siguiente sección'], top=Tn['Volver arriba']))
    CONTROL = [(M.HOME[a], M.HOME[b]) for a, b in CONTROL_ES]

    def sw_l(s, l=l, M=M):
        return switcher(M.COMMON['Idioma'], '../../sectores/%s.html' % s['es_slug'], [(x, ('%s.html' % s['slug']) if x == l else '../../%s/%s/%s.html' % (LANG_MOD[x].DIR, LANG_MOD[x].SECTORS_DIR, by_es[x][s['es_slug']]['slug'])) for x in LANGS], l)

    sector_pages(l, DATA[l], UI, CONTROL, '../../', close_l, '', h0, sw_l, lambda s: sector_urls(s['es_slug']), M.CONTACT_TALK, M.CONTACT_AUDIT, '../' + M.PRIVACY, False)

# 4. sitemap
urls = [home_urls['es'], priv_urls['es']] + ['%s/sectores/%s.html' % (SITE, s['slug']) for s in S_ES]
for l in LANGS:
    urls += [home_urls[l], priv_urls[l]] + [sector_urls(s['slug'])[l] for s in S_ES]
import datetime
today = datetime.date.today().isoformat()
open('sitemap.xml', 'w').write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' +
                               ''.join('  <url><loc>%s</loc><lastmod>%s</lastmod></url>\n' % (u, today) for u in urls) + '</urlset>\n')
print('OK: español + %s · %d páginas de sector por idioma · sitemap con %d URLs' % (', '.join(LANGS), len(S_ES), len(urls)))
