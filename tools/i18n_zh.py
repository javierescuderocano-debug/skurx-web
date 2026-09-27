# Textos en chino simplificado de la web. Clave = texto exacto en español; valor = traducción.
# Para añadir un idioma: copiar este archivo como i18n_<código>.py y traducir los valores.

LANG = 'zh'
LOCALE = 'zh_CN'
DIR = 'zh'                      # carpeta donde se publica
SECTORS_DIR = 'sectors'         # carpeta de las páginas de sector dentro de DIR
PRIVACY = 'privacy.html'
RTL = False                     # True solo para idiomas de derecha a izquierda (árabe)
JSONLD = {'country': '西班牙', 'knows': ['资源自动化', '流程自动化', '应用型人工智能', '工具互联']}

# Contacto mientras Fini no esté disponible en este idioma
CONTACT_TALK = "mailto:info@skurx.es?subject=%E8%81%94%E7%B3%BB%E6%88%91%E4%BB%AC%20-%20SKURX%20SYSTEMS"
CONTACT_AUDIT = "mailto:info@skurx.es?subject=%E5%88%9D%E5%A7%8B%E8%BF%90%E8%90%A5%E5%AE%A1%E8%AE%A1%20-%20SKURX%20SYSTEMS"

# ---------------------------------------------------------------- Comunes
COMMON = {
    'Saltar al contenido': '跳至正文',
    'CAPACIDAD LIBERADA': '释放产能',
    'Quiénes somos': '关于我们',
    'Qué hacemos': '业务内容',
    'Cómo lo hacemos': '工作方式',
    'Sectores': '行业',
    'Hablemos': '联系我们',
    'SKURX SYSTEMS - AUTOMATIZACIÓN DE RECURSOS': 'SKURX SYSTEMS - 资源自动化',
    'Privacidad': '隐私',
    'El trabajo bien hecho': '扎实的工作，',
    'no hace ruido.': '从不喧哗。',
    'Todo sigue en marcha, aunque ya no quede nadie en la oficina.': '即使办公室里已空无一人，一切仍在照常运转。',
    'SKURX SYSTEMS, inicio': 'SKURX SYSTEMS，首页',
    'Navegación principal': '主导航',
    'Idioma': '语言',
}

# ---------------------------------------------------------------- Portada
HOME = {
    'SKURX SYSTEMS | Automatización de Recursos': 'SKURX SYSTEMS | 资源自动化',
    'SKURX SYSTEMS libera la capacidad que las empresas pierden en trabajo manual con automatización, conexión de herramientas e IA aplicada. Para empresas de toda España.':
        'SKURX SYSTEMS 通过自动化、工具互联和应用型 AI，释放企业在手工操作中流失的产能。服务西班牙各地的企业。',
    'SKURX SYSTEMS — Comprender antes de proponer.': 'SKURX SYSTEMS — 先理解，再建议。',
    'AUTOMATIZACIÓN DE RECURSOS': '资源自动化',
    'Comprender antes de proponer.': '先理解，再建议。',
    'La mayoría de las empresas no necesitan más herramientas. Necesitan saber dónde se les escapa el tiempo, la información y la atención.':
        '大多数企业并不需要更多工具。它们需要知道，时间、信息和精力究竟流失在哪里。',
    'SKURX SYSTEMS identifica dónde se pierde capacidad y la convierte en sistemas de trabajo más claros, conectados y eficientes.':
        'SKURX SYSTEMS 找出产能流失的环节，将其转化为更清晰、更互联、更高效的工作体系。',
    'Tareas manuales': '手工任务',
    'Información dispersa': '信息分散',
    'Herramientas aisladas': '工具孤立',
    'Seguimiento pendiente': '跟进搁置',
    'Datos copiados a mano': '手工抄录数据',
    'Dependencia de personas': '依赖个人',
    'QUÉ HACEMOS': '业务内容',
    'De la fricción': '从摩擦',
    'a la': '到',
    'capacidad.': '产能。',
    'Detectamos dónde pierde capacidad tu empresa y la liberamos con automatización, herramientas conectadas e inteligencia artificial aplicada donde tiene sentido.':
        '我们找出您企业流失产能的环节，并在合适之处借助自动化、工具互联和应用型人工智能将其释放。',
    'Flujos de trabajo dispersos que convergen en capacidad real.': '分散的工作流程，汇聚为实际产能。',
    'NUESTROS SERVICIOS': '我们的服务',
    'La herramienta viene después.': '工具是后话。',
    'Automatización': '自动化',
    'Convertimos las tareas repetitivas en procesos automáticos, con las reglas que definimos contigo.':
        '我们与您共同制定规则，把重复性任务变成自动运行的流程。',
    'IA aplicada': '应用型 AI',
    'Para lo que una regla no resuelve: la IA potencia a tu equipo, no lo sustituye.':
        '用于规则解决不了的问题：AI 增强您的团队，而不是取代团队。',
    'Conexión de herramientas': '工具互联',
    'Conectamos tus herramientas para que la información pase de una a otra sin que nadie intervenga.':
        '我们打通您的各类工具，让信息在工具之间自动流转，无需人工介入。',
    'CÓMO LO HACEMOS': '工作方式',
    'Primero comprender.': '先理解。',
    'Después': '再',
    'intervenir.': '行动。',
    'No partimos de una tecnología, sino de una pregunta: ¿dónde está perdiendo capacidad tu empresa y por qué?':
        '我们不从某项技术出发，而是从一个问题出发：您的企业在哪里流失产能？原因是什么？',
    'Entender': '理解',
    'Conocemos tu empresa desde dentro, observando cómo trabaja tu equipo cada día.':
        '我们深入了解您的企业，观察团队每天如何工作。',
    'Analizar': '分析',
    'Localizamos dónde se pierde tiempo, información o clientes potenciales, y por qué.':
        '我们找出时间、信息或潜在客户在哪里流失，以及原因。',
    'Proponer': '建议',
    'Te decimos qué cambiaríamos y qué no merece la pena tocar.': '我们会告诉您哪些值得改变，哪些不必改动。',
    'Implantar': '实施',
    'Lo ponemos en marcha, lo probamos contigo y lo ajustamos hasta que funcione como tu equipo necesita.':
        '我们负责上线，与您一起测试，并持续调整，直到它符合团队的实际需要。',
    'EL PRIMER PASO': '第一步',
    'Auditoría Operativa Inicial': '初始运营审计',
    'En una semana analizamos cómo trabaja tu empresa y te entregamos un mapa claro: qué consume capacidad, qué se puede automatizar y en qué orden. El informe es tuyo, decidas lo que decidas.':
        '我们用一周时间分析您企业的运作方式，并交付一份清晰的全景图：哪些环节消耗产能，哪些可以自动化，按什么顺序推进。无论您最终如何决定，报告都归您所有。',
    'Solicitar auditoría': '申请审计',
    'Documentado': '有据可查',
    'Cada flujo explicado en lenguaje claro.': '每个流程都用通俗的语言说明。',
    'A nombre de tu empresa': '归属您的企业',
    'Cuentas, herramientas y datos son tuyos.': '账户、工具和数据都属于您。',
    'Auditable': '可审计',
    'Puedes ver qué ha hecho cada automatización y cuándo.': '您可以查看每项自动化做了什么、何时做的。',
    'Sin dependencia': '不被绑定',
    'Si dejamos de trabajar juntos, todo sigue siendo tuyo.': '即使我们停止合作，一切仍归您所有。',
    'EJEMPLOS POR SECTOR': '行业示例',
    'Cómo se ve en la práctica.': '实际效果如何。',
    'Escenarios ilustrativos basados en situaciones habituales. Trabajamos con empresas de cualquier sector, en toda España.':
        '以下为基于常见情况的示例场景。我们服务西班牙各地、各个行业的企业。',
    'INMOBILIARIAS': '房产中介',
    'Cada consulta sin respuesta es una visita que no ocurre.': '每一条未回复的咨询，都是一次没有发生的看房。',
    'Entra una consulta desde un portal.': '房产平台上来了一条咨询。',
    'Recibe respuesta con la información del inmueble.': '客户收到附有房源信息的回复。',
    'Queda registrada y asignada a un agente.': '咨询被登记并分配给一名经纪人。',
    'El agente empieza el día con el seguimiento preparado.': '经纪人一上班，跟进事项已准备就绪。',
    'GESTORÍAS': '会计税务事务所',
    'Menos tiempo persiguiendo papeles. Más tiempo asesorando.': '少花时间催材料，多花时间做咨询。',
    'Día 1': '第 1 天',
    'Se pide al cliente la documentación que falta.': '向客户索取缺少的材料。',
    'Día 3': '第 3 天',
    'Si no ha llegado, sale un recordatorio.': '如果仍未收到，自动发送提醒。',
    'Al llegar': '收到后',
    'Se clasifica y se archiva en su expediente.': '材料自动分类，归入客户档案。',
    'Listo': '完成',
    'El gestor recibe el aviso: expediente completo.': '顾问收到通知：档案已齐全。',
    'AUTOMOCIÓN': '汽车行业',
    'Un interesado que espera es un coche que se vende en otro sitio.': '让买家等待，车就会在别处卖掉。',
    'Consulta sobre un vehículo desde un portal.': '汽车平台上来了一条车辆咨询。',
    'Respuesta con ficha, precio y opción de cita.': '回复附上车辆信息、价格和预约选项。',
    'Se registra y se asigna a un comercial.': '咨询被登记并分配给一名销售。',
    'Día antes': '前一天',
    'Recordatorio automático de la prueba o la visita.': '自动提醒试驾或到店时间。',
    'MÁS SECTORES': '更多行业',
}

# ---------------------------------------------------------------- Privacidad
PRIVACY_TEXT = {
    'Política de privacidad | SKURX SYSTEMS': '隐私政策 | SKURX SYSTEMS',
    'Cómo trata SKURX SYSTEMS los datos que compartes a través de skurx.es y de su asistente Fini.':
        'SKURX SYSTEMS 如何处理您通过 skurx.es 分享的数据。',
    'Volver': '返回',
    'INFORMACIÓN LEGAL': '法律信息',
    'Política de privacidad': '隐私政策',
    'Última actualización: 26 de septiembre de 2026': '最后更新：2026 年 9 月 27 日',
    'Quién es el responsable': '数据控制者',
    'El responsable del tratamiento de tus datos es ': '您的数据控制者为 ',
    ', que desarrolla su actividad bajo el nombre comercial ': '，以商业名称 ',
    '. Para cualquier cuestión sobre tus datos puedes escribir a ': ' 开展业务。如您对个人数据有任何疑问，请发送邮件至 ',
    'Qué datos tratamos': '我们处理哪些数据',
    'Solo los que tú decides compartir con nosotros:': '仅限您自愿与我们分享的数据：',
    'A través de Fini': '通过 Fini',
    ', el asistente de la web: tu nombre, la forma de contacto que elijas (correo o teléfono), tu horario preferido y lo que nos cuentes sobre tu empresa y tu situación, junto con la conversación completa.':
        '（本网站的助手，目前仅提供西班牙语服务）：您的姓名、您选择的联系方式（邮箱或电话）、您方便联系的时间，以及您介绍的企业情况和自身需求，连同完整的对话内容。',
    'Por correo electrónico': '通过电子邮件',
    ': los datos que incluyas en tu mensaje.': '：您在邮件中提供的信息。',
    'No te pedimos datos especialmente sensibles. Te rogamos que no los incluyas en la conversación.':
        '我们不会要求您提供特殊类别的敏感数据。请勿在沟通中提供此类信息。',
    'Para qué los usamos': '数据用途',
    'Para atender tu consulta, ponernos en contacto contigo y, si lo solicitas, preparar una propuesta. No los usamos para enviarte publicidad ni los vendemos o cedemos a terceros con fines comerciales.':
        '用于答复您的咨询、与您联系，以及应您的要求准备方案。我们不会用这些数据向您发送广告，也不会出售或出于商业目的转交给第三方。',
    'Base legal': '法律依据',
    'Tratamos tus datos porque tú nos los envías voluntariamente para que te contactemos (tu consentimiento) y, cuando corresponde, para aplicar a petición tuya medidas previas a un posible contrato.':
        '我们处理您的数据，是因为您为了让我们与您联系而自愿提供（即您的同意）；在适用情况下，也是为了应您的要求，在可能签订合同之前采取相应措施。',
    'Cuánto tiempo los conservamos': '保存期限',
    'El tiempo necesario para atender tu consulta. Si no llegamos a trabajar juntos, los eliminamos como máximo doce meses después del último contacto. Si iniciamos una relación profesional, los conservaremos mientras dure y durante los plazos que exija la ley.':
        '以答复您的咨询所需时间为限。如果我们最终没有合作，最迟在最后一次联系后十二个月内删除。如果我们建立业务关系，数据将在合作期间及法律要求的期限内保存。',
    'Quién más interviene': '其他参与方',
    'Para que la web y el asistente funcionen nos apoyamos en proveedores que solo tratan los datos para prestarnos su servicio:':
        '为保障网站和助手正常运行，我们使用以下服务商，他们仅为向我们提供服务而处理数据：',
    ': envía a nuestro correo la conversación que confirmas en Fini.': '：将您在 Fini 中确认发送的对话转发至我们的邮箱。',
    ': aloja el correo info@skurx.es.': '：托管 info@skurx.es 邮箱。',
    ': aloja la web y puede registrar datos técnicos de conexión, como la dirección IP, por motivos de seguridad.':
        '：托管本网站，并可能出于安全原因记录技术连接数据，例如 IP 地址。',
    'Algunos de estos proveedores pueden tratar datos fuera del Espacio Económico Europeo. En ese caso, la transferencia debe ampararse en las garantías que prevé el Reglamento General de Protección de Datos.':
        '部分服务商可能在欧洲经济区以外处理数据。此类情况下，数据传输须受《通用数据保护条例》规定的保障措施约束。',
    'Lo que se guarda en tu navegador': '保存在您浏览器中的内容',
    'Fini guarda la conversación en tu propio navegador durante un máximo de treinta días, para que puedas retomarla si vuelves. Esa información no nos llega hasta que confirmas el envío, y puedes borrarla en cualquier momento eliminando los datos del sitio en tu navegador. La web no utiliza cookies de publicidad ni de analítica.':
        'Fini 会将对话保存在您自己的浏览器中，最长三十天，方便您再次访问时继续。在您确认发送之前，我们不会收到这些信息；您可以随时在浏览器中清除本网站数据来删除它。本网站不使用广告或分析类 Cookie。',
    'Tus derechos': '您的权利',
    'Puedes pedirnos acceder a tus datos, corregirlos, eliminarlos, oponerte a su tratamiento, limitarlo, recibirlos en un formato portable o retirar tu consentimiento en cualquier momento. Solo tienes que escribir a ':
        '您可以随时要求查阅、更正或删除您的数据，反对或限制对其的处理，以可携带格式获取数据，或撤回您的同意。只需发送邮件至 ',
    'Si consideras que no hemos tratado bien tus datos, puedes presentar una reclamación ante la Agencia Española de Protección de Datos (':
        '如您认为我们未妥善处理您的数据，可向西班牙数据保护局提出投诉 (',
    'Cambios en esta política': '本政策的变更',
    'Si cambiamos algo relevante, lo actualizaremos en esta página indicando la fecha de la última revisión.':
        '如有重要变更，我们会在本页面更新，并注明最近一次修订的日期。',
}

# ---------------------------------------------------------------- Páginas de sector (plantilla)
SECTOR_UI = {
    'title': '{plural}自动化 | SKURX SYSTEMS',
    'desc': '为{plural}提供自动化与 AI 服务。{desc}',
    'crumb': '行业',
    'pains_eyebrow': '产能流失在哪里',
    'fix': '我们的做法',
    'flow_eyebrow': '实际场景',
    'flow_h2': '普通的一天，<br>系统一直在运转。',
    'flow_note': '基于常见情况的示例场景。',
    'control_eyebrow': '没有黑箱',
    'audit_h3': '面向{plural}的初始运营审计',
    'audit_tail': '我们为您提供一份清晰的全景图：哪些该自动化，按什么顺序推进。无论您最终如何决定，报告都归您所有。',
    'audit_btn': '申请审计',
    'ba_before_alt': '改造前：一套老公寓的客厅和厨房，中间有隔墙，家具颜色深，瓷砖陈旧，光线不足。',
    'ba_after_alt': '改造后：同一套公寓翻新完成，开放式厨房与客厅相连，设有中岛，木地板，灯光温暖。',
    'ba_before': '改造前', 'ba_after': '改造后',
    'ba_aria': '对比改造前后',
    'ba_caption': '拖动滑块进行对比。示例图片由计算机生成。',
}

# ---------------------------------------------------------------- Ilustración de la portada
SVG = {
    'Tareas manuales': '手工任务',
    'Información dispersa': '信息分散',
    'Herramientas aisladas': '工具孤立',
    'Seguimiento pendiente': '跟进搁置',
    'Datos copiados a mano': '手工抄录数据',
    'Dependencia de personas': '依赖个人',
    'CAPACIDAD': '实际',
    'REAL': '产能',
}
