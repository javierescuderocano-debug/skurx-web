# Testi in italiano del sito. Chiave = testo esatto in spagnolo; valore = traduzione.
# Per aggiungere una lingua: copiare questo file come i18n_<codice>.py e tradurre i valori.

LANG = 'it'
LOCALE = 'it_IT'
DIR = 'it'                      # carpeta donde se publica
SECTORS_DIR = 'settori'         # carpeta de las páginas de sector dentro de DIR
PRIVACY = 'privacy.html'
RTL = False                     # True solo para idiomas de derecha a izquierda (árabe)
JSONLD = {'country': 'Spagna', 'knows': ['Automazione delle Risorse', 'Automazione dei processi', 'Intelligenza artificiale applicata', 'Integrazione degli strumenti']}

# Contacto mientras Fini no esté disponible en este idioma
CONTACT_TALK = "mailto:info@skurx.es?subject=Parliamone%20-%20SKURX%20SYSTEMS"
CONTACT_AUDIT = "mailto:info@skurx.es?subject=Audit%20Operativo%20Iniziale%20-%20SKURX%20SYSTEMS"

# ---------------------------------------------------------------- Comunes
COMMON = {
    'Siguiente sección': 'Sezione successiva',
    'Volver a la página principal': 'Torna alla pagina principale',
    'Volver arriba': 'Torna su',
    'Saltar al contenido': 'Vai al contenuto',
    'CAPACIDAD LIBERADA': 'CAPACITÀ LIBERATA',
    'Quiénes somos': 'Chi siamo',
    'Qué hacemos': 'Cosa facciamo',
    'Cómo lo hacemos': 'Come lavoriamo',
    'Sectores': 'Settori',
    'Hablemos': 'Parliamone',
    'SKURX SYSTEMS - AUTOMATIZACIÓN DE RECURSOS': 'SKURX SYSTEMS - AUTOMAZIONE DELLE RISORSE',
    'Privacidad': 'Privacy',
    'El trabajo bien hecho': 'Il lavoro ben fatto',
    'no hace ruido.': 'non fa rumore.',
    'Todo sigue en marcha, aunque ya no quede nadie en la oficina.': "Tutto continua a funzionare, anche quando in ufficio non c’è più nessuno.",
    'SKURX SYSTEMS, inicio': 'SKURX SYSTEMS, home',
    'Navegación principal': 'Navigazione principale',
    'Idioma': 'Lingua',
}

# ---------------------------------------------------------------- Portada
HOME = {
    'SKURX SYSTEMS | Automatización de Recursos': 'SKURX SYSTEMS | Automazione delle Risorse',
    'SKURX SYSTEMS libera la capacidad que las empresas pierden en trabajo manual con automatización, conexión de herramientas e IA aplicada. Para empresas de toda España.':
        'SKURX SYSTEMS libera la capacità che le aziende perdono nel lavoro manuale, con automazione, integrazione degli strumenti e IA applicata. Per aziende di tutta la Spagna.',
    'SKURX SYSTEMS — Comprender antes de proponer.': 'SKURX SYSTEMS — Capire prima di proporre.',
    'AUTOMATIZACIÓN DE RECURSOS': 'AUTOMAZIONE DELLE RISORSE',
    'Comprender antes de proponer.': 'Capire prima di proporre.',
    'La mayoría de las empresas no necesitan más herramientas. Necesitan saber dónde se les escapa el tiempo, la información y la atención.':
        'Alla maggior parte delle aziende non servono altri strumenti. Serve sapere dove si disperdono tempo, informazioni e attenzione.',
    'SKURX SYSTEMS identifica dónde se pierde capacidad y la convierte en sistemas de trabajo más claros, conectados y eficientes.':
        'SKURX SYSTEMS individua dove si perde capacità e la trasforma in modi di lavorare più chiari, connessi ed efficienti.',
    'Tareas manuales': 'Attività manuali',
    'Información dispersa': 'Informazioni sparse',
    'Herramientas aisladas': 'Strumenti isolati',
    'Seguimiento pendiente': 'Follow-up in sospeso',
    'Datos copiados a mano': 'Dati copiati a mano',
    'Dependencia de personas': 'Dipendenza dalle persone',
    'QUÉ HACEMOS': 'COSA FACCIAMO',
    'De la fricción': 'Dall’attrito',
    'a la': 'alla',
    'capacidad.': 'capacità.',
    'Detectamos dónde pierde capacidad tu empresa y la liberamos con automatización, herramientas conectadas e inteligencia artificial aplicada donde tiene sentido.':
        'Individuiamo dove la tua azienda perde capacità e la liberiamo con automazione, strumenti connessi e intelligenza artificiale applicata dove ha senso.',
    'Flujos de trabajo dispersos que convergen en capacidad real.': 'Flussi di lavoro sparsi che convergono in capacità reale.',
    'NUESTROS SERVICIOS': 'I NOSTRI SERVIZI',
    'La herramienta viene después.': 'Lo strumento viene dopo.',
    'Automatización': 'Automazione',
    'Convertimos las tareas repetitivas en procesos automáticos, con las reglas que definimos contigo.':
        'Trasformiamo le attività ripetitive in processi automatici, con regole che definiamo insieme a te.',
    'IA aplicada': 'IA applicata',
    'Para lo que una regla no resuelve: la IA potencia a tu equipo, no lo sustituye.':
        'Per ciò che una regola non risolve: l’IA potenzia il tuo team, non lo sostituisce.',
    'Conexión de herramientas': 'Integrazione degli strumenti',
    'Conectamos tus herramientas para que la información pase de una a otra sin que nadie intervenga.':
        'Colleghiamo i tuoi strumenti perché le informazioni passino dall’uno all’altro senza che nessuno debba intervenire.',
    'CÓMO LO HACEMOS': 'COME LAVORIAMO',
    'Primero comprender.': 'Prima capire.',
    'Después': 'Poi',
    'intervenir.': 'intervenire.',
    'No partimos de una tecnología, sino de una pregunta: ¿dónde está perdiendo capacidad tu empresa y por qué?':
        'Non partiamo da una tecnologia, ma da una domanda: dove sta perdendo capacità la tua azienda, e perché?',
    'Entender': 'Capire',
    'Conocemos tu empresa desde dentro, observando cómo trabaja tu equipo cada día.':
        'Conosciamo la tua azienda dall’interno, osservando come lavora il tuo team ogni giorno.',
    'Analizar': 'Analizzare',
    'Localizamos dónde se pierde tiempo, información o clientes potenciales, y por qué.':
        'Individuiamo dove si perdono tempo, informazioni o potenziali clienti, e perché.',
    'Proponer': 'Proporre',
    'Te decimos qué cambiaríamos y qué no merece la pena tocar.': 'Ti diciamo cosa cambieremmo e cosa non vale la pena toccare.',
    'Implantar': 'Implementare',
    'Lo ponemos en marcha, lo probamos contigo y lo ajustamos hasta que funcione como tu equipo necesita.':
        'Lo mettiamo in funzione, lo testiamo con te e lo regoliamo finché non funziona come serve al tuo team.',
    'EL PRIMER PASO': 'IL PRIMO PASSO',
    'Auditoría Operativa Inicial': 'Audit Operativo Iniziale',
    'En una semana analizamos cómo trabaja tu empresa y te entregamos un mapa claro: qué consume capacidad, qué se puede automatizar y en qué orden. El informe es tuyo, decidas lo que decidas.':
        'In una settimana analizziamo come lavora la tua azienda e ti consegniamo una mappa chiara: cosa consuma capacità, cosa si può automatizzare e in quale ordine. Il report è tuo, qualunque cosa tu decida.',
    'Solicitar auditoría': "Richiedi l’audit",
    'Documentado': 'Documentato',
    'Cada flujo explicado en lenguaje claro.': 'Ogni flusso spiegato in un linguaggio chiaro.',
    'A nombre de tu empresa': 'Intestato alla tua azienda',
    'Cuentas, herramientas y datos son tuyos.': 'Account, strumenti e dati sono tuoi.',
    'Auditable': 'Verificabile',
    'Puedes ver qué ha hecho cada automatización y cuándo.': 'Puoi vedere cosa ha fatto ogni automazione e quando.',
    'Sin dependencia': 'Nessun vincolo',
    'Si dejamos de trabajar juntos, todo sigue siendo tuyo.': 'Se smettiamo di lavorare insieme, tutto resta tuo.',
    'EJEMPLOS POR SECTOR': 'ESEMPI PER SETTORE',
    'Cómo se ve en la práctica.': 'Come funziona in pratica.',
    'Escenarios ilustrativos basados en situaciones habituales. Trabajamos con empresas de cualquier sector, en toda España.':
        'Scenari illustrativi basati su situazioni comuni. Lavoriamo con aziende di qualsiasi settore, in tutta la Spagna.',
    'INMOBILIARIAS': 'AGENZIE IMMOBILIARI',
    'Cada consulta sin respuesta es una visita que no ocurre.': 'Ogni richiesta senza risposta è una visita che non avverrà.',
    'Entra una consulta desde un portal.': 'Arriva una richiesta da un portale.',
    'Recibe respuesta con la información del inmueble.': "Riceve una risposta con le informazioni sull’immobile.",
    'Queda registrada y asignada a un agente.': 'Viene registrata e assegnata a un agente.',
    'El agente empieza el día con el seguimiento preparado.': 'L’agente inizia la giornata con il follow-up già pronto.',
    'GESTORÍAS': 'STUDI COMMERCIALISTI',
    'Menos tiempo persiguiendo papeles. Más tiempo asesorando.': 'Meno tempo a rincorrere documenti. Più tempo per la consulenza.',
    'Día 1': 'Giorno 1',
    'Se pide al cliente la documentación que falta.': 'Al cliente vengono chiesti i documenti mancanti.',
    'Día 3': 'Giorno 3',
    'Si no ha llegado, sale un recordatorio.': 'Se non sono arrivati, parte un promemoria.',
    'Al llegar': "All’arrivo",
    'Se clasifica y se archiva en su expediente.': 'Vengono classificati e archiviati nella pratica del cliente.',
    'Listo': 'Fatto',
    'El gestor recibe el aviso: expediente completo.': 'Il consulente riceve l’avviso: pratica completa.',
    'AUTOMOCIÓN': 'SETTORE AUTO',
    'Un interesado que espera es un coche que se vende en otro sitio.': "Un interessato che aspetta è un’auto venduta altrove.",
    'Consulta sobre un vehículo desde un portal.': 'Richiesta su un veicolo da un portale.',
    'Respuesta con ficha, precio y opción de cita.': 'Risposta con scheda, prezzo e possibilità di appuntamento.',
    'Se registra y se asigna a un comercial.': 'Viene registrata e assegnata a un venditore.',
    'Día antes': 'Il giorno prima',
    'Recordatorio automático de la prueba o la visita.': 'Promemoria automatico del test drive o della visita.',
    'MÁS SECTORES': 'ALTRI SETTORI',
}

# ---------------------------------------------------------------- Privacidad
PRIVACY_TEXT = {
    'Política de privacidad | SKURX SYSTEMS': 'Informativa sulla privacy | SKURX SYSTEMS',
    'Cómo trata SKURX SYSTEMS los datos que compartes a través de skurx.es y de su asistente Fini.':
        'Come SKURX SYSTEMS tratta i dati che condividi tramite skurx.es.',
    'Volver': 'Indietro',
    'INFORMACIÓN LEGAL': 'INFORMAZIONI LEGALI',
    'Política de privacidad': 'Informativa sulla privacy',
    'Última actualización: 26 de septiembre de 2026': 'Ultimo aggiornamento: 27 settembre 2026',
    'Quién es el responsable': 'Chi è il titolare',
    'El responsable del tratamiento de tus datos es ': 'Il titolare del trattamento dei tuoi dati è ',
    ', que desarrolla su actividad bajo el nombre comercial ': ', che opera con il nome commerciale ',
    '. Para cualquier cuestión sobre tus datos puedes escribir a ': '. Per qualsiasi domanda sui tuoi dati puoi scrivere a ',
    'Qué datos tratamos': 'Quali dati trattiamo',
    'Solo los que tú decides compartir con nosotros:': 'Solo quelli che decidi di condividere con noi:',
    'A través de Fini': 'Tramite Fini',
    ', el asistente de la web: tu nombre, la forma de contacto que elijas (correo o teléfono), tu horario preferido y lo que nos cuentes sobre tu empresa y tu situación, junto con la conversación completa.':
        ", l’assistente del sito (per ora disponibile solo in spagnolo): il tuo nome, il recapito che scegli (email o telefono), l’orario che preferisci e ciò che ci racconti sulla tua azienda e sulla tua situazione, insieme alla conversazione completa.",
    'Por correo electrónico': 'Via email',
    ': los datos que incluyas en tu mensaje.': ': i dati che includi nel tuo messaggio.',
    'No te pedimos datos especialmente sensibles. Te rogamos que no los incluyas en la conversación.':
        'Non ti chiediamo dati appartenenti a categorie particolari. Ti preghiamo di non includerli nei tuoi messaggi.',
    'Para qué los usamos': 'Per cosa li usiamo',
    'Para atender tu consulta, ponernos en contacto contigo y, si lo solicitas, preparar una propuesta. No los usamos para enviarte publicidad ni los vendemos o cedemos a terceros con fines comerciales.':
        'Per rispondere alla tua richiesta, contattarti e, se lo chiedi, preparare una proposta. Non li usiamo per inviarti pubblicità e non li vendiamo né li cediamo a terzi per fini commerciali.',
    'Base legal': 'Base giuridica',
    'Tratamos tus datos porque tú nos los envías voluntariamente para que te contactemos (tu consentimiento) y, cuando corresponde, para aplicar a petición tuya medidas previas a un posible contrato.':
        'Trattiamo i tuoi dati perché ce li invii volontariamente affinché ti contattiamo (il tuo consenso) e, quando previsto, per adottare su tua richiesta misure precontrattuali.',
    'Cuánto tiempo los conservamos': 'Per quanto tempo li conserviamo',
    'El tiempo necesario para atender tu consulta. Si no llegamos a trabajar juntos, los eliminamos como máximo doce meses después del último contacto. Si iniciamos una relación profesional, los conservaremos mientras dure y durante los plazos que exija la ley.':
        'Per il tempo necessario a rispondere alla tua richiesta. Se non arriviamo a lavorare insieme, li cancelliamo al massimo dodici mesi dopo l’ultimo contatto. Se avviamo un rapporto professionale, li conserviamo per tutta la sua durata e per i periodi previsti dalla legge.',
    'Quién más interviene': 'Chi altro è coinvolto',
    'Para que la web y el asistente funcionen nos apoyamos en proveedores que solo tratan los datos para prestarnos su servicio:':
        'Per far funzionare il sito e l’assistente ci affidiamo a fornitori che trattano i dati solo per fornirci il loro servizio:',
    ': envía a nuestro correo la conversación que confirmas en Fini.': ': invia alla nostra casella email la conversazione che confermi in Fini.',
    ': aloja el correo info@skurx.es.': ': ospita la casella email info@skurx.es.',
    ': aloja la web y puede registrar datos técnicos de conexión, como la dirección IP, por motivos de seguridad.':
        ': ospita il sito e può registrare dati tecnici di connessione, come l’indirizzo IP, per motivi di sicurezza.',
    'Algunos de estos proveedores pueden tratar datos fuera del Espacio Económico Europeo. En ese caso, la transferencia debe ampararse en las garantías que prevé el Reglamento General de Protección de Datos.':
        'Alcuni di questi fornitori possono trattare dati al di fuori dello Spazio economico europeo. In tal caso, il trasferimento deve essere coperto dalle garanzie previste dal Regolamento generale sulla protezione dei dati.',
    'Lo que se guarda en tu navegador': 'Cosa viene salvato nel tuo browser',
    'Fini guarda la conversación en tu propio navegador durante un máximo de treinta días, para que puedas retomarla si vuelves. Esa información no nos llega hasta que confirmas el envío, y puedes borrarla en cualquier momento eliminando los datos del sitio en tu navegador. La web no utiliza cookies de publicidad ni de analítica.':
        'Fini salva la conversazione nel tuo browser per un massimo di trenta giorni, così puoi riprenderla se torni. Queste informazioni non ci arrivano finché non confermi l’invio, e puoi cancellarle in qualsiasi momento eliminando i dati del sito dal tuo browser. Il sito non utilizza cookie pubblicitari né di analisi.',
    'Tus derechos': 'I tuoi diritti',
    'Puedes pedirnos acceder a tus datos, corregirlos, eliminarlos, oponerte a su tratamiento, limitarlo, recibirlos en un formato portable o retirar tu consentimiento en cualquier momento. Solo tienes que escribir a ':
        'Puoi chiederci di accedere ai tuoi dati, correggerli o cancellarli, opporti al loro trattamento o limitarlo, riceverli in un formato portabile o revocare il tuo consenso in qualsiasi momento. Ti basta scrivere a ',
    'Si consideras que no hemos tratado bien tus datos, puedes presentar una reclamación ante la Agencia Española de Protección de Datos (':
        'Se ritieni che non abbiamo trattato correttamente i tuoi dati, puoi presentare un reclamo all’Agenzia spagnola per la protezione dei dati (',
    'Cambios en esta política': 'Modifiche a questa informativa',
    'Si cambiamos algo relevante, lo actualizaremos en esta página indicando la fecha de la última revisión.':
        'Se modifichiamo qualcosa di rilevante, aggiorneremo questa pagina indicando la data dell’ultima revisione.',
}

# ---------------------------------------------------------------- Páginas de sector (plantilla)
SECTOR_UI = {
    'title': 'Automazione per {plural} | SKURX SYSTEMS',
    'desc': 'Automazione e IA per {plural}. {desc}',
    'crumb': 'SETTORI',
    'pains_eyebrow': 'DOVE SI PERDE CAPACITÀ',
    'fix': 'COSA FACCIAMO',
    'flow_eyebrow': 'IN PRATICA',
    'flow_h2': 'Una giornata qualunque,<br>con il sistema in funzione.',
    'flow_note': 'Scenario illustrativo basato su situazioni comuni.',
    'control_eyebrow': 'NESSUNA SCATOLA NERA',
    'audit_h3': 'Audit Operativo Iniziale per {plural}',
    'audit_tail': 'Ti consegniamo una mappa chiara di cosa automatizzare e in quale ordine. Il report è tuo, qualunque cosa tu decida.',
    'audit_btn': "Richiedi l’audit",
    'ba_before_alt': 'Prima: soggiorno e cucina di un vecchio appartamento, separati da un tramezzo, con mobili scuri, piastrelle datate e poca luce.',
    'ba_after_alt': 'Dopo: lo stesso appartamento ristrutturato, con cucina e soggiorno open space, un’isola, pavimenti in legno e luce calda.',
    'ba_before': 'PRIMA', 'ba_after': 'DOPO',
    'ba_aria': 'Confronta prima e dopo',
    'ba_caption': 'Trascina per confrontare. Immagine di esempio generata al computer.',
}

# ---------------------------------------------------------------- Ilustración de la portada
SVG = {
    'Tareas manuales': 'Attività manuali',
    'Información dispersa': 'Informazioni sparse',
    'Herramientas aisladas': 'Strumenti isolati',
    'Seguimiento pendiente': 'Follow-up in sospeso',
    'Datos copiados a mano': 'Dati copiati a mano',
    'Dependencia de personas': 'Dipendenza dalle persone',
    'CAPACIDAD': 'CAPACITÀ',
    'REAL': 'REALE',
}
