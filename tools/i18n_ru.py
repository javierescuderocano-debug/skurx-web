# Textos en ruso de la web. Clave = texto exacto en español; valor = traducción.
# Para añadir un idioma: copiar este archivo como i18n_<código>.py y traducir los valores.

LANG = 'ru'
LOCALE = 'ru_RU'
DIR = 'ru'                      # carpeta donde se publica
SECTORS_DIR = 'sectors'         # carpeta de las páginas de sector dentro de DIR
PRIVACY = 'privacy.html'
RTL = False                     # True solo para idiomas de derecha a izquierda (árabe)
JSONLD = {'country': 'Испания', 'knows': ['Автоматизация ресурсов', 'Автоматизация процессов', 'Прикладной искусственный интеллект', 'Интеграция инструментов']}

# Contacto mientras Fini no esté disponible en este idioma
CONTACT_TALK = "mailto:info@skurx.es?subject=%D0%9F%D0%BE%D0%B3%D0%BE%D0%B2%D0%BE%D1%80%D0%B8%D0%BC%20-%20SKURX%20SYSTEMS"
CONTACT_AUDIT = "mailto:info@skurx.es?subject=%D0%9F%D0%B5%D1%80%D0%B2%D0%B8%D1%87%D0%BD%D1%8B%D0%B9%20%D0%BE%D0%BF%D0%B5%D1%80%D0%B0%D1%86%D0%B8%D0%BE%D0%BD%D0%BD%D1%8B%D0%B9%20%D0%B0%D1%83%D0%B4%D0%B8%D1%82%20-%20SKURX%20SYSTEMS"

# ---------------------------------------------------------------- Comunes
COMMON = {
    'Volver a la página principal': 'Вернуться на главную',
    'Volver arriba': 'Наверх',
    'Saltar al contenido': 'Перейти к содержанию',
    'CAPACIDAD LIBERADA': 'ВЫСВОБОЖДЁННЫЙ РЕСУРС',
    'Quiénes somos': 'О нас',
    'Qué hacemos': 'Что мы делаем',
    'Cómo lo hacemos': 'Как мы работаем',
    'Sectores': 'Отрасли',
    'Hablemos': 'Поговорим',
    'SKURX SYSTEMS - AUTOMATIZACIÓN DE RECURSOS': 'SKURX SYSTEMS - АВТОМАТИЗАЦИЯ РЕСУРСОВ',
    'Privacidad': 'Конфиденциальность',
    'El trabajo bien hecho': 'Хорошо сделанная работа',
    'no hace ruido.': 'не шумит.',
    'Todo sigue en marcha, aunque ya no quede nadie en la oficina.': 'Всё продолжает работать, даже когда в офисе уже никого нет.',
    'SKURX SYSTEMS, inicio': 'SKURX SYSTEMS, главная',
    'Navegación principal': 'Основная навигация',
    'Idioma': 'Язык',
}

# ---------------------------------------------------------------- Portada
HOME = {
    'SKURX SYSTEMS | Automatización de Recursos': 'SKURX SYSTEMS | Автоматизация ресурсов',
    'SKURX SYSTEMS libera la capacidad que las empresas pierden en trabajo manual con automatización, conexión de herramientas e IA aplicada. Para empresas de toda España.':
        'SKURX SYSTEMS высвобождает ресурс, который компании теряют на ручной работе, с помощью автоматизации, интеграции инструментов и прикладного ИИ. Для компаний по всей Испании.',
    'SKURX SYSTEMS — Comprender antes de proponer.': 'SKURX SYSTEMS — Понять, прежде чем предлагать.',
    'AUTOMATIZACIÓN DE RECURSOS': 'АВТОМАТИЗАЦИЯ РЕСУРСОВ',
    'Comprender antes de proponer.': 'Понять, прежде чем предлагать.',
    'La mayoría de las empresas no necesitan más herramientas. Necesitan saber dónde se les escapa el tiempo, la información y la atención.':
        'Большинству компаний не нужны новые инструменты. Им нужно понять, куда уходят их время, информация и внимание.',
    'SKURX SYSTEMS identifica dónde se pierde capacidad y la convierte en sistemas de trabajo más claros, conectados y eficientes.':
        'SKURX SYSTEMS находит, где теряется ресурс, и превращает его в более понятные, связанные и эффективные рабочие системы.',
    'Tareas manuales': 'Ручные задачи',
    'Información dispersa': 'Разрозненная информация',
    'Herramientas aisladas': 'Разобщённые инструменты',
    'Seguimiento pendiente': 'Забытые контакты',
    'Datos copiados a mano': 'Ручной перенос данных',
    'Dependencia de personas': 'Зависимость от людей',
    'QUÉ HACEMOS': 'ЧТО МЫ ДЕЛАЕМ',
    'De la fricción': 'От потерь',
    'a la': 'к',
    'capacidad.': 'ресурсу.',
    'Detectamos dónde pierde capacidad tu empresa y la liberamos con automatización, herramientas conectadas e inteligencia artificial aplicada donde tiene sentido.':
        'Мы находим, где ваша компания теряет ресурс, и высвобождаем его с помощью автоматизации, связанных инструментов и искусственного интеллекта там, где это оправдано.',
    'Flujos de trabajo dispersos que convergen en capacidad real.': 'Разрозненные рабочие процессы, которые сходятся в реальный ресурс.',
    'NUESTROS SERVICIOS': 'НАШИ УСЛУГИ',
    'La herramienta viene después.': 'Инструмент — потом.',
    'Automatización': 'Автоматизация',
    'Convertimos las tareas repetitivas en procesos automáticos, con las reglas que definimos contigo.':
        'Превращаем повторяющиеся задачи в автоматические процессы по правилам, которые определяем вместе с вами.',
    'IA aplicada': 'Прикладной ИИ',
    'Para lo que una regla no resuelve: la IA potencia a tu equipo, no lo sustituye.':
        'Для того, что не решить правилом: ИИ усиливает вашу команду, а не заменяет её.',
    'Conexión de herramientas': 'Интеграция инструментов',
    'Conectamos tus herramientas para que la información pase de una a otra sin que nadie intervenga.':
        'Связываем ваши инструменты, чтобы информация переходила из одного в другой без чьего-либо участия.',
    'CÓMO LO HACEMOS': 'КАК МЫ РАБОТАЕМ',
    'Primero comprender.': 'Сначала понять.',
    'Después': 'Потом',
    'intervenir.': 'действовать.',
    'No partimos de una tecnología, sino de una pregunta: ¿dónde está perdiendo capacidad tu empresa y por qué?':
        'Мы исходим не из технологии, а из вопроса: где ваша компания теряет ресурс и почему?',
    'Entender': 'Понять',
    'Conocemos tu empresa desde dentro, observando cómo trabaja tu equipo cada día.':
        'Изучаем вашу компанию изнутри: смотрим, как ваша команда работает каждый день.',
    'Analizar': 'Проанализировать',
    'Localizamos dónde se pierde tiempo, información o clientes potenciales, y por qué.':
        'Находим, где теряются время, информация или потенциальные клиенты, и почему.',
    'Proponer': 'Предложить',
    'Te decimos qué cambiaríamos y qué no merece la pena tocar.': 'Говорим, что мы бы изменили, а что трогать не стоит.',
    'Implantar': 'Внедрить',
    'Lo ponemos en marcha, lo probamos contigo y lo ajustamos hasta que funcione como tu equipo necesita.':
        'Запускаем, проверяем вместе с вами и настраиваем, пока всё не заработает так, как нужно вашей команде.',
    'EL PRIMER PASO': 'ПЕРВЫЙ ШАГ',
    'Auditoría Operativa Inicial': 'Первичный операционный аудит',
    'En una semana analizamos cómo trabaja tu empresa y te entregamos un mapa claro: qué consume capacidad, qué se puede automatizar y en qué orden. El informe es tuyo, decidas lo que decidas.':
        'За неделю мы разбираемся, как работает ваша компания, и передаём вам понятную карту: что отнимает ресурс, что можно автоматизировать и в каком порядке. Отчёт остаётся у вас, что бы вы ни решили.',
    'Solicitar auditoría': 'Заказать аудит',
    'Documentado': 'Документировано',
    'Cada flujo explicado en lenguaje claro.': 'Каждый процесс описан простым языком.',
    'A nombre de tu empresa': 'На имя вашей компании',
    'Cuentas, herramientas y datos son tuyos.': 'Учётные записи, инструменты и данные принадлежат вам.',
    'Auditable': 'Проверяемо',
    'Puedes ver qué ha hecho cada automatización y cuándo.': 'Вы видите, что и когда сделала каждая автоматизация.',
    'Sin dependencia': 'Без привязки',
    'Si dejamos de trabajar juntos, todo sigue siendo tuyo.': 'Если мы перестанем работать вместе, всё останется вашим.',
    'EJEMPLOS POR SECTOR': 'ПРИМЕРЫ ПО ОТРАСЛЯМ',
    'Cómo se ve en la práctica.': 'Как это выглядит на практике.',
    'Escenarios ilustrativos basados en situaciones habituales. Trabajamos con empresas de cualquier sector, en toda España.':
        'Иллюстративные сценарии на основе типичных ситуаций. Мы работаем с компаниями любых отраслей по всей Испании.',
    'INMOBILIARIAS': 'НЕДВИЖИМОСТЬ',
    'Cada consulta sin respuesta es una visita que no ocurre.': 'Каждый запрос без ответа — это несостоявшийся показ.',
    'Entra una consulta desde un portal.': 'С портала приходит запрос.',
    'Recibe respuesta con la información del inmueble.': 'Клиент получает ответ с информацией об объекте.',
    'Queda registrada y asignada a un agente.': 'Запрос регистрируется и передаётся агенту.',
    'El agente empieza el día con el seguimiento preparado.': 'Агент начинает день с уже подготовленным следующим шагом.',
    'GESTORÍAS': 'БУХГАЛТЕРСКИЕ ФИРМЫ',
    'Menos tiempo persiguiendo papeles. Más tiempo asesorando.': 'Меньше времени на сбор бумаг. Больше — на консультации.',
    'Día 1': 'День 1',
    'Se pide al cliente la documentación que falta.': 'Клиенту отправляется запрос недостающих документов.',
    'Día 3': 'День 3',
    'Si no ha llegado, sale un recordatorio.': 'Если документы не пришли, уходит напоминание.',
    'Al llegar': 'По получении',
    'Se clasifica y se archiva en su expediente.': 'Документы сортируются и подшиваются в дело клиента.',
    'Listo': 'Готово',
    'El gestor recibe el aviso: expediente completo.': 'Специалист получает уведомление: дело укомплектовано.',
    'AUTOMOCIÓN': 'АВТОБИЗНЕС',
    'Un interesado que espera es un coche que se vende en otro sitio.': 'Клиент, который ждёт, — это машина, проданная в другом месте.',
    'Consulta sobre un vehículo desde un portal.': 'С портала приходит запрос об автомобиле.',
    'Respuesta con ficha, precio y opción de cita.': 'Ответ с характеристиками, ценой и возможностью записаться.',
    'Se registra y se asigna a un comercial.': 'Запрос регистрируется и передаётся менеджеру по продажам.',
    'Día antes': 'Накануне',
    'Recordatorio automático de la prueba o la visita.': 'Автоматическое напоминание о тест-драйве или визите.',
    'MÁS SECTORES': 'ДРУГИЕ ОТРАСЛИ',
}

# ---------------------------------------------------------------- Privacidad
PRIVACY_TEXT = {
    'Política de privacidad | SKURX SYSTEMS': 'Политика конфиденциальности | SKURX SYSTEMS',
    'Cómo trata SKURX SYSTEMS los datos que compartes a través de skurx.es y de su asistente Fini.':
        'Как SKURX SYSTEMS обращается с данными, которые вы передаёте через skurx.es.',
    'Volver': 'Назад',
    'INFORMACIÓN LEGAL': 'ПРАВОВАЯ ИНФОРМАЦИЯ',
    'Política de privacidad': 'Политика конфиденциальности',
    'Última actualización: 26 de septiembre de 2026': 'Последнее обновление: 27 сентября 2026 г.',
    'Quién es el responsable': 'Кто отвечает за обработку',
    'El responsable del tratamiento de tus datos es ': 'Оператор ваших персональных данных — ',
    ', que desarrolla su actividad bajo el nombre comercial ': ', ведущий деятельность под коммерческим наименованием ',
    '. Para cualquier cuestión sobre tus datos puedes escribir a ': '. По любым вопросам, касающимся ваших данных, пишите на ',
    'Qué datos tratamos': 'Какие данные мы обрабатываем',
    'Solo los que tú decides compartir con nosotros:': 'Только те, которыми вы сами решите с нами поделиться:',
    'A través de Fini': 'Через Fini',
    ', el asistente de la web: tu nombre, la forma de contacto que elijas (correo o teléfono), tu horario preferido y lo que nos cuentes sobre tu empresa y tu situación, junto con la conversación completa.':
        ', ассистента сайта (пока только на испанском языке): ваше имя, выбранный способ связи (электронная почта или телефон), удобное для вас время и то, что вы расскажете о своей компании и ситуации, вместе с полной перепиской.',
    'Por correo electrónico': 'По электронной почте',
    ': los datos que incluyas en tu mensaje.': ': данные, которые вы укажете в своём сообщении.',
    'No te pedimos datos especialmente sensibles. Te rogamos que no los incluyas en la conversación.':
        'Мы не запрашиваем данные особых категорий. Просим не указывать их в переписке.',
    'Para qué los usamos': 'Для чего мы их используем',
    'Para atender tu consulta, ponernos en contacto contigo y, si lo solicitas, preparar una propuesta. No los usamos para enviarte publicidad ni los vendemos o cedemos a terceros con fines comerciales.':
        'Чтобы ответить на ваш запрос, связаться с вами и, если вы попросите, подготовить предложение. Мы не используем их для рекламных рассылок, не продаём и не передаём третьим лицам в коммерческих целях.',
    'Base legal': 'Правовое основание',
    'Tratamos tus datos porque tú nos los envías voluntariamente para que te contactemos (tu consentimiento) y, cuando corresponde, para aplicar a petición tuya medidas previas a un posible contrato.':
        'Мы обрабатываем ваши данные, потому что вы добровольно передаёте их нам, чтобы мы с вами связались (ваше согласие), а также, когда это применимо, чтобы по вашей просьбе принять меры, предшествующие возможному заключению договора.',
    'Cuánto tiempo los conservamos': 'Как долго мы их храним',
    'El tiempo necesario para atender tu consulta. Si no llegamos a trabajar juntos, los eliminamos como máximo doce meses después del último contacto. Si iniciamos una relación profesional, los conservaremos mientras dure y durante los plazos que exija la ley.':
        'Столько, сколько нужно, чтобы ответить на ваш запрос. Если сотрудничество не состоится, мы удалим их не позднее чем через двенадцать месяцев после последнего контакта. Если мы начнём работать вместе, мы будем хранить их, пока длится сотрудничество, и в течение сроков, установленных законом.',
    'Quién más interviene': 'Кто ещё участвует',
    'Para que la web y el asistente funcionen nos apoyamos en proveedores que solo tratan los datos para prestarnos su servicio:':
        'Для работы сайта и ассистента мы пользуемся услугами поставщиков, которые обрабатывают данные только для того, чтобы оказывать нам свои услуги:',
    ': envía a nuestro correo la conversación que confirmas en Fini.': ': отправляет на нашу почту переписку, которую вы подтверждаете в Fini.',
    ': aloja el correo info@skurx.es.': ': обслуживает почтовый ящик info@skurx.es.',
    ': aloja la web y puede registrar datos técnicos de conexión, como la dirección IP, por motivos de seguridad.':
        ': размещает сайт и в целях безопасности может регистрировать технические данные подключения, например IP-адрес.',
    'Algunos de estos proveedores pueden tratar datos fuera del Espacio Económico Europeo. En ese caso, la transferencia debe ampararse en las garantías que prevé el Reglamento General de Protección de Datos.':
        'Некоторые из этих поставщиков могут обрабатывать данные за пределами Европейской экономической зоны. В этом случае передача должна сопровождаться гарантиями, предусмотренными Общим регламентом по защите данных (GDPR).',
    'Lo que se guarda en tu navegador': 'Что хранится в вашем браузере',
    'Fini guarda la conversación en tu propio navegador durante un máximo de treinta días, para que puedas retomarla si vuelves. Esa información no nos llega hasta que confirmas el envío, y puedes borrarla en cualquier momento eliminando los datos del sitio en tu navegador. La web no utiliza cookies de publicidad ni de analítica.':
        'Fini хранит переписку в вашем браузере не более тридцати дней, чтобы вы могли продолжить её, если вернётесь. Эта информация не поступает к нам, пока вы не подтвердите отправку, и вы можете в любой момент удалить её, очистив данные сайта в браузере. Сайт не использует рекламные и аналитические файлы cookie.',
    'Tus derechos': 'Ваши права',
    'Puedes pedirnos acceder a tus datos, corregirlos, eliminarlos, oponerte a su tratamiento, limitarlo, recibirlos en un formato portable o retirar tu consentimiento en cualquier momento. Solo tienes que escribir a ':
        'Вы можете в любой момент запросить доступ к своим данным, их исправление или удаление, возразить против их обработки или ограничить её, получить данные в переносимом формате или отозвать своё согласие. Для этого достаточно написать на ',
    'Si consideras que no hemos tratado bien tus datos, puedes presentar una reclamación ante la Agencia Española de Protección de Datos (':
        'Если вы считаете, что мы ненадлежащим образом обработали ваши данные, вы можете подать жалобу в Испанское агентство по защите данных (',
    'Cambios en esta política': 'Изменения в этой политике',
    'Si cambiamos algo relevante, lo actualizaremos en esta página indicando la fecha de la última revisión.':
        'Если мы изменим что-то существенное, мы обновим эту страницу и укажем дату последней редакции.',
}

# ---------------------------------------------------------------- Páginas de sector (plantilla)
SECTOR_UI = {
    'title': 'Автоматизация для {plural} | SKURX SYSTEMS',
    'desc': 'Автоматизация и ИИ для {plural}. {desc}',
    'crumb': 'ОТРАСЛИ',
    'pains_eyebrow': 'ГДЕ ТЕРЯЕТСЯ РЕСУРС',
    'fix': 'ЧТО МЫ ДЕЛАЕМ',
    'flow_eyebrow': 'НА ПРАКТИКЕ',
    'flow_h2': 'Обычный день,<br>когда система работает.',
    'flow_note': 'Иллюстративный сценарий на основе типичных ситуаций.',
    'control_eyebrow': 'БЕЗ ЧЁРНЫХ ЯЩИКОВ',
    'audit_h3': 'Первичный операционный аудит для {plural}',
    'audit_tail': 'Мы передаём вам понятную карту: что автоматизировать и в каком порядке. Отчёт остаётся у вас, что бы вы ни решили.',
    'audit_btn': 'Заказать аудит',
    'ba_before_alt': 'До: гостиная и кухня старой квартиры, разделённые перегородкой, с тёмной мебелью, устаревшей плиткой и слабым освещением.',
    'ba_after_alt': 'После: та же квартира после ремонта, с кухней-гостиной, островом, деревянным полом и тёплым светом.',
    'ba_before': 'ДО', 'ba_after': 'ПОСЛЕ',
    'ba_aria': 'Сравнить «до» и «после»',
    'ba_caption': 'Потяните, чтобы сравнить. Пример изображения, созданного на компьютере.',
}

# ---------------------------------------------------------------- Ilustración de la portada
SVG = {
    'Tareas manuales': 'Ручные задачи',
    'Información dispersa': 'Разрозненная информация',
    'Herramientas aisladas': 'Разобщённые инструменты',
    'Seguimiento pendiente': 'Забытые контакты',
    'Datos copiados a mano': 'Ручной перенос данных',
    'Dependencia de personas': 'Зависимость от людей',
    'CAPACIDAD': 'РЕАЛЬНЫЙ',
    'REAL': 'РЕСУРС',
}
