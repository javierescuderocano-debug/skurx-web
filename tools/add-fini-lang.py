"""Añade Fini (fini-i18n.js) a las páginas de EN, CA, FR, DE y NL.

- Inserta el panel de chat (mismo HTML que la versión en español, con textos traducidos).
- Convierte los botones «Hablemos» y «Solicitar auditoría» (hoy enlaces mailto) en aperturas de Fini.
  El enlace de correo visible (info@skurx.es) se mantiene.
- Es idempotente: si la página ya tiene el panel, no la toca.
Uso: python3 tools/add-fini-lang.py
"""
import pathlib, re

ROOT = pathlib.Path(__file__).resolve().parent.parent
VERSION = '20260930a'

UI = {
    'en': dict(role='Virtual assistant of SKURX SYSTEMS', close='Close conversation', log='Conversation with Fini',
               quick='Quick replies', label='Type your message', ph='Type here…', send='Send',
               note='What you write here will be reviewed by the SKURX SYSTEMS team to reply to you.', priv='Privacy', privfile='privacy.html'),
    'ca': dict(role='Assistent virtual de SKURX SYSTEMS', close='Tanca la conversa', log='Conversa amb la Fini',
               quick='Respostes ràpides', label='Escriu el teu missatge', ph='Escriu aquí…', send='Envia',
               note='El que escriguis aquí ho revisarà l’equip de SKURX SYSTEMS per respondre’t.', priv='Privacitat', privfile='privacitat.html'),
    'fr': dict(role='Assistante virtuelle de SKURX SYSTEMS', close='Fermer la conversation', log='Conversation avec Fini',
               quick='Réponses rapides', label='Écrivez votre message', ph='Écrivez ici…', send='Envoyer',
               note='Ce que vous écrivez ici sera lu par l’équipe de SKURX SYSTEMS pour vous répondre.', priv='Confidentialité', privfile='confidentialite.html'),
    'de': dict(role='Virtuelle Assistentin von SKURX SYSTEMS', close='Gespräch schließen', log='Gespräch mit Fini',
               quick='Schnellantworten', label='Nachricht schreiben', ph='Hier schreiben…', send='Senden',
               note='Was Sie hier schreiben, liest das Team von SKURX SYSTEMS, um Ihnen zu antworten.', priv='Datenschutz', privfile='datenschutz.html'),
    'nl': dict(role='Virtuele assistent van SKURX SYSTEMS', close='Gesprek sluiten', log='Gesprek met Fini',
               quick='Snelle antwoorden', label='Typ je bericht', ph='Typ hier…', send='Versturen',
               note='Wat je hier schrijft, wordt gelezen door het team van SKURX SYSTEMS om je te antwoorden.', priv='Privacy', privfile='privacy.html'),
}

DIALOG = ('<dialog class="contact-panel chat-panel" id="panel-contacto" aria-labelledby="fini-nombre">'
          '<header class="chat-head"><img class="chat-avatar" src="{up}fini-avatar.svg" width="44" height="44" alt="">'
          '<div><p class="chat-name" id="fini-nombre">Fini</p><p class="chat-role">{role}</p></div>'
          '<button class="panel-close" type="button" data-contact-close aria-label="{close}"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6 6l12 12M18 6L6 18"/></svg></button></header>'
          '<div class="chat-log" role="log" aria-live="polite" aria-label="{log}" tabindex="-1"></div>'
          '<div class="chat-quick" aria-label="{quick}"></div>'
          '<form class="chat-form" autocomplete="off"><label class="visually-hidden" for="chat-input">{label}</label>'
          '<textarea id="chat-input" rows="1" maxlength="1200" placeholder="{ph}" enterkeyhint="send"></textarea>'
          '<button class="chat-send" type="submit" aria-label="{send}"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12h13M13 6l6 6-6 6"/></svg></button></form>'
          '<p class="chat-privacy">{note} <a href="{langup}{privfile}" target="_blank" rel="noopener">{priv}</a></p></dialog>')

OPEN = 'href="#contacto" data-contact-open{extra} aria-haspopup="dialog" aria-controls="panel-contacto"'
AUDIT_WORDS = re.compile(r'Audit|Auditoria|Erstanalyse|Startaudit', re.I)


def patch(path, lang):
    html = path.read_text(encoding='utf-8')
    if 'id="panel-contacto"' in html:
        return False
    depth = len(path.relative_to(ROOT / lang).parts) - 1  # 0 = index, 1 = sector page
    up = '../' * (depth + 1)          # to site root
    langup = '../' * depth            # to the language folder
    ui = UI[lang]

    def fix(m):
        tag = m.group(0)
        cls = m.group(1)
        href = m.group(2)
        if cls not in ('header-contact', 'gold-link'):
            return tag
        extra = ' data-fini-intent="auditoria"' if cls == 'gold-link' and AUDIT_WORDS.search(href.replace('%20', ' ')) else ''
        return tag.replace('href="%s"' % href, OPEN.format(extra=extra))

    html = re.sub(r'<a class="([\w-]+)" href="(mailto:[^"]*)"', fix, html)
    script = '<script src="%sfini-i18n.js?v=%s" defer></script>' % (up, VERSION)
    html = html.replace('</head>', script + '</head>', 1)
    dialog = DIALOG.format(up=up, langup=langup, **ui)
    if '<button class="next-section"' in html:
        html = html.replace('<button class="next-section"', dialog + '<button class="next-section"', 1)
    else:
        html = html.replace('</body>', dialog + '</body>', 1)
    path.write_text(html, encoding='utf-8')
    return True


if __name__ == '__main__':
    changed = 0
    for lang in UI:
        for p in sorted((ROOT / lang).rglob('*.html')):
            if p.name == UI[lang]['privfile']:
                continue
            if patch(p, lang):
                changed += 1
                print('ok', p.relative_to(ROOT))
    print(changed, 'páginas')
