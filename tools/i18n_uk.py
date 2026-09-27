# Textos en ucraniano de la web. Clave = texto exacto en español; valor = traducción.
# Para añadir un idioma: copiar este archivo como i18n_<código>.py y traducir los valores.

LANG = 'uk'
LOCALE = 'uk_UA'
DIR = 'uk'                      # carpeta donde se publica
SECTORS_DIR = 'sectors'         # carpeta de las páginas de sector dentro de DIR
PRIVACY = 'privacy.html'
RTL = False                     # True solo para idiomas de derecha a izquierda (árabe)
JSONLD = {'country': 'Іспанія', 'knows': ['Автоматизація ресурсів', 'Автоматизація процесів', 'Прикладний штучний інтелект', 'Інтеграція інструментів']}

# Contacto mientras Fini no esté disponible en este idioma
CONTACT_TALK = "mailto:info@skurx.es?subject=%D0%9F%D0%BE%D0%B3%D0%BE%D0%B2%D0%BE%D1%80%D1%96%D0%BC%D0%BE%20-%20SKURX%20SYSTEMS"
CONTACT_AUDIT = "mailto:info@skurx.es?subject=%D0%9F%D0%BE%D1%87%D0%B0%D1%82%D0%BA%D0%BE%D0%B2%D0%B8%D0%B9%20%D0%BE%D0%BF%D0%B5%D1%80%D0%B0%D1%86%D1%96%D0%B9%D0%BD%D0%B8%D0%B9%20%D0%B0%D1%83%D0%B4%D0%B8%D1%82%20-%20SKURX%20SYSTEMS"

# ---------------------------------------------------------------- Comunes
COMMON = {
    'Siguiente sección': 'Наступний розділ',
    'Volver a la página principal': 'Повернутися на головну',
    'Volver arriba': 'Нагору',
    'Saltar al contenido': 'Перейти до змісту',
    'CAPACIDAD LIBERADA': 'ВИВІЛЬНЕНИЙ РЕСУРС',
    'Quiénes somos': 'Про нас',
    'Qué hacemos': 'Що ми робимо',
    'Cómo lo hacemos': 'Як ми працюємо',
    'Sectores': 'Галузі',
    'Hablemos': 'Поговорімо',
    'SKURX SYSTEMS - AUTOMATIZACIÓN DE RECURSOS': 'SKURX SYSTEMS - АВТОМАТИЗАЦІЯ РЕСУРСІВ',
    'Privacidad': 'Конфіденційність',
    'El trabajo bien hecho': 'Добре зроблена робота',
    'no hace ruido.': 'не здіймає шуму.',
    'Todo sigue en marcha, aunque ya no quede nadie en la oficina.': 'Усе працює далі, навіть коли в офісі вже нікого немає.',
    'SKURX SYSTEMS, inicio': 'SKURX SYSTEMS, головна',
    'Navegación principal': 'Основна навігація',
    'Idioma': 'Мова',
}

# ---------------------------------------------------------------- Portada
HOME = {
    'SKURX SYSTEMS | Automatización de Recursos': 'SKURX SYSTEMS | Автоматизація ресурсів',
    'SKURX SYSTEMS libera la capacidad que las empresas pierden en trabajo manual con automatización, conexión de herramientas e IA aplicada. Para empresas de toda España.':
        'SKURX SYSTEMS вивільняє ресурс, який компанії втрачають на ручній роботі, за допомогою автоматизації, інтеграції інструментів і прикладного ШІ. Для компаній по всій Іспанії.',
    'SKURX SYSTEMS — Comprender antes de proponer.': 'SKURX SYSTEMS — Зрозуміти, перш ніж пропонувати.',
    'AUTOMATIZACIÓN DE RECURSOS': 'АВТОМАТИЗАЦІЯ РЕСУРСІВ',
    'Comprender antes de proponer.': 'Зрозуміти, перш ніж пропонувати.',
    'La mayoría de las empresas no necesitan más herramientas. Necesitan saber dónde se les escapa el tiempo, la información y la atención.':
        'Більшості компаній не потрібні нові інструменти. Їм потрібно знати, куди зникають їхні час, інформація та увага.',
    'SKURX SYSTEMS identifica dónde se pierde capacidad y la convierte en sistemas de trabajo más claros, conectados y eficientes.':
        'SKURX SYSTEMS визначає, де втрачається ресурс, і перетворює його на чіткіші, пов’язані та ефективніші робочі процеси.',
    'Tareas manuales': 'Ручні завдання',
    'Información dispersa': 'Розпорошена інформація',
    'Herramientas aisladas': 'Роз’єднані інструменти',
    'Seguimiento pendiente': 'Незавершений супровід',
    'Datos copiados a mano': 'Дані, скопійовані вручну',
    'Dependencia de personas': 'Залежність від людей',
    'QUÉ HACEMOS': 'ЩО МИ РОБИМО',
    'De la fricción': 'Від тертя',
    'a la': 'до',
    'capacidad.': 'ресурсу.',
    'Detectamos dónde pierde capacidad tu empresa y la liberamos con automatización, herramientas conectadas e inteligencia artificial aplicada donde tiene sentido.':
        'Ми визначаємо, де ваша компанія втрачає ресурс, і вивільняємо його за допомогою автоматизації, пов’язаних інструментів і штучного інтелекту там, де це має сенс.',
    'Flujos de trabajo dispersos que convergen en capacidad real.': 'Розрізнені робочі процеси, що сходяться в реальний ресурс.',
    'NUESTROS SERVICIOS': 'НАШІ ПОСЛУГИ',
    'La herramienta viene después.': 'Інструмент — потім.',
    'Automatización': 'Автоматизація',
    'Convertimos las tareas repetitivas en procesos automáticos, con las reglas que definimos contigo.':
        'Ми перетворюємо рутинні завдання на автоматичні процеси за правилами, які визначаємо разом із вами.',
    'IA aplicada': 'Прикладний ШІ',
    'Para lo que una regla no resuelve: la IA potencia a tu equipo, no lo sustituye.':
        'Для того, що не розв’язати правилом: ШІ підсилює вашу команду, а не замінює її.',
    'Conexión de herramientas': 'Інтеграція інструментів',
    'Conectamos tus herramientas para que la información pase de una a otra sin que nadie intervenga.':
        'Ми поєднуємо ваші інструменти, щоб інформація переходила з одного в інший без чиєїсь участі.',
    'CÓMO LO HACEMOS': 'ЯК МИ ПРАЦЮЄМО',
    'Primero comprender.': 'Спершу зрозуміти.',
    'Después': 'Потім',
    'intervenir.': 'діяти.',
    'No partimos de una tecnología, sino de una pregunta: ¿dónde está perdiendo capacidad tu empresa y por qué?':
        'Ми починаємо не з технології, а з питання: де ваша компанія втрачає ресурс і чому?',
    'Entender': 'Зрозуміти',
    'Conocemos tu empresa desde dentro, observando cómo trabaja tu equipo cada día.':
        'Ми знайомимося з вашою компанією зсередини й спостерігаємо, як ваша команда працює щодня.',
    'Analizar': 'Проаналізувати',
    'Localizamos dónde se pierde tiempo, información o clientes potenciales, y por qué.':
        'Ми знаходимо, де втрачаються час, інформація чи потенційні клієнти, і чому.',
    'Proponer': 'Запропонувати',
    'Te decimos qué cambiaríamos y qué no merece la pena tocar.': 'Ми кажемо, що змінили б, а чого краще не чіпати.',
    'Implantar': 'Впровадити',
    'Lo ponemos en marcha, lo probamos contigo y lo ajustamos hasta que funcione como tu equipo necesita.':
        'Ми запускаємо рішення, тестуємо його разом із вами й налаштовуємо, доки воно не працюватиме так, як потрібно вашій команді.',
    'EL PRIMER PASO': 'ПЕРШИЙ КРОК',
    'Auditoría Operativa Inicial': 'Початковий операційний аудит',
    'En una semana analizamos cómo trabaja tu empresa y te entregamos un mapa claro: qué consume capacidad, qué se puede automatizar y en qué orden. El informe es tuyo, decidas lo que decidas.':
        'За тиждень ми аналізуємо, як працює ваша компанія, і передаємо вам чітку карту: що забирає ресурс, що можна автоматизувати і в якому порядку. Звіт залишається у вас, хоч би яке рішення ви ухвалили.',
    'Solicitar auditoría': 'Замовити аудит',
    'Documentado': 'Задокументовано',
    'Cada flujo explicado en lenguaje claro.': 'Кожен процес описано зрозумілою мовою.',
    'A nombre de tu empresa': 'На ім’я вашої компанії',
    'Cuentas, herramientas y datos son tuyos.': 'Облікові записи, інструменти й дані належать вам.',
    'Auditable': 'Прозоро',
    'Puedes ver qué ha hecho cada automatización y cuándo.': 'Ви бачите, що і коли зробила кожна автоматизація.',
    'Sin dependencia': 'Без прив’язки',
    'Si dejamos de trabajar juntos, todo sigue siendo tuyo.': 'Якщо ми припинимо співпрацю, усе залишиться вашим.',
    'EJEMPLOS POR SECTOR': 'ПРИКЛАДИ ЗА ГАЛУЗЯМИ',
    'Cómo se ve en la práctica.': 'Як це виглядає на практиці.',
    'Escenarios ilustrativos basados en situaciones habituales. Trabajamos con empresas de cualquier sector, en toda España.':
        'Ілюстративні сценарії на основі типових ситуацій. Ми працюємо з компаніями будь-якої галузі по всій Іспанії.',
    'INMOBILIARIAS': 'АГЕНТСТВА НЕРУХОМОСТІ',
    'Cada consulta sin respuesta es una visita que no ocurre.': 'Кожен запит без відповіді — це перегляд, який не відбудеться.',
    'Entra una consulta desde un portal.': 'Із порталу надходить запит.',
    'Recibe respuesta con la información del inmueble.': 'Клієнт отримує відповідь з інформацією про об’єкт.',
    'Queda registrada y asignada a un agente.': 'Запит реєструється й передається агентові.',
    'El agente empieza el día con el seguimiento preparado.': 'Агент починає день із готовим планом подальших дій.',
    'GESTORÍAS': 'БУХГАЛТЕРСЬКІ ФІРМИ',
    'Menos tiempo persiguiendo papeles. Más tiempo asesorando.': 'Менше часу на збирання паперів. Більше — на консультації.',
    'Día 1': 'День 1',
    'Se pide al cliente la documentación que falta.': 'Клієнтові надсилають запит на документи, яких бракує.',
    'Día 3': 'День 3',
    'Si no ha llegado, sale un recordatorio.': 'Якщо їх досі немає, надходить нагадування.',
    'Al llegar': 'Після отримання',
    'Se clasifica y se archiva en su expediente.': 'Документи сортуються й зберігаються у справі клієнта.',
    'Listo': 'Готово',
    'El gestor recibe el aviso: expediente completo.': 'Бухгалтер отримує сповіщення: справа укомплектована.',
    'AUTOMOCIÓN': 'АВТОБІЗНЕС',
    'Un interesado que espera es un coche que se vende en otro sitio.': 'Покупець, який чекає, — це авто, продане деінде.',
    'Consulta sobre un vehículo desde un portal.': 'Із порталу надходить запит про автомобіль.',
    'Respuesta con ficha, precio y opción de cita.': 'Відповідь з характеристиками, ціною та можливістю записатися.',
    'Se registra y se asigna a un comercial.': 'Запит реєструється й передається менеджерові з продажу.',
    'Día antes': 'Напередодні',
    'Recordatorio automático de la prueba o la visita.': 'Автоматичне нагадування про тест-драйв або візит.',
    'MÁS SECTORES': 'ІНШІ ГАЛУЗІ',
}

# ---------------------------------------------------------------- Privacidad
PRIVACY_TEXT = {
    'Política de privacidad | SKURX SYSTEMS': 'Політика конфіденційності | SKURX SYSTEMS',
    'Cómo trata SKURX SYSTEMS los datos que compartes a través de skurx.es y de su asistente Fini.':
        'Як SKURX SYSTEMS обробляє дані, які ви надаєте через skurx.es.',
    'Volver': 'Назад',
    'INFORMACIÓN LEGAL': 'ПРАВОВА ІНФОРМАЦІЯ',
    'Política de privacidad': 'Політика конфіденційності',
    'Última actualización: 26 de septiembre de 2026': 'Останнє оновлення: 27 вересня 2026 року',
    'Quién es el responsable': 'Хто відповідає за дані',
    'El responsable del tratamiento de tus datos es ': 'Володільцем ваших персональних даних є ',
    ', que desarrolla su actividad bajo el nombre comercial ': ', який веде діяльність під комерційною назвою ',
    '. Para cualquier cuestión sobre tus datos puedes escribir a ': '. З будь-яких питань щодо ваших даних пишіть на ',
    'Qué datos tratamos': 'Які дані ми обробляємо',
    'Solo los que tú decides compartir con nosotros:': 'Лише ті, якими ви вирішите з нами поділитися:',
    'A través de Fini': 'Через Fini',
    ', el asistente de la web: tu nombre, la forma de contacto que elijas (correo o teléfono), tu horario preferido y lo que nos cuentes sobre tu empresa y tu situación, junto con la conversación completa.':
        ', асистента сайту (наразі лише іспанською мовою): ваше ім’я, обраний спосіб зв’язку (електронна пошта або телефон), зручний для вас час і те, що ви розповісте про свою компанію та ситуацію, разом з усією розмовою.',
    'Por correo electrónico': 'Електронною поштою',
    ': los datos que incluyas en tu mensaje.': ': дані, які ви вкажете у своєму листі.',
    'No te pedimos datos especialmente sensibles. Te rogamos que no los incluyas en la conversación.':
        'Ми не запитуємо особливо чутливих даних. Просимо не вказувати їх у своїх повідомленнях.',
    'Para qué los usamos': 'Для чого ми їх використовуємо',
    'Para atender tu consulta, ponernos en contacto contigo y, si lo solicitas, preparar una propuesta. No los usamos para enviarte publicidad ni los vendemos o cedemos a terceros con fines comerciales.':
        'Щоб відповісти на ваш запит, зв’язатися з вами і, якщо ви попросите, підготувати пропозицію. Ми не використовуємо їх для надсилання реклами, не продаємо й не передаємо третім особам з комерційною метою.',
    'Base legal': 'Правова підстава',
    'Tratamos tus datos porque tú nos los envías voluntariamente para que te contactemos (tu consentimiento) y, cuando corresponde, para aplicar a petición tuya medidas previas a un posible contrato.':
        'Ми обробляємо ваші дані, тому що ви добровільно надсилаєте їх нам, щоб ми з вами зв’язалися (ваша згода), а також, за потреби, щоб на ваше прохання вжити заходів, які передують можливому договору.',
    'Cuánto tiempo los conservamos': 'Як довго ми їх зберігаємо',
    'El tiempo necesario para atender tu consulta. Si no llegamos a trabajar juntos, los eliminamos como máximo doce meses después del último contacto. Si iniciamos una relación profesional, los conservaremos mientras dure y durante los plazos que exija la ley.':
        'Стільки, скільки потрібно, щоб опрацювати ваш запит. Якщо співпраця не розпочнеться, ми видаляємо їх не пізніше ніж через дванадцять місяців після останнього контакту. Якщо ми розпочнемо професійні відносини, зберігатимемо їх упродовж усієї співпраці та протягом строків, установлених законом.',
    'Quién más interviene': 'Хто ще бере участь',
    'Para que la web y el asistente funcionen nos apoyamos en proveedores que solo tratan los datos para prestarnos su servicio:':
        'Для роботи сайту й асистента ми користуємося послугами постачальників, які обробляють дані лише для того, щоб надавати нам свої послуги:',
    ': envía a nuestro correo la conversación que confirmas en Fini.': ': надсилає на нашу пошту розмову, яку ви підтверджуєте у Fini.',
    ': aloja el correo info@skurx.es.': ': обслуговує поштову скриньку info@skurx.es.',
    ': aloja la web y puede registrar datos técnicos de conexión, como la dirección IP, por motivos de seguridad.':
        ': розміщує сайт і з міркувань безпеки може фіксувати технічні дані підключення, як-от IP-адресу.',
    'Algunos de estos proveedores pueden tratar datos fuera del Espacio Económico Europeo. En ese caso, la transferencia debe ampararse en las garantías que prevé el Reglamento General de Protección de Datos.':
        'Деякі з цих постачальників можуть обробляти дані за межами Європейської економічної зони. У такому разі передавання даних має супроводжуватися гарантіями, передбаченими Загальним регламентом про захист даних (GDPR).',
    'Lo que se guarda en tu navegador': 'Що зберігається у вашому браузері',
    'Fini guarda la conversación en tu propio navegador durante un máximo de treinta días, para que puedas retomarla si vuelves. Esa información no nos llega hasta que confirmas el envío, y puedes borrarla en cualquier momento eliminando los datos del sitio en tu navegador. La web no utiliza cookies de publicidad ni de analítica.':
        'Fini зберігає розмову у вашому браузері до тридцяти днів, щоб ви могли продовжити її, коли повернетеся. Ця інформація не надходить до нас, доки ви не підтвердите надсилання, і ви можете будь-коли видалити її, очистивши дані сайту в браузері. Сайт не використовує рекламних чи аналітичних файлів cookie.',
    'Tus derechos': 'Ваші права',
    'Puedes pedirnos acceder a tus datos, corregirlos, eliminarlos, oponerte a su tratamiento, limitarlo, recibirlos en un formato portable o retirar tu consentimiento en cualquier momento. Solo tienes que escribir a ':
        'Ви можете будь-коли попросити нас надати доступ до ваших даних, виправити чи видалити їх, заперечити проти їх обробки або обмежити її, отримати їх у переносному форматі чи відкликати свою згоду. Просто напишіть на ',
    'Si consideras que no hemos tratado bien tus datos, puedes presentar una reclamación ante la Agencia Española de Protección de Datos (':
        'Якщо ви вважаєте, що ми неналежно обробили ваші дані, ви можете подати скаргу до Іспанського агентства із захисту даних (',
    'Cambios en esta política': 'Зміни до цієї політики',
    'Si cambiamos algo relevante, lo actualizaremos en esta página indicando la fecha de la última revisión.':
        'Якщо ми змінимо щось суттєве, то оновимо цю сторінку й зазначимо дату останньої редакції.',
}

# ---------------------------------------------------------------- Páginas de sector (plantilla)
SECTOR_UI = {
    'title': 'Автоматизація для {plural} | SKURX SYSTEMS',
    'desc': 'Автоматизація та ШІ для {plural}. {desc}',
    'crumb': 'ГАЛУЗІ',
    'pains_eyebrow': 'ДЕ ВТРАЧАЄТЬСЯ РЕСУРС',
    'fix': 'ЩО МИ РОБИМО',
    'flow_eyebrow': 'НА ПРАКТИЦІ',
    'flow_h2': 'Звичайний день,<br>коли система працює.',
    'flow_note': 'Ілюстративний сценарій на основі типових ситуацій.',
    'control_eyebrow': 'ЖОДНИХ ЧОРНИХ СКРИНЬОК',
    'audit_h3': 'Початковий операційний аудит для {plural}',
    'audit_tail': 'Ми передаємо вам чітку карту: що автоматизувати і в якому порядку. Звіт залишається у вас, хоч би яке рішення ви ухвалили.',
    'audit_btn': 'Замовити аудит',
    'ba_before_alt': 'До: вітальня і кухня старої квартири, розділені перегородкою, з темними меблями, застарілою плиткою та слабким освітленням.',
    'ba_after_alt': 'Після: та сама квартира після ремонту, з відкритою кухнею-вітальнею, острівцем, дерев’яною підлогою та теплим світлом.',
    'ba_before': 'ДО', 'ba_after': 'ПІСЛЯ',
    'ba_aria': 'Порівняти «до» і «після»',
    'ba_caption': 'Перетягніть, щоб порівняти. Приклад зображення, створеного комп’ютером.',
}

# ---------------------------------------------------------------- Ilustración de la portada
SVG = {
    'Tareas manuales': 'Ручні завдання',
    'Información dispersa': 'Розпорошена інформація',
    'Herramientas aisladas': 'Роз’єднані інструменти',
    'Seguimiento pendiente': 'Незавершений супровід',
    'Datos copiados a mano': 'Дані, скопійовані вручну',
    'Dependencia de personas': 'Залежність від людей',
    'CAPACIDAD': 'РЕАЛЬНИЙ',
    'REAL': 'РЕСУРС',
}
