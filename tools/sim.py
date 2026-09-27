# Clientes simulados que responden a lo que Fini pregunta de verdad.
import json, sys, os, re
from playwright.sync_api import sync_playwright
BASE='http://localhost:8770'
Q=[('confirm',r'¿Está todo bien\?|Escríbeme lo que quieras añadir'),('horario',r'momento del día|te venga mejor'),('contacto',r'email o un teléfono|email \(algo como|dejarme un email|me dejas un email|me lo escribes de nuevo|En qué teléfono'),
   ('nombre',r'¿Cómo te llamas|tu nombre|Me dices tu nombre'),('urgencia',r'os preocupa ya|explorando con calma'),
   ('empresa',r'a qué se dedica|a qué os dedicáis|cuántas personas'),('tiempo',r'cuánto tiempo|pocas horas a la semana'),
   ('herramientas',r'herramienta|programas o aplicaciones'),
   ('detalle',r'cómo os llega|quién se encarga|por dónde os suelen|lo hacéis a mano|qué suele quedarse|qué pasa cuando|más de detalle|cómo es ese trabajo|cómo gestionáis|cómo lo hacéis|cómo funciona ahora'),
   ('problema',r'qué es lo que más tiempo|qué parte del trabajo|cuéntame tu caso|me cuentas un poco más|qué te trae|en qué podemos')]
def classify(text):
    for k,rx in Q:
        if re.search(rx,text,re.I): return k
    return None
def run(personas, only=None, show=True):
    res={}
    with sync_playwright() as p:
        b=p.chromium.launch(); ctx=b.new_context(viewport={'width':390,'height':844}, reduced_motion='reduce'); sent=[]
        # Azar reproducible: así dos ejecuciones se pueden comparar línea a línea.
        ctx.add_init_script("(function(){var s=42;Math.random=function(){s=(s*16807)%2147483647;return (s-1)/2147483646;};})()")
        ctx.route('**/api.web3forms.com/**', lambda r: (sent.append(json.loads(r.request.post_data or '{}')), r.fulfill(status=200, body='{"success":true}', headers={'Content-Type':'application/json'})))
        for name,P in personas.items():
            if only and not any(o in name for o in only): continue
            page,opener=P.get('open',('/','.header-contact'))
            pg=ctx.new_page(); errs=[]; pg.on('pageerror',lambda e: errs.append(str(e)))
            pg.goto(BASE+page); pg.evaluate("localStorage.clear();sessionStorage.clear()"); pg.reload(); pg.locator(opener).first.evaluate('e=>e.click()')
            def idle():
                last=-1; same=0
                for _ in range(300):
                    n=pg.locator('.chat-log .chat-msg').count(); busy=pg.locator('.chat-log .typing').count()
                    same = same+1 if (n==last and not busy) else 0
                    if same>=3: return
                    last=n; pg.wait_for_timeout(50)
            def fini_since(k):
                els=pg.locator('.chat-log .chat-msg').all()[k:]
                return [e.inner_text().replace('\n',' | ') for e in els if 'from-fini' in (e.get_attribute('class') or '')]
            idle(); seen=0; asked={}; issues=[]; queue={k:(list(v) if isinstance(v,list) else [v]) for k,v in P['a'].items()}
            extras=list(P.get('extra',[])); turn=0; done=False
            while turn<24:
                msgs=fini_since(seen); seen=pg.locator('.chat-log .chat-msg').count()
                blob=' '.join(msgs)
                if re.search(r'Se lo he pasado al equipo|Modo prueba',blob): done=True; break
                if re.search(r'Cuando quieras retomarlo|no hace falta que lo dejes ahora',blob) and 'contacto' in asked and asked['contacto']>=1 and not queue.get('contacto'): break
                last=msgs[-1] if msgs else ''
                k=classify(last) or classify(blob)
                if extras and extras[0][0]==turn: msg=extras.pop(0)[1]
                elif k is None:
                    issues.append('SIN PREGUNTA RECONOCIBLE: '+last[:90]); break
                else:
                    asked[k]=asked.get(k,0)+1
                    if asked[k]>(3 if k=='confirm' else 2): issues.append('PREGUNTA REPETIDA: '+k); break
                    q=queue.get(k) or []
                    v=P['a'].get(k,'no sé'); msg=q.pop(0) if q else ((v[-1] if v else 'no sé') if isinstance(v,list) else (v or 'no sé'))
                    if not q and isinstance(v,list) and not v: issues.append('PREGUNTA NO ESPERADA: '+k)
                pg.fill('#chat-input',msg); pg.keyboard.press('Enter'); idle(); turn+=1
            lines=[]
            for el in pg.locator('.chat-log .chat-msg').all():
                c=el.get_attribute('class') or ''; lines.append(('U: ' if 'from-user' in c else 'F: ')+el.inner_text().replace('\n',' | '))
            clar=sum(1 for l in lines if l.startswith('F:') and re.search(r'no te he entendido|no me he explicado|no sé si te he seguido|no lo he entendido|Creo que no te he entendido',l))
            if errs: issues.append('ERROR JS: '+'; '.join(errs))
            if not done: issues.append('NO TERMINA')
            res[name]=dict(lines=lines,issues=issues,clar=clar,turns=turn,done=done); pg.close()
        b.close()
    if show:
        for n,r in res.items():
            print('\n=== %s  [%s | aclaraciones:%d | turnos:%d]'%(n,'OK' if r['done'] and not r['issues'] else 'REVISAR',r['clar'],r['turns']))
            for i in r['issues']: print('  !!',i)
            print('\n'.join(r['lines']))
        ok=sum(1 for r in res.values() if r['done'] and not r['issues'])
        print('\nRESUMEN: %d/%d terminan sin incidencias; aclaraciones totales: %d'%(ok,len(res),sum(r['clar'] for r in res.values())))
    return res
if __name__=='__main__':
    sys.path.insert(0,os.path.dirname(__file__)); from personas import PERSONAS
    run(PERSONAS, sys.argv[1:] or None)
