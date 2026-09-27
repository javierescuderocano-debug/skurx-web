# Textos en català de la web. Clau = text exacte en espanyol; valor = traducció.
# Per afegir un idioma: copiar aquest fitxer com a i18n_<codi>.py i traduir els valors.

LANG = 'ca'
LOCALE = 'ca_ES'
DIR = 'ca'                      # carpeta on es publica
SECTORS_DIR = 'sectors'         # carpeta de les pàgines de sector dins de DIR
PRIVACY = 'privacitat.html'
RTL = False                     # True només per a idiomes de dreta a esquerra (àrab)
JSONLD = {'country': 'Espanya', 'knows': ['Automatització de Recursos', 'Automatització de processos', 'Intel·ligència artificial aplicada', "Connexió d'eines"]}

# Contacte mentre Fini no estigui disponible en aquest idioma
CONTACT_TALK = "mailto:info@skurx.es?subject=Parlem%20-%20SKURX%20SYSTEMS"
CONTACT_AUDIT = "mailto:info@skurx.es?subject=Auditoria%20Operativa%20Inicial%20-%20SKURX%20SYSTEMS"

# ---------------------------------------------------------------- Comuns
COMMON = {
    'Volver a la página principal': 'Tornar a la pàgina principal',
    'Volver arriba': 'Tornar a dalt',
    'Saltar al contenido': 'Salta al contingut',
    'CAPACIDAD LIBERADA': 'CAPACITAT ALLIBERADA',
    'Quiénes somos': 'Qui som',
    'Qué hacemos': 'Què fem',
    'Cómo lo hacemos': 'Com ho fem',
    'Sectores': 'Sectors',
    'Hablemos': 'Parlem',
    'SKURX SYSTEMS - AUTOMATIZACIÓN DE RECURSOS': 'SKURX SYSTEMS - AUTOMATITZACIÓ DE RECURSOS',
    'Privacidad': 'Privacitat',
    'El trabajo bien hecho': 'La feina ben feta',
    'no hace ruido.': 'no fa soroll.',
    'Todo sigue en marcha, aunque ya no quede nadie en la oficina.': "Tot continua funcionant, encara que ja no quedi ningú a l'oficina.",
    'SKURX SYSTEMS, inicio': 'SKURX SYSTEMS, inici',
    'Navegación principal': 'Navegació principal',
    'Idioma': 'Idioma',
}

# ---------------------------------------------------------------- Portada
HOME = {
    'SKURX SYSTEMS | Automatización de Recursos': 'SKURX SYSTEMS | Automatització de Recursos',
    'SKURX SYSTEMS libera la capacidad que las empresas pierden en trabajo manual con automatización, conexión de herramientas e IA aplicada. Para empresas de toda España.':
        "SKURX SYSTEMS allibera la capacitat que les empreses perden en feina manual, amb automatització, connexió d'eines i IA aplicada. Per a empreses de tot Espanya.",
    'SKURX SYSTEMS — Comprender antes de proponer.': 'SKURX SYSTEMS — Comprendre abans de proposar.',
    'AUTOMATIZACIÓN DE RECURSOS': 'AUTOMATITZACIÓ DE RECURSOS',
    'Comprender antes de proponer.': 'Comprendre abans de proposar.',
    'La mayoría de las empresas no necesitan más herramientas. Necesitan saber dónde se les escapa el tiempo, la información y la atención.':
        "La majoria d'empreses no necessiten més eines. Necessiten saber per on se'ls escapa el temps, la informació i l'atenció.",
    'SKURX SYSTEMS identifica dónde se pierde capacidad y la convierte en sistemas de trabajo más claros, conectados y eficientes.':
        'SKURX SYSTEMS identifica on es perd capacitat i la converteix en sistemes de treball més clars, connectats i eficients.',
    'Tareas manuales': 'Tasques manuals',
    'Información dispersa': 'Informació dispersa',
    'Herramientas aisladas': 'Eines aïllades',
    'Seguimiento pendiente': 'Seguiment pendent',
    'Datos copiados a mano': 'Dades copiades a mà',
    'Dependencia de personas': 'Dependència de persones',
    'QUÉ HACEMOS': 'QUÈ FEM',
    'De la fricción': 'De la fricció',
    'a la': 'a la',
    'capacidad.': 'capacitat.',
    'Detectamos dónde pierde capacidad tu empresa y la liberamos con automatización, herramientas conectadas e inteligencia artificial aplicada donde tiene sentido.':
        "Detectem on perd capacitat la teva empresa i l'alliberem amb automatització, eines connectades i intel·ligència artificial aplicada allà on té sentit.",
    'Flujos de trabajo dispersos que convergen en capacidad real.': 'Fluxos de treball dispersos que convergeixen en capacitat real.',
    'NUESTROS SERVICIOS': 'ELS NOSTRES SERVEIS',
    'La herramienta viene después.': "L'eina ve després.",
    'Automatización': 'Automatització',
    'Convertimos las tareas repetitivas en procesos automáticos, con las reglas que definimos contigo.':
        'Convertim les tasques repetitives en processos automàtics, amb les regles que definim amb tu.',
    'IA aplicada': 'IA aplicada',
    'Para lo que una regla no resuelve: la IA potencia a tu equipo, no lo sustituye.':
        "Per al que una regla no resol: la IA potencia el teu equip, no el substitueix.",
    'Conexión de herramientas': "Connexió d'eines",
    'Conectamos tus herramientas para que la información pase de una a otra sin que nadie intervenga.':
        "Connectem les teves eines perquè la informació passi de l'una a l'altra sense que ningú hi intervingui.",
    'CÓMO LO HACEMOS': 'COM HO FEM',
    'Primero comprender.': 'Primer, comprendre.',
    'Después': 'Després,',
    'intervenir.': 'intervenir.',
    'No partimos de una tecnología, sino de una pregunta: ¿dónde está perdiendo capacidad tu empresa y por qué?':
        'No partim d\'una tecnologia, sinó d\'una pregunta: on està perdent capacitat la teva empresa, i per què?',
    'Entender': 'Entendre',
    'Conocemos tu empresa desde dentro, observando cómo trabaja tu equipo cada día.':
        'Coneixem la teva empresa des de dins, observant com treballa el teu equip cada dia.',
    'Analizar': 'Analitzar',
    'Localizamos dónde se pierde tiempo, información o clientes potenciales, y por qué.':
        'Localitzem on es perd temps, informació o clients potencials, i per què.',
    'Proponer': 'Proposar',
    'Te decimos qué cambiaríamos y qué no merece la pena tocar.': 'Et diem què canviaríem i què no val la pena tocar.',
    'Implantar': 'Implantar',
    'Lo ponemos en marcha, lo probamos contigo y lo ajustamos hasta que funcione como tu equipo necesita.':
        "Ho posem en marxa, ho provem amb tu i ho ajustem fins que funcioni com el teu equip necessita.",
    'EL PRIMER PASO': 'EL PRIMER PAS',
    'Auditoría Operativa Inicial': 'Auditoria Operativa Inicial',
    'En una semana analizamos cómo trabaja tu empresa y te entregamos un mapa claro: qué consume capacidad, qué se puede automatizar y en qué orden. El informe es tuyo, decidas lo que decidas.':
        "En una setmana analitzem com treballa la teva empresa i et lliurem un mapa clar: què consumeix capacitat, què es pot automatitzar i en quin ordre. L'informe és teu, decideixis el que decideixis.",
    'Solicitar auditoría': 'Sol·licitar auditoria',
    'Documentado': 'Documentat',
    'Cada flujo explicado en lenguaje claro.': 'Cada flux explicat en un llenguatge clar.',
    'A nombre de tu empresa': 'A nom de la teva empresa',
    'Cuentas, herramientas y datos son tuyos.': 'Els comptes, les eines i les dades són teus.',
    'Auditable': 'Auditable',
    'Puedes ver qué ha hecho cada automatización y cuándo.': 'Pots veure què ha fet cada automatització i quan.',
    'Sin dependencia': 'Sense dependència',
    'Si dejamos de trabajar juntos, todo sigue siendo tuyo.': 'Si deixem de treballar junts, tot continua sent teu.',
    'EJEMPLOS POR SECTOR': 'EXEMPLES PER SECTOR',
    'Cómo se ve en la práctica.': 'Com es veu a la pràctica.',
    'Escenarios ilustrativos basados en situaciones habituales. Trabajamos con empresas de cualquier sector, en toda España.':
        "Escenaris il·lustratius basats en situacions habituals. Treballem amb empreses de qualsevol sector, a tot Espanya.",
    'INMOBILIARIAS': 'IMMOBILIÀRIES',
    'Cada consulta sin respuesta es una visita que no ocurre.': 'Cada consulta sense resposta és una visita que no es fa.',
    'Entra una consulta desde un portal.': 'Entra una consulta des d\'un portal.',
    'Recibe respuesta con la información del inmueble.': "Rep resposta amb la informació de l'immoble.",
    'Queda registrada y asignada a un agente.': 'Queda registrada i assignada a un agent.',
    'El agente empieza el día con el seguimiento preparado.': "L'agent comença el dia amb el seguiment preparat.",
    'GESTORÍAS': 'GESTORIES',
    'Menos tiempo persiguiendo papeles. Más tiempo asesorando.': 'Menys temps perseguint papers. Més temps assessorant.',
    'Día 1': 'Dia 1',
    'Se pide al cliente la documentación que falta.': 'Es demana al client la documentació que falta.',
    'Día 3': 'Dia 3',
    'Si no ha llegado, sale un recordatorio.': "Si no ha arribat, s'envia un recordatori.",
    'Al llegar': 'En arribar',
    'Se clasifica y se archiva en su expediente.': "Es classifica i s'arxiva al seu expedient.",
    'Listo': 'Enllestit',
    'El gestor recibe el aviso: expediente completo.': "El gestor rep l'avís: expedient complet.",
    'AUTOMOCIÓN': 'AUTOMOCIÓ',
    'Un interesado que espera es un coche que se vende en otro sitio.': "Un interessat que espera és un cotxe que es ven en un altre lloc.",
    'Consulta sobre un vehículo desde un portal.': "Consulta sobre un vehicle des d'un portal.",
    'Respuesta con ficha, precio y opción de cita.': 'Resposta amb fitxa, preu i opció de cita.',
    'Se registra y se asigna a un comercial.': "Es registra i s'assigna a un comercial.",
    'Día antes': 'El dia abans',
    'Recordatorio automático de la prueba o la visita.': 'Recordatori automàtic de la prova o la visita.',
    'MÁS SECTORES': 'MÉS SECTORS',
}

# ---------------------------------------------------------------- Privacitat
PRIVACY_TEXT = {
    'Política de privacidad | SKURX SYSTEMS': 'Política de privacitat | SKURX SYSTEMS',
    'Cómo trata SKURX SYSTEMS los datos que compartes a través de skurx.es y de su asistente Fini.':
        'Com tracta SKURX SYSTEMS les dades que comparteixes a través de skurx.es.',
    'Volver': 'Tornar',
    'INFORMACIÓN LEGAL': 'INFORMACIÓ LEGAL',
    'Política de privacidad': 'Política de privacitat',
    'Última actualización: 26 de septiembre de 2026': 'Última actualització: 27 de setembre de 2026',
    'Quién es el responsable': 'Qui és el responsable',
    'El responsable del tratamiento de tus datos es ': 'El responsable del tractament de les teves dades és ',
    ', que desarrolla su actividad bajo el nombre comercial ': ", que exerceix la seva activitat amb el nom comercial ",
    '. Para cualquier cuestión sobre tus datos puedes escribir a ': '. Per a qualsevol qüestió sobre les teves dades pots escriure a ',
    'Qué datos tratamos': 'Quines dades tractem',
    'Solo los que tú decides compartir con nosotros:': 'Només les que tu decideixes compartir amb nosaltres:',
    'A través de Fini': 'A través de Fini',
    ', el asistente de la web: tu nombre, la forma de contacto que elijas (correo o teléfono), tu horario preferido y lo que nos cuentes sobre tu empresa y tu situación, junto con la conversación completa.':
        ", l'assistent del web (de moment, només en espanyol): el teu nom, la forma de contacte que triïs (correu o telèfon), l'horari que prefereixis i el que ens expliquis sobre la teva empresa i la teva situació, juntament amb la conversa completa.",
    'Por correo electrónico': 'Per correu electrònic',
    ': los datos que incluyas en tu mensaje.': ': les dades que incloguis en el teu missatge.',
    'No te pedimos datos especialmente sensibles. Te rogamos que no los incluyas en la conversación.':
        "No et demanem dades especialment sensibles. Et preguem que no les incloguis a la conversa.",
    'Para qué los usamos': 'Per a què les fem servir',
    'Para atender tu consulta, ponernos en contacto contigo y, si lo solicitas, preparar una propuesta. No los usamos para enviarte publicidad ni los vendemos o cedemos a terceros con fines comerciales.':
        "Per atendre la teva consulta, posar-nos en contacte amb tu i, si ho sol·licites, preparar una proposta. No les fem servir per enviar-te publicitat ni les venem o cedim a tercers amb finalitats comercials.",
    'Base legal': 'Base legal',
    'Tratamos tus datos porque tú nos los envías voluntariamente para que te contactemos (tu consentimiento) y, cuando corresponde, para aplicar a petición tuya medidas previas a un posible contrato.':
        "Tractem les teves dades perquè tu ens les envies voluntàriament perquè et contactem (el teu consentiment) i, quan correspon, per aplicar a petició teva mesures prèvies a un possible contracte.",
    'Cuánto tiempo los conservamos': 'Quant de temps les conservem',
    'El tiempo necesario para atender tu consulta. Si no llegamos a trabajar juntos, los eliminamos como máximo doce meses después del último contacto. Si iniciamos una relación profesional, los conservaremos mientras dure y durante los plazos que exija la ley.':
        "El temps necessari per atendre la teva consulta. Si no arribem a treballar junts, les eliminem com a màxim dotze mesos després de l'últim contacte. Si iniciem una relació professional, les conservarem mentre duri i durant els terminis que exigeixi la llei.",
    'Quién más interviene': 'Qui més hi intervé',
    'Para que la web y el asistente funcionen nos apoyamos en proveedores que solo tratan los datos para prestarnos su servicio:':
        "Perquè el web i l'assistent funcionin, ens recolzem en proveïdors que només tracten les dades per prestar-nos el seu servei:",
    ': envía a nuestro correo la conversación que confirmas en Fini.': ': envia al nostre correu la conversa que confirmes a Fini.',
    ': aloja el correo info@skurx.es.': ': allotja el correu info@skurx.es.',
    ': aloja la web y puede registrar datos técnicos de conexión, como la dirección IP, por motivos de seguridad.':
        ": allotja el web i pot registrar dades tècniques de connexió, com l'adreça IP, per motius de seguretat.",
    'Algunos de estos proveedores pueden tratar datos fuera del Espacio Económico Europeo. En ese caso, la transferencia debe ampararse en las garantías que prevé el Reglamento General de Protección de Datos.':
        "Alguns d'aquests proveïdors poden tractar dades fora de l'Espai Econòmic Europeu. En aquest cas, la transferència s'ha d'emparar en les garanties que preveu el Reglament General de Protecció de Dades.",
    'Lo que se guarda en tu navegador': 'El que es desa al teu navegador',
    'Fini guarda la conversación en tu propio navegador durante un máximo de treinta días, para que puedas retomarla si vuelves. Esa información no nos llega hasta que confirmas el envío, y puedes borrarla en cualquier momento eliminando los datos del sitio en tu navegador. La web no utiliza cookies de publicidad ni de analítica.':
        "Fini desa la conversa al teu propi navegador durant un màxim de trenta dies, perquè la puguis reprendre si hi tornes. Aquesta informació no ens arriba fins que confirmes l'enviament, i la pots esborrar en qualsevol moment eliminant les dades del lloc al teu navegador. El web no utilitza galetes de publicitat ni d'analítica.",
    'Tus derechos': 'Els teus drets',
    'Puedes pedirnos acceder a tus datos, corregirlos, eliminarlos, oponerte a su tratamiento, limitarlo, recibirlos en un formato portable o retirar tu consentimiento en cualquier momento. Solo tienes que escribir a ':
        "Ens pots demanar accedir a les teves dades, corregir-les, eliminar-les, oposar-te al seu tractament, limitar-lo, rebre-les en un format portable o retirar el teu consentiment en qualsevol moment. Només has d'escriure a ",
    'Si consideras que no hemos tratado bien tus datos, puedes presentar una reclamación ante la Agencia Española de Protección de Datos (':
        "Si consideres que no hem tractat bé les teves dades, pots presentar una reclamació davant l'Agència Espanyola de Protecció de Dades (",
    'Cambios en esta política': 'Canvis en aquesta política',
    'Si cambiamos algo relevante, lo actualizaremos en esta página indicando la fecha de la última revisión.':
        "Si canviem alguna cosa rellevant, ho actualitzarem en aquesta pàgina indicant la data de l'última revisió.",
}

# ---------------------------------------------------------------- Pàgines de sector (plantilla)
SECTOR_UI = {
    'title': 'Automatització per a {plural} | SKURX SYSTEMS',
    'desc': 'Automatització i IA per a {plural}. {desc}',
    'crumb': 'SECTORS',
    'pains_eyebrow': 'ON ES PERD CAPACITAT',
    'fix': 'QUÈ FEM',
    'flow_eyebrow': 'A LA PRÀCTICA',
    'flow_h2': 'Un dia qualsevol,<br>amb el sistema en marxa.',
    'flow_note': 'Escenari il·lustratiu basat en situacions habituals.',
    'control_eyebrow': 'SENSE CAIXES NEGRES',
    'audit_h3': 'Auditoria Operativa Inicial per a {plural}',
    'audit_tail': "Et lliurem un mapa clar del que cal automatitzar i en quin ordre. L'informe és teu, decideixis el que decideixis.",
    'audit_btn': 'Sol·licitar auditoria',
    'ba_before_alt': "Abans: menjador i cuina d'un pis antic, separats per un envà, amb mobles foscos, rajoles antiquades i poca llum.",
    'ba_after_alt': 'Després: el mateix pis reformat, amb la cuina oberta al menjador, una illa, terra de fusta i llum càlida.',
    'ba_before': 'ABANS', 'ba_after': 'DESPRÉS',
    'ba_aria': "Compara l'abans i el després",
    'ba_caption': "Llisca per comparar. Imatge d'exemple generada per ordinador.",
}

# ---------------------------------------------------------------- Il·lustració de la portada
SVG = {
    'Tareas manuales': 'Tasques manuals',
    'Información dispersa': 'Informació dispersa',
    'Herramientas aisladas': 'Eines aïllades',
    'Seguimiento pendiente': 'Seguiment pendent',
    'Datos copiados a mano': 'Dades copiades a mà',
    'Dependencia de personas': 'Dependència de persones',
    'CAPACIDAD': 'CAPACITAT',
    'REAL': 'REAL',
}
