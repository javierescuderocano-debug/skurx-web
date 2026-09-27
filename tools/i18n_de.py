# Textos en alemán de la web. Clave = texto exacto en español; valor = traducción.
# Para añadir un idioma: copiar este archivo como i18n_<código>.py y traducir los valores.

LANG = 'de'
LOCALE = 'de_DE'
DIR = 'de'                      # carpeta donde se publica
SECTORS_DIR = 'branchen'        # carpeta de las páginas de sector dentro de DIR
PRIVACY = 'datenschutz.html'
RTL = False                     # True solo para idiomas de derecha a izquierda (árabe)
JSONLD = {'country': 'Spanien', 'knows': ['Ressourcenautomatisierung', 'Prozessautomatisierung', 'Angewandte künstliche Intelligenz', 'Tool-Integration']}

# Contacto mientras Fini no esté disponible en este idioma
CONTACT_TALK = "mailto:info@skurx.es?subject=Sprechen%20wir%20-%20SKURX%20SYSTEMS"
CONTACT_AUDIT = "mailto:info@skurx.es?subject=Operative%20Erstanalyse%20-%20SKURX%20SYSTEMS"

# ---------------------------------------------------------------- Comunes
COMMON = {
    'Siguiente sección': 'Nächster Abschnitt',
    'Volver a la página principal': 'Zurück zur Startseite',
    'Volver arriba': 'Nach oben',
    'Saltar al contenido': 'Zum Inhalt springen',
    'CAPACIDAD LIBERADA': 'FREIGESETZTE KAPAZITÄT',
    'Quiénes somos': 'Wer wir sind',
    'Qué hacemos': 'Was wir tun',
    'Cómo lo hacemos': 'Wie wir arbeiten',
    'Sectores': 'Branchen',
    'Hablemos': 'Sprechen wir',
    'SKURX SYSTEMS - AUTOMATIZACIÓN DE RECURSOS': 'SKURX SYSTEMS - RESSOURCENAUTOMATISIERUNG',
    'Privacidad': 'Datenschutz',
    'El trabajo bien hecho': 'Gute Arbeit',
    'no hace ruido.': 'macht keinen Lärm.',
    'Todo sigue en marcha, aunque ya no quede nadie en la oficina.': 'Alles läuft weiter, auch wenn niemand mehr im Büro ist.',
    'SKURX SYSTEMS, inicio': 'SKURX SYSTEMS, Startseite',
    'Navegación principal': 'Hauptnavigation',
    'Idioma': 'Sprache',
}

# ---------------------------------------------------------------- Portada
HOME = {
    'SKURX SYSTEMS | Automatización de Recursos': 'SKURX SYSTEMS | Ressourcenautomatisierung',
    'SKURX SYSTEMS libera la capacidad que las empresas pierden en trabajo manual con automatización, conexión de herramientas e IA aplicada. Para empresas de toda España.':
        'SKURX SYSTEMS setzt die Kapazität frei, die Unternehmen an manuelle Arbeit verlieren – mit Automatisierung, Tool-Integration und angewandter KI. Für Unternehmen in ganz Spanien.',
    'SKURX SYSTEMS — Comprender antes de proponer.': 'SKURX SYSTEMS — Erst verstehen, dann vorschlagen.',
    'AUTOMATIZACIÓN DE RECURSOS': 'RESSOURCENAUTOMATISIERUNG',
    'Comprender antes de proponer.': 'Erst verstehen, dann vorschlagen.',
    'La mayoría de las empresas no necesitan más herramientas. Necesitan saber dónde se les escapa el tiempo, la información y la atención.':
        'Die meisten Unternehmen brauchen keine weiteren Tools. Sie müssen wissen, wo ihnen Zeit, Informationen und Aufmerksamkeit verloren gehen.',
    'SKURX SYSTEMS identifica dónde se pierde capacidad y la convierte en sistemas de trabajo más claros, conectados y eficientes.':
        'SKURX SYSTEMS erkennt, wo Kapazität verloren geht, und macht daraus klarere, vernetzte und effizientere Arbeitsabläufe.',
    'Tareas manuales': 'Manuelle Aufgaben',
    'Información dispersa': 'Verstreute Informationen',
    'Herramientas aisladas': 'Isolierte Tools',
    'Seguimiento pendiente': 'Offene Nachverfolgung',
    'Datos copiados a mano': 'Von Hand kopierte Daten',
    'Dependencia de personas': 'Abhängigkeit von Einzelnen',
    'QUÉ HACEMOS': 'WAS WIR TUN',
    'De la fricción': 'Von der Reibung',
    'a la': 'zur',
    'capacidad.': 'Kapazität.',
    'Detectamos dónde pierde capacidad tu empresa y la liberamos con automatización, herramientas conectadas e inteligencia artificial aplicada donde tiene sentido.':
        'Wir finden heraus, wo Ihr Unternehmen Kapazität verliert, und setzen sie frei – mit Automatisierung, vernetzten Tools und angewandter künstlicher Intelligenz, wo es sinnvoll ist.',
    'Flujos de trabajo dispersos que convergen en capacidad real.': 'Verstreute Arbeitsabläufe, die zu echter Kapazität zusammenfinden.',
    'NUESTROS SERVICIOS': 'UNSERE LEISTUNGEN',
    'La herramienta viene después.': 'Das Werkzeug kommt danach.',
    'Automatización': 'Automatisierung',
    'Convertimos las tareas repetitivas en procesos automáticos, con las reglas que definimos contigo.':
        'Wir machen aus wiederkehrenden Aufgaben automatische Abläufe – nach Regeln, die wir gemeinsam mit Ihnen festlegen.',
    'IA aplicada': 'Angewandte KI',
    'Para lo que una regla no resuelve: la IA potencia a tu equipo, no lo sustituye.':
        'Für das, was eine Regel nicht löst: KI stärkt Ihr Team, sie ersetzt es nicht.',
    'Conexión de herramientas': 'Tool-Integration',
    'Conectamos tus herramientas para que la información pase de una a otra sin que nadie intervenga.':
        'Wir verbinden Ihre Tools, damit Informationen von einem zum anderen fließen, ohne dass jemand eingreifen muss.',
    'CÓMO LO HACEMOS': 'WIE WIR ARBEITEN',
    'Primero comprender.': 'Erst verstehen.',
    'Después': 'Dann',
    'intervenir.': 'handeln.',
    'No partimos de una tecnología, sino de una pregunta: ¿dónde está perdiendo capacidad tu empresa y por qué?':
        'Wir gehen nicht von einer Technologie aus, sondern von einer Frage: Wo verliert Ihr Unternehmen Kapazität, und warum?',
    'Entender': 'Verstehen',
    'Conocemos tu empresa desde dentro, observando cómo trabaja tu equipo cada día.':
        'Wir lernen Ihr Unternehmen von innen kennen und sehen uns an, wie Ihr Team jeden Tag arbeitet.',
    'Analizar': 'Analysieren',
    'Localizamos dónde se pierde tiempo, información o clientes potenciales, y por qué.':
        'Wir finden heraus, wo Zeit, Informationen oder potenzielle Kunden verloren gehen, und warum.',
    'Proponer': 'Vorschlagen',
    'Te decimos qué cambiaríamos y qué no merece la pena tocar.': 'Wir sagen Ihnen, was wir ändern würden und was man besser so lässt.',
    'Implantar': 'Umsetzen',
    'Lo ponemos en marcha, lo probamos contigo y lo ajustamos hasta que funcione como tu equipo necesita.':
        'Wir setzen es um, testen es mit Ihnen und passen es an, bis es so funktioniert, wie Ihr Team es braucht.',
    'EL PRIMER PASO': 'DER ERSTE SCHRITT',
    'Auditoría Operativa Inicial': 'Operative Erstanalyse',
    'En una semana analizamos cómo trabaja tu empresa y te entregamos un mapa claro: qué consume capacidad, qué se puede automatizar y en qué orden. El informe es tuyo, decidas lo que decidas.':
        'In einer Woche analysieren wir, wie Ihr Unternehmen arbeitet, und übergeben Ihnen eine klare Übersicht: was Kapazität bindet, was sich automatisieren lässt und in welcher Reihenfolge. Der Bericht gehört Ihnen, wie auch immer Sie sich entscheiden.',
    'Solicitar auditoría': 'Analyse anfragen',
    'Documentado': 'Dokumentiert',
    'Cada flujo explicado en lenguaje claro.': 'Jeder Ablauf in verständlicher Sprache erklärt.',
    'A nombre de tu empresa': 'Auf Ihren Namen',
    'Cuentas, herramientas y datos son tuyos.': 'Konten, Tools und Daten gehören Ihnen.',
    'Auditable': 'Nachvollziehbar',
    'Puedes ver qué ha hecho cada automatización y cuándo.': 'Sie sehen, was jede Automatisierung getan hat und wann.',
    'Sin dependencia': 'Keine Abhängigkeit',
    'Si dejamos de trabajar juntos, todo sigue siendo tuyo.': 'Wenn wir nicht mehr zusammenarbeiten, gehört weiterhin alles Ihnen.',
    'EJEMPLOS POR SECTOR': 'BEISPIELE NACH BRANCHE',
    'Cómo se ve en la práctica.': 'So sieht es in der Praxis aus.',
    'Escenarios ilustrativos basados en situaciones habituales. Trabajamos con empresas de cualquier sector, en toda España.':
        'Beispielhafte Szenarien auf Basis alltäglicher Situationen. Wir arbeiten mit Unternehmen aus allen Branchen, in ganz Spanien.',
    'INMOBILIARIAS': 'IMMOBILIENMAKLER',
    'Cada consulta sin respuesta es una visita que no ocurre.': 'Jede unbeantwortete Anfrage ist eine Besichtigung, die nicht stattfindet.',
    'Entra una consulta desde un portal.': 'Über ein Immobilienportal kommt eine Anfrage herein.',
    'Recibe respuesta con la información del inmueble.': 'Sie wird mit den Angaben zur Immobilie beantwortet.',
    'Queda registrada y asignada a un agente.': 'Sie wird erfasst und einem Makler zugewiesen.',
    'El agente empieza el día con el seguimiento preparado.': 'Der Makler beginnt den Tag mit vorbereitetem Nachfassen.',
    'GESTORÍAS': 'STEUERKANZLEIEN',
    'Menos tiempo persiguiendo papeles. Más tiempo asesorando.': 'Weniger Zeit für Unterlagen hinterherlaufen. Mehr Zeit für Beratung.',
    'Día 1': 'Tag 1',
    'Se pide al cliente la documentación que falta.': 'Der Mandant wird um die fehlenden Unterlagen gebeten.',
    'Día 3': 'Tag 3',
    'Si no ha llegado, sale un recordatorio.': 'Sind sie noch nicht da, geht eine Erinnerung raus.',
    'Al llegar': 'Bei Eingang',
    'Se clasifica y se archiva en su expediente.': 'Sie werden sortiert und in der Mandantenakte abgelegt.',
    'Listo': 'Erledigt',
    'El gestor recibe el aviso: expediente completo.': 'Der Berater erhält die Meldung: Akte vollständig.',
    'AUTOMOCIÓN': 'AUTOMOBIL',
    'Un interesado que espera es un coche que se vende en otro sitio.': 'Ein Interessent, der warten muss, ist ein Auto, das woanders verkauft wird.',
    'Consulta sobre un vehículo desde un portal.': 'Über ein Portal kommt eine Anfrage zu einem Fahrzeug.',
    'Respuesta con ficha, precio y opción de cita.': 'Antwort mit Datenblatt, Preis und Terminoption.',
    'Se registra y se asigna a un comercial.': 'Sie wird erfasst und einem Verkäufer zugewiesen.',
    'Día antes': 'Am Vortag',
    'Recordatorio automático de la prueba o la visita.': 'Automatische Erinnerung an Probefahrt oder Termin.',
    'MÁS SECTORES': 'WEITERE BRANCHEN',
}

# ---------------------------------------------------------------- Privacidad
PRIVACY_TEXT = {
    'Política de privacidad | SKURX SYSTEMS': 'Datenschutzerklärung | SKURX SYSTEMS',
    'Cómo trata SKURX SYSTEMS los datos que compartes a través de skurx.es y de su asistente Fini.':
        'Wie SKURX SYSTEMS mit den Daten umgeht, die Sie über skurx.es mitteilen.',
    'Volver': 'Zurück',
    'INFORMACIÓN LEGAL': 'RECHTLICHE HINWEISE',
    'Política de privacidad': 'Datenschutzerklärung',
    'Última actualización: 26 de septiembre de 2026': 'Zuletzt aktualisiert: 27. September 2026',
    'Quién es el responsable': 'Wer verantwortlich ist',
    'El responsable del tratamiento de tus datos es ': 'Verantwortlich für die Verarbeitung Ihrer Daten ist ',
    ', que desarrolla su actividad bajo el nombre comercial ': ', tätig unter dem Handelsnamen ',
    '. Para cualquier cuestión sobre tus datos puedes escribir a ': '. Bei Fragen zu Ihren Daten erreichen Sie uns unter ',
    'Qué datos tratamos': 'Welche Daten wir verarbeiten',
    'Solo los que tú decides compartir con nosotros:': 'Nur die Daten, die Sie uns selbst mitteilen:',
    'A través de Fini': 'Über Fini',
    ', el asistente de la web: tu nombre, la forma de contacto que elijas (correo o teléfono), tu horario preferido y lo que nos cuentes sobre tu empresa y tu situación, junto con la conversación completa.':
        ', den Assistenten der Website (derzeit nur auf Spanisch verfügbar): Ihren Namen, den von Ihnen gewählten Kontaktweg (E-Mail oder Telefon), Ihre bevorzugte Uhrzeit und das, was Sie uns über Ihr Unternehmen und Ihre Situation erzählen, zusammen mit dem vollständigen Gesprächsverlauf.',
    'Por correo electrónico': 'Per E-Mail',
    ': los datos que incluyas en tu mensaje.': ': die Angaben, die Sie in Ihrer Nachricht machen.',
    'No te pedimos datos especialmente sensibles. Te rogamos que no los incluyas en la conversación.':
        'Wir fragen keine besonderen Kategorien personenbezogener Daten ab. Bitte geben Sie solche Daten in Ihren Nachrichten nicht an.',
    'Para qué los usamos': 'Wofür wir sie verwenden',
    'Para atender tu consulta, ponernos en contacto contigo y, si lo solicitas, preparar una propuesta. No los usamos para enviarte publicidad ni los vendemos o cedemos a terceros con fines comerciales.':
        'Um Ihre Anfrage zu beantworten, Sie zu kontaktieren und, wenn Sie es wünschen, ein Angebot zu erstellen. Wir verwenden sie nicht, um Ihnen Werbung zu schicken, und wir verkaufen sie nicht und geben sie nicht zu kommerziellen Zwecken an Dritte weiter.',
    'Base legal': 'Rechtsgrundlage',
    'Tratamos tus datos porque tú nos los envías voluntariamente para que te contactemos (tu consentimiento) y, cuando corresponde, para aplicar a petición tuya medidas previas a un posible contrato.':
        'Wir verarbeiten Ihre Daten, weil Sie sie uns freiwillig senden, damit wir Sie kontaktieren (Ihre Einwilligung), und gegebenenfalls zur Durchführung vorvertraglicher Maßnahmen auf Ihre Anfrage hin.',
    'Cuánto tiempo los conservamos': 'Wie lange wir sie aufbewahren',
    'El tiempo necesario para atender tu consulta. Si no llegamos a trabajar juntos, los eliminamos como máximo doce meses después del último contacto. Si iniciamos una relación profesional, los conservaremos mientras dure y durante los plazos que exija la ley.':
        'So lange, wie es für die Bearbeitung Ihrer Anfrage nötig ist. Kommt keine Zusammenarbeit zustande, löschen wir sie spätestens zwölf Monate nach dem letzten Kontakt. Beginnen wir eine geschäftliche Beziehung, bewahren wir sie für deren Dauer und für die gesetzlich vorgeschriebenen Fristen auf.',
    'Quién más interviene': 'Wer außerdem beteiligt ist',
    'Para que la web y el asistente funcionen nos apoyamos en proveedores que solo tratan los datos para prestarnos su servicio:':
        'Für den Betrieb der Website und des Assistenten nutzen wir Dienstleister, die die Daten nur verarbeiten, um ihre Leistung für uns zu erbringen:',
    ': envía a nuestro correo la conversación que confirmas en Fini.': ': sendet das Gespräch, das Sie in Fini bestätigen, an unser Postfach.',
    ': aloja el correo info@skurx.es.': ': hostet das Postfach info@skurx.es.',
    ': aloja la web y puede registrar datos técnicos de conexión, como la dirección IP, por motivos de seguridad.':
        ': hostet die Website und kann aus Sicherheitsgründen technische Verbindungsdaten wie die IP-Adresse protokollieren.',
    'Algunos de estos proveedores pueden tratar datos fuera del Espacio Económico Europeo. En ese caso, la transferencia debe ampararse en las garantías que prevé el Reglamento General de Protección de Datos.':
        'Einige dieser Dienstleister können Daten außerhalb des Europäischen Wirtschaftsraums verarbeiten. In diesem Fall muss die Übermittlung durch die Garantien abgesichert sein, die die Datenschutz-Grundverordnung vorsieht.',
    'Lo que se guarda en tu navegador': 'Was in Ihrem Browser gespeichert wird',
    'Fini guarda la conversación en tu propio navegador durante un máximo de treinta días, para que puedas retomarla si vuelves. Esa información no nos llega hasta que confirmas el envío, y puedes borrarla en cualquier momento eliminando los datos del sitio en tu navegador. La web no utiliza cookies de publicidad ni de analítica.':
        'Fini speichert das Gespräch bis zu dreißig Tage lang in Ihrem eigenen Browser, damit Sie es fortsetzen können, wenn Sie zurückkommen. Diese Informationen erreichen uns erst, wenn Sie das Senden bestätigen, und Sie können sie jederzeit löschen, indem Sie die Websitedaten in Ihrem Browser entfernen. Die Website verwendet keine Werbe- oder Analyse-Cookies.',
    'Tus derechos': 'Ihre Rechte',
    'Puedes pedirnos acceder a tus datos, corregirlos, eliminarlos, oponerte a su tratamiento, limitarlo, recibirlos en un formato portable o retirar tu consentimiento en cualquier momento. Solo tienes que escribir a ':
        'Sie können jederzeit Auskunft über Ihre Daten verlangen, sie berichtigen oder löschen lassen, der Verarbeitung widersprechen, sie einschränken lassen, die Daten in einem übertragbaren Format erhalten oder Ihre Einwilligung widerrufen. Schreiben Sie dazu einfach an ',
    'Si consideras que no hemos tratado bien tus datos, puedes presentar una reclamación ante la Agencia Española de Protección de Datos (':
        'Wenn Sie der Meinung sind, dass wir Ihre Daten nicht korrekt behandelt haben, können Sie sich bei der spanischen Datenschutzbehörde Agencia Española de Protección de Datos beschweren (',
    'Cambios en esta política': 'Änderungen dieser Erklärung',
    'Si cambiamos algo relevante, lo actualizaremos en esta página indicando la fecha de la última revisión.':
        'Wenn wir etwas Wesentliches ändern, aktualisieren wir diese Seite und geben das Datum der letzten Überarbeitung an.',
}

# ---------------------------------------------------------------- Páginas de sector (plantilla)
SECTOR_UI = {
    'title': 'Automatisierung für {plural} | SKURX SYSTEMS',
    'desc': 'Automatisierung und KI für {plural}. {desc}',
    'crumb': 'BRANCHEN',
    'pains_eyebrow': 'WO KAPAZITÄT VERLOREN GEHT',
    'fix': 'WAS WIR TUN',
    'flow_eyebrow': 'IN DER PRAXIS',
    'flow_h2': 'Ein ganz normaler Tag,<br>mit laufendem System.',
    'flow_note': 'Beispielhaftes Szenario auf Basis alltäglicher Situationen.',
    'control_eyebrow': 'KEINE BLACKBOX',
    'audit_h3': 'Operative Erstanalyse für {plural}',
    'audit_tail': 'Sie erhalten eine klare Übersicht, was sich automatisieren lässt und in welcher Reihenfolge. Der Bericht gehört Ihnen, wie auch immer Sie sich entscheiden.',
    'audit_btn': 'Analyse anfragen',
    'ba_before_alt': 'Vorher: Wohnzimmer und Küche einer alten Wohnung, durch eine Trennwand getrennt, mit dunklen Möbeln, veralteten Fliesen und wenig Licht.',
    'ba_after_alt': 'Nachher: dieselbe Wohnung renoviert, mit offener Wohnküche, Kochinsel, Holzboden und warmem Licht.',
    'ba_before': 'VORHER', 'ba_after': 'NACHHER',
    'ba_aria': 'Vorher und nachher vergleichen',
    'ba_caption': 'Zum Vergleichen schieben. Computergeneriertes Beispielbild.',
}

# ---------------------------------------------------------------- Ilustración de la portada
SVG = {
    'Tareas manuales': 'Manuelle Aufgaben',
    'Información dispersa': 'Verstreute Informationen',
    'Herramientas aisladas': 'Isolierte Tools',
    'Seguimiento pendiente': 'Offene Nachverfolgung',
    'Datos copiados a mano': 'Von Hand kopierte Daten',
    'Dependencia de personas': 'Abhängigkeit von Einzelnen',
    'CAPACIDAD': 'ECHTE',
    'REAL': 'KAPAZITÄT',
}
