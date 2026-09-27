# Nederlandse teksten van de website. Sleutel = exacte Spaanse tekst; waarde = vertaling.
# Om een taal toe te voegen: dit bestand kopiëren als i18n_<code>.py en de waarden vertalen.

LANG = 'nl'
LOCALE = 'nl_NL'
DIR = 'nl'                      # carpeta donde se publica
SECTORS_DIR = 'sectoren'        # carpeta de las páginas de sector dentro de DIR
PRIVACY = 'privacy.html'
RTL = False                     # True solo para idiomas de derecha a izquierda (árabe)
JSONLD = {'country': 'Spanje', 'knows': ['Automatisering van Middelen', 'Procesautomatisering', 'Toegepaste kunstmatige intelligentie', 'Koppeling van tools']}

# Contacto mientras Fini no esté disponible en este idioma
CONTACT_TALK = "mailto:info@skurx.es?subject=Laten%20we%20praten%20-%20SKURX%20SYSTEMS"
CONTACT_AUDIT = "mailto:info@skurx.es?subject=Operationele%20Startaudit%20-%20SKURX%20SYSTEMS"

# ---------------------------------------------------------------- Comunes
COMMON = {
    'Volver a la página principal': 'Terug naar de homepage',
    'Volver arriba': 'Terug naar boven',
    'Saltar al contenido': 'Naar de inhoud',
    'CAPACIDAD LIBERADA': 'VRIJGEMAAKTE CAPACITEIT',
    'Quiénes somos': 'Over ons',
    'Qué hacemos': 'Wat we doen',
    'Cómo lo hacemos': 'Onze aanpak',
    'Sectores': 'Sectoren',
    'Hablemos': 'Contact',
    'SKURX SYSTEMS - AUTOMATIZACIÓN DE RECURSOS': 'SKURX SYSTEMS - AUTOMATISERING VAN MIDDELEN',
    'Privacidad': 'Privacy',
    'El trabajo bien hecho': 'Goed werk',
    'no hace ruido.': 'maakt geen lawaai.',
    'Todo sigue en marcha, aunque ya no quede nadie en la oficina.': 'Alles blijft doorlopen, ook als er niemand meer op kantoor is.',
    'SKURX SYSTEMS, inicio': 'SKURX SYSTEMS, home',
    'Navegación principal': 'Hoofdnavigatie',
    'Idioma': 'Taal',
}

# ---------------------------------------------------------------- Portada
HOME = {
    'SKURX SYSTEMS | Automatización de Recursos': 'SKURX SYSTEMS | Automatisering van Middelen',
    'SKURX SYSTEMS libera la capacidad que las empresas pierden en trabajo manual con automatización, conexión de herramientas e IA aplicada. Para empresas de toda España.':
        'SKURX SYSTEMS maakt de capaciteit vrij die bedrijven verliezen aan handwerk, met automatisering, koppeling van tools en toegepaste AI. Voor bedrijven in heel Spanje.',
    'SKURX SYSTEMS — Comprender antes de proponer.': 'SKURX SYSTEMS — Eerst begrijpen, dan voorstellen.',
    'AUTOMATIZACIÓN DE RECURSOS': 'AUTOMATISERING VAN MIDDELEN',
    'Comprender antes de proponer.': 'Eerst begrijpen, dan voorstellen.',
    'La mayoría de las empresas no necesitan más herramientas. Necesitan saber dónde se les escapa el tiempo, la información y la atención.':
        'De meeste bedrijven hebben geen extra tools nodig. Ze moeten weten waar hun tijd, informatie en aandacht weglekken.',
    'SKURX SYSTEMS identifica dónde se pierde capacidad y la convierte en sistemas de trabajo más claros, conectados y eficientes.':
        'SKURX SYSTEMS brengt in kaart waar capaciteit verloren gaat en zet die om in duidelijkere, gekoppelde en efficiëntere manieren van werken.',
    'Tareas manuales': 'Handmatige taken',
    'Información dispersa': 'Versnipperde informatie',
    'Herramientas aisladas': 'Losse tools',
    'Seguimiento pendiente': 'Opvolging die blijft liggen',
    'Datos copiados a mano': 'Handmatig overgetypte data',
    'Dependencia de personas': 'Afhankelijk van personen',
    'QUÉ HACEMOS': 'WAT WE DOEN',
    'De la fricción': 'Van frictie',
    'a la': 'naar',
    'capacidad.': 'capaciteit.',
    'Detectamos dónde pierde capacidad tu empresa y la liberamos con automatización, herramientas conectadas e inteligencia artificial aplicada donde tiene sentido.':
        'We sporen op waar je bedrijf capaciteit verliest en maken die vrij met automatisering, gekoppelde tools en toegepaste kunstmatige intelligentie waar dat zinvol is.',
    'Flujos de trabajo dispersos que convergen en capacidad real.': 'Losse werkstromen die samenkomen in echte capaciteit.',
    'NUESTROS SERVICIOS': 'ONZE DIENSTEN',
    'La herramienta viene después.': 'De tool komt daarna.',
    'Automatización': 'Automatisering',
    'Convertimos las tareas repetitivas en procesos automáticos, con las reglas que definimos contigo.':
        'We zetten terugkerende taken om in automatische processen, volgens regels die we samen met jou bepalen.',
    'IA aplicada': 'Toegepaste AI',
    'Para lo que una regla no resuelve: la IA potencia a tu equipo, no lo sustituye.':
        'Voor wat een regel niet oplost: AI versterkt je team, maar vervangt het niet.',
    'Conexión de herramientas': 'Koppeling van tools',
    'Conectamos tus herramientas para que la información pase de una a otra sin que nadie intervenga.':
        'We koppelen je tools, zodat informatie van de ene naar de andere gaat zonder dat iemand hoeft in te grijpen.',
    'CÓMO LO HACEMOS': 'ONZE AANPAK',
    'Primero comprender.': 'Eerst begrijpen.',
    'Después': 'Daarna',
    'intervenir.': 'ingrijpen.',
    'No partimos de una tecnología, sino de una pregunta: ¿dónde está perdiendo capacidad tu empresa y por qué?':
        'We beginnen niet bij een technologie, maar bij een vraag: waar verliest je bedrijf capaciteit, en waarom?',
    'Entender': 'Begrijpen',
    'Conocemos tu empresa desde dentro, observando cómo trabaja tu equipo cada día.':
        'We leren je bedrijf van binnenuit kennen door te kijken hoe je team elke dag werkt.',
    'Analizar': 'Analyseren',
    'Localizamos dónde se pierde tiempo, información o clientes potenciales, y por qué.':
        'We brengen in kaart waar tijd, informatie of potentiële klanten verloren gaan, en waarom.',
    'Proponer': 'Voorstellen',
    'Te decimos qué cambiaríamos y qué no merece la pena tocar.': 'We vertellen je wat we zouden veranderen en wat de moeite niet waard is.',
    'Implantar': 'Invoeren',
    'Lo ponemos en marcha, lo probamos contigo y lo ajustamos hasta que funcione como tu equipo necesita.':
        'We zetten het op, testen het met jou en stellen het bij tot het werkt zoals je team het nodig heeft.',
    'EL PRIMER PASO': 'DE EERSTE STAP',
    'Auditoría Operativa Inicial': 'Operationele Startaudit',
    'En una semana analizamos cómo trabaja tu empresa y te entregamos un mapa claro: qué consume capacidad, qué se puede automatizar y en qué orden. El informe es tuyo, decidas lo que decidas.':
        'In één week analyseren we hoe je bedrijf werkt en geven we je een helder overzicht: wat capaciteit kost, wat geautomatiseerd kan worden en in welke volgorde. Het rapport is van jou, wat je ook besluit.',
    'Solicitar auditoría': 'Audit aanvragen',
    'Documentado': 'Gedocumenteerd',
    'Cada flujo explicado en lenguaje claro.': 'Elke werkstroom uitgelegd in heldere taal.',
    'A nombre de tu empresa': 'Op naam van je bedrijf',
    'Cuentas, herramientas y datos son tuyos.': 'Accounts, tools en data zijn van jou.',
    'Auditable': 'Controleerbaar',
    'Puedes ver qué ha hecho cada automatización y cuándo.': 'Je kunt zien wat elke automatisering heeft gedaan en wanneer.',
    'Sin dependencia': 'Geen lock-in',
    'Si dejamos de trabajar juntos, todo sigue siendo tuyo.': 'Als we stoppen met samenwerken, blijft alles van jou.',
    'EJEMPLOS POR SECTOR': 'VOORBEELDEN PER SECTOR',
    'Cómo se ve en la práctica.': 'Zo ziet het er in de praktijk uit.',
    'Escenarios ilustrativos basados en situaciones habituales. Trabajamos con empresas de cualquier sector, en toda España.':
        'Illustratieve scenario\'s op basis van alledaagse situaties. We werken met bedrijven uit elke sector, in heel Spanje.',
    'INMOBILIARIAS': 'MAKELAARS',
    'Cada consulta sin respuesta es una visita que no ocurre.': 'Elke onbeantwoorde aanvraag is een bezichtiging die niet doorgaat.',
    'Entra una consulta desde un portal.': 'Er komt een aanvraag binnen via een woningportal.',
    'Recibe respuesta con la información del inmueble.': 'Die krijgt een antwoord met de gegevens van de woning.',
    'Queda registrada y asignada a un agente.': 'Ze wordt vastgelegd en toegewezen aan een makelaar.',
    'El agente empieza el día con el seguimiento preparado.': 'De makelaar begint de dag met de opvolging klaar.',
    'GESTORÍAS': 'ADMINISTRATIEKANTOREN',
    'Menos tiempo persiguiendo papeles. Más tiempo asesorando.': 'Minder tijd achter papieren aan. Meer tijd om te adviseren.',
    'Día 1': 'Dag 1',
    'Se pide al cliente la documentación que falta.': 'De klant krijgt een verzoek om de ontbrekende documenten.',
    'Día 3': 'Dag 3',
    'Si no ha llegado, sale un recordatorio.': 'Zijn ze er nog niet, dan gaat er een herinnering uit.',
    'Al llegar': 'Bij ontvangst',
    'Se clasifica y se archiva en su expediente.': 'Ze worden gesorteerd en in het klantdossier gearchiveerd.',
    'Listo': 'Klaar',
    'El gestor recibe el aviso: expediente completo.': 'De adviseur krijgt een melding: dossier compleet.',
    'AUTOMOCIÓN': 'AUTOBRANCHE',
    'Un interesado que espera es un coche que se vende en otro sitio.': 'Een koper die moet wachten, koopt zijn auto ergens anders.',
    'Consulta sobre un vehículo desde un portal.': 'Een aanvraag over een auto via een portal.',
    'Respuesta con ficha, precio y opción de cita.': 'Een antwoord met specificaties, prijs en de optie om een afspraak te maken.',
    'Se registra y se asigna a un comercial.': 'Ze wordt vastgelegd en toegewezen aan een verkoper.',
    'Día antes': 'Dag ervoor',
    'Recordatorio automático de la prueba o la visita.': 'Automatische herinnering aan de proefrit of het bezoek.',
    'MÁS SECTORES': 'MEER SECTOREN',
}

# ---------------------------------------------------------------- Privacidad
PRIVACY_TEXT = {
    'Política de privacidad | SKURX SYSTEMS': 'Privacyverklaring | SKURX SYSTEMS',
    'Cómo trata SKURX SYSTEMS los datos que compartes a través de skurx.es y de su asistente Fini.':
        'Hoe SKURX SYSTEMS omgaat met de gegevens die je deelt via skurx.es.',
    'Volver': 'Terug',
    'INFORMACIÓN LEGAL': 'JURIDISCHE INFORMATIE',
    'Política de privacidad': 'Privacyverklaring',
    'Última actualización: 26 de septiembre de 2026': 'Laatst bijgewerkt: 27 september 2026',
    'Quién es el responsable': 'Wie is verantwoordelijk',
    'El responsable del tratamiento de tus datos es ': 'De verwerkingsverantwoordelijke voor je gegevens is ',
    ', que desarrolla su actividad bajo el nombre comercial ': ', die handelt onder de naam ',
    '. Para cualquier cuestión sobre tus datos puedes escribir a ': '. Voor elke vraag over je gegevens kun je mailen naar ',
    'Qué datos tratamos': 'Welke gegevens we verwerken',
    'Solo los que tú decides compartir con nosotros:': 'Alleen de gegevens die je zelf met ons deelt:',
    'A través de Fini': 'Via Fini',
    ', el asistente de la web: tu nombre, la forma de contacto que elijas (correo o teléfono), tu horario preferido y lo que nos cuentes sobre tu empresa y tu situación, junto con la conversación completa.':
        ', de assistent van de website (voorlopig alleen in het Spaans): je naam, de contactwijze die je kiest (e-mail of telefoon), je voorkeurstijd en wat je ons vertelt over je bedrijf en je situatie, samen met het volledige gesprek.',
    'Por correo electrónico': 'Per e-mail',
    ': los datos que incluyas en tu mensaje.': ': de gegevens die je in je bericht opneemt.',
    'No te pedimos datos especialmente sensibles. Te rogamos que no los incluyas en la conversación.':
        'We vragen niet om bijzondere persoonsgegevens. Neem die alsjeblieft niet op in je berichten.',
    'Para qué los usamos': 'Waarvoor we ze gebruiken',
    'Para atender tu consulta, ponernos en contacto contigo y, si lo solicitas, preparar una propuesta. No los usamos para enviarte publicidad ni los vendemos o cedemos a terceros con fines comerciales.':
        'Om je vraag te beantwoorden, contact met je op te nemen en, als je daarom vraagt, een voorstel op te stellen. We gebruiken ze niet om je reclame te sturen, en we verkopen ze niet en geven ze niet door aan derden voor commerciële doeleinden.',
    'Base legal': 'Rechtsgrond',
    'Tratamos tus datos porque tú nos los envías voluntariamente para que te contactemos (tu consentimiento) y, cuando corresponde, para aplicar a petición tuya medidas previas a un posible contrato.':
        'We verwerken je gegevens omdat je ze ons vrijwillig stuurt zodat we contact met je opnemen (je toestemming) en, waar van toepassing, om op jouw verzoek stappen te zetten voorafgaand aan een mogelijke overeenkomst.',
    'Cuánto tiempo los conservamos': 'Hoe lang we ze bewaren',
    'El tiempo necesario para atender tu consulta. Si no llegamos a trabajar juntos, los eliminamos como máximo doce meses después del último contacto. Si iniciamos una relación profesional, los conservaremos mientras dure y durante los plazos que exija la ley.':
        'Zo lang als nodig is om je vraag te beantwoorden. Als we uiteindelijk niet samenwerken, verwijderen we ze uiterlijk twaalf maanden na het laatste contact. Als we een zakelijke relatie aangaan, bewaren we ze zolang die duurt en gedurende de termijnen die de wet voorschrijft.',
    'Quién más interviene': 'Wie er verder bij betrokken is',
    'Para que la web y el asistente funcionen nos apoyamos en proveedores que solo tratan los datos para prestarnos su servicio:':
        'Voor de werking van de website en de assistent maken we gebruik van leveranciers die de gegevens alleen verwerken om hun dienst aan ons te leveren:',
    ': envía a nuestro correo la conversación que confirmas en Fini.': ': stuurt het gesprek dat je in Fini bevestigt naar onze mailbox.',
    ': aloja el correo info@skurx.es.': ': host de mailbox info@skurx.es.',
    ': aloja la web y puede registrar datos técnicos de conexión, como la dirección IP, por motivos de seguridad.':
        ': host de website en kan om veiligheidsredenen technische verbindingsgegevens registreren, zoals je IP-adres.',
    'Algunos de estos proveedores pueden tratar datos fuera del Espacio Económico Europeo. En ese caso, la transferencia debe ampararse en las garantías que prevé el Reglamento General de Protección de Datos.':
        'Sommige van deze leveranciers kunnen gegevens verwerken buiten de Europese Economische Ruimte. In dat geval moet de doorgifte vallen onder de waarborgen van de Algemene Verordening Gegevensbescherming.',
    'Lo que se guarda en tu navegador': 'Wat er in je browser wordt opgeslagen',
    'Fini guarda la conversación en tu propio navegador durante un máximo de treinta días, para que puedas retomarla si vuelves. Esa información no nos llega hasta que confirmas el envío, y puedes borrarla en cualquier momento eliminando los datos del sitio en tu navegador. La web no utiliza cookies de publicidad ni de analítica.':
        'Fini bewaart het gesprek maximaal dertig dagen in je eigen browser, zodat je het kunt hervatten als je terugkomt. Wij ontvangen die informatie pas als je het verzenden bevestigt, en je kunt ze op elk moment wissen door de sitegegevens in je browser te verwijderen. De website gebruikt geen advertentie- of analysecookies.',
    'Tus derechos': 'Je rechten',
    'Puedes pedirnos acceder a tus datos, corregirlos, eliminarlos, oponerte a su tratamiento, limitarlo, recibirlos en un formato portable o retirar tu consentimiento en cualquier momento. Solo tienes que escribir a ':
        'Je kunt ons op elk moment vragen om je gegevens in te zien, te corrigeren of te verwijderen, bezwaar te maken tegen de verwerking of die te beperken, ze in een overdraagbaar formaat te ontvangen of je toestemming in te trekken. Stuur daarvoor een e-mail naar ',
    'Si consideras que no hemos tratado bien tus datos, puedes presentar una reclamación ante la Agencia Española de Protección de Datos (':
        'Vind je dat we niet goed met je gegevens zijn omgegaan, dan kun je een klacht indienen bij de Spaanse gegevensbeschermingsautoriteit (',
    'Cambios en esta política': 'Wijzigingen in deze verklaring',
    'Si cambiamos algo relevante, lo actualizaremos en esta página indicando la fecha de la última revisión.':
        'Als we iets wezenlijks wijzigen, passen we deze pagina aan en vermelden we de datum van de laatste herziening.',
}

# ---------------------------------------------------------------- Páginas de sector (plantilla)
SECTOR_UI = {
    'title': 'Automatisering voor {plural} | SKURX SYSTEMS',
    'desc': 'Automatisering en AI voor {plural}. {desc}',
    'crumb': 'SECTOREN',
    'pains_eyebrow': 'WAAR CAPACITEIT VERLOREN GAAT',
    'fix': 'WAT WE DOEN',
    'flow_eyebrow': 'IN DE PRAKTIJK',
    'flow_h2': 'Een gewone dag,<br>met het systeem aan het werk.',
    'flow_note': 'Illustratief scenario op basis van alledaagse situaties.',
    'control_eyebrow': 'GEEN BLACK BOXES',
    'audit_h3': 'Operationele Startaudit voor {plural}',
    'audit_tail': 'We geven je een helder overzicht van wat je kunt automatiseren en in welke volgorde. Het rapport is van jou, wat je ook besluit.',
    'audit_btn': 'Audit aanvragen',
    'ba_before_alt': 'Voor: woonkamer en keuken van een oud appartement, gescheiden door een tussenmuur, met donkere meubels, gedateerde tegels en weinig licht.',
    'ba_after_alt': 'Na: hetzelfde appartement gerenoveerd, met een open keuken en woonkamer, een kookeiland, houten vloeren en warm licht.',
    'ba_before': 'VOOR', 'ba_after': 'NA',
    'ba_aria': 'Vergelijk voor en na',
    'ba_caption': 'Schuif om te vergelijken. Computergegenereerde voorbeeldafbeelding.',
}

# ---------------------------------------------------------------- Ilustración de la portada
SVG = {
    'Tareas manuales': 'Handmatige taken',
    'Información dispersa': 'Versnipperde informatie',
    'Herramientas aisladas': 'Losse tools',
    'Seguimiento pendiente': 'Opvolging die blijft liggen',
    'Datos copiados a mano': 'Handmatig overgetypte data',
    'Dependencia de personas': 'Afhankelijk van personen',
    'CAPACIDAD': 'ECHTE',
    'REAL': 'CAPACITEIT',
}
