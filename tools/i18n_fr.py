# Textes en français du site. Clé = texte exact en espagnol ; valeur = traduction.
# Pour ajouter une langue : copier i18n_en.py sous le nom i18n_<code>.py et traduire les valeurs.

LANG = 'fr'
LOCALE = 'fr_FR'
DIR = 'fr'                      # carpeta donde se publica
SECTORS_DIR = 'secteurs'        # carpeta de las páginas de sector dentro de DIR
PRIVACY = 'confidentialite.html'
RTL = False                     # True solo para idiomas de derecha a izquierda (árabe)
JSONLD = {'country': 'Espagne', 'knows': ['Automatisation des Ressources', 'Automatisation des processus', 'Intelligence artificielle appliquée', 'Connexion des outils']}

# Contacto mientras Fini no esté disponible en este idioma
CONTACT_TALK = "mailto:info@skurx.es?subject=Parlons-en%20-%20SKURX%20SYSTEMS"
CONTACT_AUDIT = "mailto:info@skurx.es?subject=Audit%20Op%C3%A9rationnel%20Initial%20-%20SKURX%20SYSTEMS"

# ---------------------------------------------------------------- Comunes
COMMON = {
    'Siguiente sección': 'Section suivante',
    'Volver a la página principal': "Retour à la page d'accueil",
    'Volver arriba': 'Retour en haut',
    'Saltar al contenido': 'Aller au contenu',
    'CAPACIDAD LIBERADA': 'CAPACITÉ LIBÉRÉE',
    'Quiénes somos': 'Qui sommes-nous',
    'Qué hacemos': 'Ce que nous faisons',
    'Cómo lo hacemos': 'Notre méthode',
    'Sectores': 'Secteurs',
    'Hablemos': 'Parlons-en',
    'SKURX SYSTEMS - AUTOMATIZACIÓN DE RECURSOS': 'SKURX SYSTEMS - AUTOMATISATION DES RESSOURCES',
    'Privacidad': 'Confidentialité',
    'El trabajo bien hecho': 'Le travail bien fait',
    'no hace ruido.': 'ne fait pas de bruit.',
    'Todo sigue en marcha, aunque ya no quede nadie en la oficina.': 'Tout continue de tourner, même quand il ne reste plus personne au bureau.',
    'SKURX SYSTEMS, inicio': 'SKURX SYSTEMS, accueil',
    'Navegación principal': 'Navigation principale',
    'Idioma': 'Langue',
}

# ---------------------------------------------------------------- Portada
HOME = {
    'SKURX SYSTEMS | Automatización de Recursos': 'SKURX SYSTEMS | Automatisation des Ressources',
    'SKURX SYSTEMS libera la capacidad que las empresas pierden en trabajo manual con automatización, conexión de herramientas e IA aplicada. Para empresas de toda España.':
        "SKURX SYSTEMS libère la capacité que les entreprises perdent en travail manuel, grâce à l'automatisation, à la connexion des outils et à l'IA appliquée. Pour les entreprises de toute l'Espagne.",
    'SKURX SYSTEMS — Comprender antes de proponer.': 'SKURX SYSTEMS — Comprendre avant de proposer.',
    'AUTOMATIZACIÓN DE RECURSOS': 'AUTOMATISATION DES RESSOURCES',
    'Comprender antes de proponer.': 'Comprendre avant de proposer.',
    'La mayoría de las empresas no necesitan más herramientas. Necesitan saber dónde se les escapa el tiempo, la información y la atención.':
        "La plupart des entreprises n'ont pas besoin de plus d'outils. Elles ont besoin de savoir où leur échappent le temps, l'information et l'attention.",
    'SKURX SYSTEMS identifica dónde se pierde capacidad y la convierte en sistemas de trabajo más claros, conectados y eficientes.':
        'SKURX SYSTEMS repère où se perd la capacité et la transforme en méthodes de travail plus claires, plus connectées et plus efficaces.',
    'Tareas manuales': 'Tâches manuelles',
    'Información dispersa': 'Information dispersée',
    'Herramientas aisladas': 'Outils isolés',
    'Seguimiento pendiente': 'Relances en attente',
    'Datos copiados a mano': 'Données recopiées à la main',
    'Dependencia de personas': 'Dépendance aux personnes',
    'QUÉ HACEMOS': 'CE QUE NOUS FAISONS',
    'De la fricción': 'De la friction',
    'a la': 'à la',
    'capacidad.': 'capacité.',
    'Detectamos dónde pierde capacidad tu empresa y la liberamos con automatización, herramientas conectadas e inteligencia artificial aplicada donde tiene sentido.':
        "Nous repérons où votre entreprise perd de la capacité et nous la libérons grâce à l'automatisation, à des outils connectés et à l'intelligence artificielle appliquée, là où elle a du sens.",
    'Flujos de trabajo dispersos que convergen en capacidad real.': 'Des flux de travail dispersés qui convergent vers une capacité réelle.',
    'NUESTROS SERVICIOS': 'NOS SERVICES',
    'La herramienta viene después.': "L'outil vient après.",
    'Automatización': 'Automatisation',
    'Convertimos las tareas repetitivas en procesos automáticos, con las reglas que definimos contigo.':
        'Nous transformons les tâches répétitives en processus automatiques, selon des règles définies avec vous.',
    'IA aplicada': 'IA appliquée',
    'Para lo que una regla no resuelve: la IA potencia a tu equipo, no lo sustituye.':
        "Pour ce qu'une règle ne résout pas : l'IA renforce votre équipe, elle ne la remplace pas.",
    'Conexión de herramientas': 'Connexion des outils',
    'Conectamos tus herramientas para que la información pase de una a otra sin que nadie intervenga.':
        "Nous connectons vos outils pour que l'information passe de l'un à l'autre sans que personne n'ait à intervenir.",
    'CÓMO LO HACEMOS': 'NOTRE MÉTHODE',
    'Primero comprender.': "D'abord comprendre.",
    'Después': 'Ensuite',
    'intervenir.': 'intervenir.',
    'No partimos de una tecnología, sino de una pregunta: ¿dónde está perdiendo capacidad tu empresa y por qué?':
        "Nous ne partons pas d'une technologie, mais d'une question : où votre entreprise perd-elle de la capacité, et pourquoi ?",
    'Entender': 'Comprendre',
    'Conocemos tu empresa desde dentro, observando cómo trabaja tu equipo cada día.':
        'Nous découvrons votre entreprise de l\'intérieur, en observant comment votre équipe travaille au quotidien.',
    'Analizar': 'Analyser',
    'Localizamos dónde se pierde tiempo, información o clientes potenciales, y por qué.':
        'Nous identifions où se perdent du temps, des informations ou des clients potentiels, et pourquoi.',
    'Proponer': 'Proposer',
    'Te decimos qué cambiaríamos y qué no merece la pena tocar.': 'Nous vous disons ce que nous changerions et ce qui ne vaut pas la peine d\'être touché.',
    'Implantar': 'Mettre en place',
    'Lo ponemos en marcha, lo probamos contigo y lo ajustamos hasta que funcione como tu equipo necesita.':
        "Nous le mettons en service, le testons avec vous et l'ajustons jusqu'à ce qu'il fonctionne comme votre équipe en a besoin.",
    'EL PRIMER PASO': 'LA PREMIÈRE ÉTAPE',
    'Auditoría Operativa Inicial': 'Audit Opérationnel Initial',
    'En una semana analizamos cómo trabaja tu empresa y te entregamos un mapa claro: qué consume capacidad, qué se puede automatizar y en qué orden. El informe es tuyo, decidas lo que decidas.':
        "En une semaine, nous analysons le fonctionnement de votre entreprise et nous vous remettons une carte claire : ce qui consomme de la capacité, ce qui peut être automatisé et dans quel ordre. Le rapport vous appartient, quelle que soit votre décision.",
    'Solicitar auditoría': 'Demander un audit',
    'Documentado': 'Documenté',
    'Cada flujo explicado en lenguaje claro.': 'Chaque flux expliqué en langage clair.',
    'A nombre de tu empresa': 'Au nom de votre entreprise',
    'Cuentas, herramientas y datos son tuyos.': 'Comptes, outils et données vous appartiennent.',
    'Auditable': 'Auditable',
    'Puedes ver qué ha hecho cada automatización y cuándo.': 'Vous pouvez voir ce que chaque automatisation a fait, et quand.',
    'Sin dependencia': 'Sans dépendance',
    'Si dejamos de trabajar juntos, todo sigue siendo tuyo.': 'Si nous cessons de travailler ensemble, tout reste à vous.',
    'EJEMPLOS POR SECTOR': 'EXEMPLES PAR SECTEUR',
    'Cómo se ve en la práctica.': 'Ce que cela donne en pratique.',
    'Escenarios ilustrativos basados en situaciones habituales. Trabajamos con empresas de cualquier sector, en toda España.':
        "Scénarios illustratifs fondés sur des situations courantes. Nous travaillons avec des entreprises de tous secteurs, dans toute l'Espagne.",
    'INMOBILIARIAS': 'IMMOBILIER',
    'Cada consulta sin respuesta es una visita que no ocurre.': "Chaque demande sans réponse est une visite qui n'aura pas lieu.",
    'Entra una consulta desde un portal.': "Une demande arrive d'un portail immobilier.",
    'Recibe respuesta con la información del inmueble.': 'Elle reçoit une réponse avec les informations du bien.',
    'Queda registrada y asignada a un agente.': 'Elle est enregistrée et attribuée à un agent.',
    'El agente empieza el día con el seguimiento preparado.': "L'agent commence la journée avec le suivi déjà prêt.",
    'GESTORÍAS': 'CABINETS COMPTABLES',
    'Menos tiempo persiguiendo papeles. Más tiempo asesorando.': 'Moins de temps à courir après les papiers. Plus de temps pour conseiller.',
    'Día 1': 'Jour 1',
    'Se pide al cliente la documentación que falta.': 'On demande au client les documents manquants.',
    'Día 3': 'Jour 3',
    'Si no ha llegado, sale un recordatorio.': "S'ils ne sont pas arrivés, une relance part.",
    'Al llegar': 'À réception',
    'Se clasifica y se archiva en su expediente.': 'Ils sont classés et archivés dans le dossier du client.',
    'Listo': 'Terminé',
    'El gestor recibe el aviso: expediente completo.': "Le conseiller reçoit l'alerte : dossier complet.",
    'AUTOMOCIÓN': 'AUTOMOBILE',
    'Un interesado que espera es un coche que se vende en otro sitio.': 'Un acheteur qui attend, c\'est une voiture vendue ailleurs.',
    'Consulta sobre un vehículo desde un portal.': "Demande sur un véhicule depuis un portail.",
    'Respuesta con ficha, precio y opción de cita.': 'Réponse avec fiche, prix et possibilité de rendez-vous.',
    'Se registra y se asigna a un comercial.': 'Elle est enregistrée et attribuée à un commercial.',
    'Día antes': 'La veille',
    'Recordatorio automático de la prueba o la visita.': "Rappel automatique de l'essai ou de la visite.",
    'MÁS SECTORES': 'AUTRES SECTEURS',
}

# ---------------------------------------------------------------- Privacidad
PRIVACY_TEXT = {
    'Política de privacidad | SKURX SYSTEMS': 'Politique de confidentialité | SKURX SYSTEMS',
    'Cómo trata SKURX SYSTEMS los datos que compartes a través de skurx.es y de su asistente Fini.':
        'Comment SKURX SYSTEMS traite les données que vous partagez via skurx.es.',
    'Volver': 'Retour',
    'INFORMACIÓN LEGAL': 'INFORMATIONS LÉGALES',
    'Política de privacidad': 'Politique de confidentialité',
    'Última actualización: 26 de septiembre de 2026': 'Dernière mise à jour : 27 septembre 2026',
    'Quién es el responsable': 'Qui est responsable',
    'El responsable del tratamiento de tus datos es ': 'Le responsable du traitement de vos données est ',
    ', que desarrolla su actividad bajo el nombre comercial ': ', qui exerce son activité sous le nom commercial ',
    '. Para cualquier cuestión sobre tus datos puedes escribir a ': '. Pour toute question concernant vos données, vous pouvez écrire à ',
    'Qué datos tratamos': 'Quelles données nous traitons',
    'Solo los que tú decides compartir con nosotros:': 'Uniquement celles que vous choisissez de partager avec nous :',
    'A través de Fini': 'Via Fini',
    ', el asistente de la web: tu nombre, la forma de contacto que elijas (correo o teléfono), tu horario preferido y lo que nos cuentes sobre tu empresa y tu situación, junto con la conversación completa.':
        ", l'assistant du site (pour l'instant disponible en espagnol uniquement) : votre nom, le moyen de contact que vous choisissez (e-mail ou téléphone), vos horaires préférés et ce que vous nous dites de votre entreprise et de votre situation, ainsi que la conversation complète.",
    'Por correo electrónico': 'Par e-mail',
    ': los datos que incluyas en tu mensaje.': ' : les informations que vous incluez dans votre message.',
    'No te pedimos datos especialmente sensibles. Te rogamos que no los incluyas en la conversación.':
        'Nous ne vous demandons pas de données sensibles. Merci de ne pas les inclure dans vos messages.',
    'Para qué los usamos': 'À quoi elles servent',
    'Para atender tu consulta, ponernos en contacto contigo y, si lo solicitas, preparar una propuesta. No los usamos para enviarte publicidad ni los vendemos o cedemos a terceros con fines comerciales.':
        "À répondre à votre demande, à vous recontacter et, si vous le souhaitez, à préparer une proposition. Nous ne les utilisons pas pour vous envoyer de la publicité, et nous ne les vendons ni ne les cédons à des tiers à des fins commerciales.",
    'Base legal': 'Base légale',
    'Tratamos tus datos porque tú nos los envías voluntariamente para que te contactemos (tu consentimiento) y, cuando corresponde, para aplicar a petición tuya medidas previas a un posible contrato.':
        "Nous traitons vos données parce que vous nous les envoyez volontairement pour que nous vous contactions (votre consentement) et, le cas échéant, pour prendre à votre demande des mesures préalables à un éventuel contrat.",
    'Cuánto tiempo los conservamos': 'Combien de temps nous les conservons',
    'El tiempo necesario para atender tu consulta. Si no llegamos a trabajar juntos, los eliminamos como máximo doce meses después del último contacto. Si iniciamos una relación profesional, los conservaremos mientras dure y durante los plazos que exija la ley.':
        "Le temps nécessaire pour répondre à votre demande. Si nous ne travaillons pas ensemble, nous les supprimons au plus tard douze mois après le dernier contact. Si nous engageons une relation professionnelle, nous les conservons pendant toute sa durée et pendant les délais exigés par la loi.",
    'Quién más interviene': 'Qui d\'autre intervient',
    'Para que la web y el asistente funcionen nos apoyamos en proveedores que solo tratan los datos para prestarnos su servicio:':
        "Pour faire fonctionner le site et l'assistant, nous nous appuyons sur des prestataires qui ne traitent les données que pour nous fournir leur service :",
    ': envía a nuestro correo la conversación que confirmas en Fini.': ' : envoie à notre boîte mail la conversation que vous confirmez dans Fini.',
    ': aloja el correo info@skurx.es.': ' : héberge la boîte mail info@skurx.es.',
    ': aloja la web y puede registrar datos técnicos de conexión, como la dirección IP, por motivos de seguridad.':
        ' : héberge le site et peut enregistrer des données techniques de connexion, comme l\'adresse IP, pour des raisons de sécurité.',
    'Algunos de estos proveedores pueden tratar datos fuera del Espacio Económico Europeo. En ese caso, la transferencia debe ampararse en las garantías que prevé el Reglamento General de Protección de Datos.':
        "Certains de ces prestataires peuvent traiter des données en dehors de l'Espace économique européen. Dans ce cas, le transfert doit être encadré par les garanties prévues par le Règlement général sur la protection des données.",
    'Lo que se guarda en tu navegador': 'Ce qui est enregistré dans votre navigateur',
    'Fini guarda la conversación en tu propio navegador durante un máximo de treinta días, para que puedas retomarla si vuelves. Esa información no nos llega hasta que confirmas el envío, y puedes borrarla en cualquier momento eliminando los datos del sitio en tu navegador. La web no utiliza cookies de publicidad ni de analítica.':
        "Fini conserve la conversation dans votre propre navigateur pendant trente jours au maximum, pour que vous puissiez la reprendre si vous revenez. Ces informations ne nous parviennent pas tant que vous n'avez pas confirmé l'envoi, et vous pouvez les effacer à tout moment en supprimant les données du site dans votre navigateur. Le site n'utilise pas de cookies publicitaires ni de mesure d'audience.",
    'Tus derechos': 'Vos droits',
    'Puedes pedirnos acceder a tus datos, corregirlos, eliminarlos, oponerte a su tratamiento, limitarlo, recibirlos en un formato portable o retirar tu consentimiento en cualquier momento. Solo tienes que escribir a ':
        "Vous pouvez nous demander d'accéder à vos données, de les rectifier ou de les supprimer, vous opposer à leur traitement ou le limiter, les recevoir dans un format portable ou retirer votre consentement à tout moment. Il vous suffit d'écrire à ",
    'Si consideras que no hemos tratado bien tus datos, puedes presentar una reclamación ante la Agencia Española de Protección de Datos (':
        "Si vous estimez que nous n'avons pas traité correctement vos données, vous pouvez introduire une réclamation auprès de l'Agence espagnole de protection des données (",
    'Cambios en esta política': 'Modifications de cette politique',
    'Si cambiamos algo relevante, lo actualizaremos en esta página indicando la fecha de la última revisión.':
        'Si nous modifions un point important, nous mettrons cette page à jour en indiquant la date de la dernière révision.',
}

# ---------------------------------------------------------------- Páginas de sector (plantilla)
SECTOR_UI = {
    'title': 'Automatisation pour les {plural} | SKURX SYSTEMS',
    'desc': 'Automatisation et IA pour les {plural}. {desc}',
    'crumb': 'SECTEURS',
    'pains_eyebrow': 'OÙ SE PERD LA CAPACITÉ',
    'fix': 'CE QUE NOUS FAISONS',
    'flow_eyebrow': 'EN PRATIQUE',
    'flow_h2': 'Une journée ordinaire,<br>avec le système en marche.',
    'flow_note': 'Scénario illustratif fondé sur des situations courantes.',
    'control_eyebrow': 'PAS DE BOÎTE NOIRE',
    'audit_h3': 'Audit Opérationnel Initial pour les {plural}',
    'audit_tail': 'Nous vous remettons une carte claire de ce qu\'il faut automatiser et dans quel ordre. Le rapport vous appartient, quelle que soit votre décision.',
    'audit_btn': 'Demander un audit',
    'ba_before_alt': 'Avant : séjour et cuisine d\'un appartement ancien, séparés par une cloison, avec des meubles sombres, un carrelage daté et peu de lumière.',
    'ba_after_alt': 'Après : le même appartement rénové, avec une cuisine ouverte sur le séjour, un îlot, du parquet et une lumière chaleureuse.',
    'ba_before': 'AVANT', 'ba_after': 'APRÈS',
    'ba_aria': 'Comparer avant et après',
    'ba_caption': 'Faites glisser pour comparer. Image d\'exemple générée par ordinateur.',
}

# ---------------------------------------------------------------- Ilustración de la portada
SVG = {
    'Tareas manuales': 'Tâches manuelles',
    'Información dispersa': 'Information dispersée',
    'Herramientas aisladas': 'Outils isolés',
    'Seguimiento pendiente': 'Relances en attente',
    'Datos copiados a mano': 'Données recopiées à la main',
    'Dependencia de personas': 'Dépendance aux personnes',
    'CAPACIDAD': 'CAPACITÉ',
    'REAL': 'RÉELLE',
}
