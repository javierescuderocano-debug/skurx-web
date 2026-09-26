// Fini, la asistente virtual de SKURX: conversación guiada dentro del panel «Hablemos».
// Paso 1 (sin IA): guion propio que adapta las preguntas a lo que cuenta el usuario.
(function () {
  var CONFIG = {
    // Activado el 26/09/2026, con la Política de privacidad publicada en /privacidad.html
    enabled: true,
    // Clave gratuita de https://web3forms.com (asociada a info@skurx.es). Vacía = modo prueba, no se envía nada.
    web3formsKey: '413a9355-a4b8-472a-a87e-9cbd9b932651',
    storageKey: 'skurx-fini-v1',
    // La conversación se guarda en el navegador del usuario para que pueda retomarla otro día.
    keepDays: 30
  };

  var panel = document.getElementById('panel-contacto');
  var params = new URLSearchParams(window.location.search);
  var enabled = CONFIG.enabled || params.get('fini') === '1';
  if (!panel || !enabled || typeof panel.showModal !== 'function') return;

  var log = panel.querySelector('.chat-log');
  var quick = panel.querySelector('.chat-quick');
  var form = panel.querySelector('.chat-form');
  var input = panel.querySelector('#chat-input');
  var sendBtn = panel.querySelector('.chat-send');
  var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  // ---------- Estado ----------
  var state = load() || fresh();
  var busy = false;

  function fresh() {
    return { step: 'inicio', data: {}, history: [], asked: {}, topic: null };
  }
  function save() {
    state.savedAt = Date.now();
    try { localStorage.setItem(CONFIG.storageKey, JSON.stringify(state)); } catch (e) {}
  }
  function load() {
    try {
      var saved = JSON.parse(localStorage.getItem(CONFIG.storageKey));
      if (saved && Date.now() - (saved.savedAt || 0) < CONFIG.keepDays * 864e5) return saved;
      localStorage.removeItem(CONFIG.storageKey);
    } catch (e) {}
    return null;
  }
  // ¿Es la primera vez que se abre el panel en esta visita? Sirve para dar la bienvenida de vuelta.
  function isReturnVisit() {
    try {
      if (sessionStorage.getItem(CONFIG.storageKey + '-visit')) return false;
      sessionStorage.setItem(CONFIG.storageKey + '-visit', '1');
    } catch (e) {}
    return true;
  }

  // ---------- Textos ----------
  var GREETING = [
    'Hola, soy Fini, la asistente virtual de SKURX SYSTEMS. Es un placer saludarte.',
    '¿Cómo te llamas? Así sé cómo dirigirme a ti.'
  ];

  // Al abrir Fini desde el botón «Solicitar auditoría».
  var AUDIT = 'Auditoría Operativa Inicial';
  var GREETING_AUDIT = [
    'Hola, soy Fini, la asistente virtual de SKURX SYSTEMS.',
    'Veo que te interesa la Auditoría Operativa Inicial. Te hago unas preguntas rápidas para que el equipo la prepare con tu caso.',
    '¿Cómo te llamas? Así sé cómo dirigirme a ti.'
  ];

  // Tras conocer el nombre (o si prefiere no darlo).
  var INTRO = [
    'Muchas empresas llegan hasta aquí porque sienten que el día a día se les come el tiempo: tareas que se repiten, información repartida en mil sitios, cosas que se quedan pendientes…',
    'Si algo de esto te suena, cuéntame qué es lo que más tiempo os consume ahora mismo.'
  ];

  var HOW_WE_WORK = [
    'Trabajamos en cuatro pasos. Primero entendemos cómo funciona de verdad la empresa, hablando con quien hace el trabajo.',
    'Después analizamos dónde se está perdiendo tiempo o información, y solo entonces proponemos un cambio, si merece la pena. Si no lo merece, te lo decimos.',
    'Y por último lo ponemos en marcha y comprobamos que funciona en el día a día.'
  ];

  var TOPICS = {
    atencion: {
      re: /client|consulta|correo|e-?mail|mail|whatsapp|llamad|tel[eé]fono|\blead|contact|atenci[oó]n|respond|mensaje|incidenc|aver[ií]a|vecin|hu[eé]sped|escrib|pregunt|dudas|llaman|queja|interesad|solicitud/i,
      ack: 'Es de lo más habitual: las consultas llegan por varios sitios y darles respuesta a tiempo se vuelve una tarea en sí misma.',
      ask: 'Cuando entra una consulta, ¿cómo os llega normalmente y quién se encarga de darle respuesta?',
      // Pregunta doble: si solo responde a una parte, Fini pregunta por la otra.
      parts: [
        { re: /correo|mail|whatsapp|tel[eé]fono|llamad|\bweb\b|formulario|portal|redes|instagram|facebook|linkedin|idealista|fotocasa|habitaclia|milanuncios|google|chat|presencial|mostrador|\bapp\b/i,
          follow: '¿Y por dónde os suelen llegar? Correo, teléfono, WhatsApp, la web…' },
        { re: /\byo\b|nosotr|equipo|persona|compa[nñ]er|recepci|comercial|agente|quien (puede|est[eé]|pilla)|nadie|cada uno|encarg|secretari|gerente|due[nñ]|socio|jef[ea]|administrativ|atiend|me ocupo|lo llevo|lo llevamos|lo hace|las? (lleva|coge|contesta|responde)|contesto|respondo|respondemos|contestamos/i,
          follow: '¿Y quién se encarga de responderlas?' }
      ]
    },
    administracion: {
      re: /factur|presupuest|albar[aá]n|pedido|document|contrat|n[oó]mina|contab|cobro|pago|papeleo|papel(es)?\b|trimestr|impuest|declaraci|pag(ar|uen|an)\b|impag|deud|moros|\bpartes?\b|teclea|matr[ií]cul|inscripci|n[oó]minas?|fichaj|control horario/i,
      ack: 'Ese tipo de trabajo consume muchas horas sin que apenas se note, porque se hace un poco cada día.',
      ask: '¿Ese trabajo lo hacéis a mano cada vez, o hay alguna parte que ya esté automatizada?'
    },
    informacion: {
      re: /excel|hoja|dato|copi|informe|inventario|stock|base de datos|duplic|actualiz|programa|herramient|crm|erp/i,
      ack: 'Lo entiendo. Cuando el mismo dato vive en varios sitios, alguien acaba copiándolo a mano y es fácil que se desordene.',
      ask: '¿Con qué herramientas trabajáis ahora mismo? Aunque sea Excel y el correo, me sirve.'
    },
    agenda: {
      re: /\bcitas?\b|reserva|agenda|\bturnos?\b|cuadrante|hueco|no (vienen|se presentan|aparecen)|cancela|\bvisitas\b/i,
      ack: 'Organizar la agenda se come mucho más tiempo del que parece: pedir, confirmar, recordar y recolocar cada vez que algo cambia.',
      ask: '¿Cómo lo gestionáis ahora: por dónde llegan las peticiones y quién se encarga de organizarlo?',
      parts: null
    },
    seguimiento: {
      re: /seguimiento|olvid|pendient|se (nos )?pasa|se (nos )?pierden?\b|recordar|aviso|plazo|retras|\bbajas?\b|dan de baja|renovaci|vencimient|abandon|dejan de venir/i,
      ack: 'Eso pasa mucho: no es falta de ganas, es que hay demasiadas cosas que recordar a la vez.',
      ask: '¿Qué suele quedarse pendiente con más frecuencia, y qué consecuencias tiene cuando pasa?',
      parts: [
        { re: /perd|client|dinero|venta|queja|retras|multa|enfad|oportunidad|cobr|problema|reclam|consecuencia|nada grave|no pasa nada|se enfr[ií]a|se va|se (han )?ido|se marchan|ya es tarde/i,
          follow: '¿Y qué pasa cuando se queda pendiente? ¿Se pierde algún cliente, se retrasa algo…?' }
      ]
    }
  };

  TOPICS.agenda.parts = TOPICS.atencion.parts;

  var ACKS = ['Entiendo.', 'Tiene sentido.', 'Vale, me hago una idea.', 'Gracias, eso me ayuda mucho.'];
  var TOOLS = /whatsapp business|google sheets|google calendar|clinic ?cloud|programa de (gesti[oó]n|facturaci[oó]n|contabilidad)|\bcorreos?\b|\bexcel\b|\bexell?\b|\bword\b|\bsap\b|inmovilla|witei|gesden|gesfincas|smoobu|lodgify|avantio|hostaway|trainingym|wodbuster|mindbody|pipedrive|monday|clickup|prestashop|magento|calendly|contaplus|instagram|hojas de c[aá]lculo|gmail|outlook|whatsapp|holded|a3|sage|factusol|odoo|hubspot|salesforce|notion|trello|asana|drive|dropbox|shopify|woocommerce|wordpress|teams|slack|zoho|quickbooks|contasol|coches\.net|wallapop|milanuncios|idealista|fotocasa|habitaclia|booking|airbnb|google analytics|\bdms\b|\bcrm\b|\berp\b/gi;

  var QUESTIONS = {
    problema: 'Cuéntame, ¿qué es lo que más tiempo os consume ahora mismo?',
    herramientas: '¿Y con qué herramientas trabajáis en el día a día? Aunque sea Excel y el correo, me sirve.',
    tiempo: '¿Cuánto tiempo diríais que se os va en esto a la semana, más o menos?',
    empresa: 'Para situarme mejor: ¿a qué se dedica tu empresa y cuántas personas sois, más o menos?',
    urgencia: '¿Es algo que os preocupa ya, o lo estáis explorando con calma?',
    nombre: 'Me gustaría que alguien del equipo lo revise contigo personalmente. ¿Cómo te llamas?',
    contacto: '¿Dónde prefieres que te contactemos? Puedes dejarme un email o un teléfono.',
    horario: '¿Hay algún momento del día en el que te venga mejor que te contactemos?'
  };

  // ---------- Utilidades ----------
  function pick(list) { return list[Math.floor(Math.random() * list.length)]; }
  function words(text) { return text.trim().split(/\s+/).filter(Boolean).length; }
  function wait(ms) { return new Promise(function (r) { setTimeout(r, reduceMotion ? 0 : ms); }); }
  function typingTime(text) { return 450 + Math.min(text.length * 16, 1700); }
  function capitalize(s) { return s.charAt(0).toUpperCase() + s.slice(1).toLowerCase(); }

  function scrollDown() { log.scrollTop = log.scrollHeight; }

  function render(msg) {
    var row = document.createElement('div');
    row.className = 'chat-msg ' + (msg.who === 'fini' ? 'from-fini' : 'from-user');
    var last = log.lastElementChild;
    if (msg.who === 'fini' && !(last && last.classList.contains('from-fini'))) row.classList.add('first');
    var bubble = document.createElement('div');
    bubble.className = 'chat-bubble';
    if (msg.list) {
      var p = document.createElement('p');
      p.textContent = msg.text;
      var ul = document.createElement('ul');
      msg.list.forEach(function (item) {
        var li = document.createElement('li');
        var b = document.createElement('b');
        b.textContent = item[0] + ': ';
        li.appendChild(b);
        li.appendChild(document.createTextNode(item[1]));
        ul.appendChild(li);
      });
      bubble.appendChild(p);
      bubble.appendChild(ul);
    } else {
      bubble.textContent = msg.text;
    }
    row.appendChild(bubble);
    log.appendChild(row);
    scrollDown();
  }

  function push(msg) {
    state.history.push(msg);
    save();
    render(msg);
  }

  function showTyping() {
    var row = document.createElement('div');
    row.className = 'chat-msg from-fini typing';
    var last = log.lastElementChild;
    if (!(last && last.classList.contains('from-fini'))) row.classList.add('first');
    row.innerHTML = '<div class="chat-bubble" aria-label="Fini está escribiendo"><span></span><span></span><span></span></div>';
    log.appendChild(row);
    scrollDown();
    return row;
  }

  // Fini escribe uno o varios mensajes seguidos, con pausas realistas.
  async function say(texts) {
    busy = true;
    setQuick([]);
    for (var i = 0; i < texts.length; i++) {
      var msg = typeof texts[i] === 'string' ? { who: 'fini', text: texts[i] } : Object.assign({ who: 'fini' }, texts[i]);
      var dots = showTyping();
      await wait(typingTime(msg.text + (msg.list ? msg.list.join(' ') : '')));
      dots.remove();
      if (/\?/.test(msg.text)) state.lastQ = msg.text;
      push(msg);
      if (i < texts.length - 1) await wait(350);
    }
    busy = false;
  }

  // Retomar la última pregunta tras una duda del usuario: «Volviendo a tu caso, ¿…?»
  function reask() {
    var q = state.lastQ || QUESTIONS.problema;
    if (state.step === 'saludo') return q;
    q = q.replace(/^.*?(¿)/, '$1').replace(/^¿Y /, '¿');
    var lead = ['nombre', 'contacto', 'horario'].indexOf(state.step) !== -1 ? 'Como te decía, ' : 'Volviendo a tu caso, ';
    return lead + q.charAt(0) + q.charAt(1).toLowerCase() + q.slice(2);
  }

  function setQuick(options) {
    state.quick = options;
    save();
    quick.innerHTML = '';
    options.forEach(function (label) {
      var b = document.createElement('button');
      b.type = 'button';
      b.textContent = label;
      b.addEventListener('click', function () { submit(label); });
      quick.appendChild(b);
    });
    quick.hidden = options.length === 0;
    scrollDown();
  }

  async function ask(step, before) {
    state.step = step;
    save();
    var question = step === 'contacto' && state.data.preferencia === 'Llamada' ? '¿En qué teléfono te llamamos?' : QUESTIONS[step];
    if (step === 'nombre' && state.data.preferencia === 'Llamada') question = '¿Cómo te llamas?';
    await say((before || []).concat([question]));
    if (step === 'urgencia') setQuick(['Me urge', 'En los próximos meses', 'Solo estoy explorando']);
    if (step === 'horario') setQuick(['Por la mañana', 'Por la tarde', 'Me da igual']);
  }

  // ---------- Intenciones generales ----------
  var PRIVACY = /mis datos|datos personales|privacidad|rgpd|protecci[oó]n de datos|confidencial|(es|ser[aá]) seguro|seguridad|datos de (mis |los |nuestros )?(clientes|pacientes|alumnos|socios|vecinos)|para qu[eé] (quer[eé]is|necesit[aá]is) (mi|el) (email|correo|tel[eé]fono)/i;
  var INTENTS = [
    {
      re: /\b(hi|hello|my name is|i need|i want|please|thanks|thank you)\b/i,
      once: 'english',
      reply: ['Sorry, for now I can only chat in Spanish. You can write to info@skurx.es in English and the team will get back to you.', 'Si lo prefieres, seguimos en español.']
    },
    {
      re: PRIVACY,
      reply: function (text) {
        var r = ['Lo que me cuentas aquí solo lo usa el equipo de SKURX SYSTEMS para atender tu consulta, y no se cede a nadie. Tienes los detalles en la política de privacidad, enlazada justo debajo.'];
        if (/\bia\b|inteligencia artificial|automatiz/i.test(text)) r.push('Y sobre usar IA o automatizaciones con datos delicados: se puede hacer con garantías, y se decide contigo antes de tocar nada qué datos se usan, dónde se guardan y quién accede. Todo queda documentado.');
        return r;
      }
    },
    {
      re: /qu[eé] tiempo hace|el tiempo (hoy|ma[nñ]ana)|un chiste|cu[eé]ntame algo|f[uú]tbol|cu[aá]ntos a[nñ]os tienes|te gusta|est[aá]s soltera|eres guapa/i,
      reply: ['Ahí no te puedo ayudar: solo sé de cómo trabajamos en SKURX SYSTEMS.']
    },
    {
      re: /cu[aá]nto (tard|tiempo (lleva|tarda|se tarda|cuesta montar|os lleva))|en cu[aá]nto tiempo (lo|est|pod|ten)|cu[aá]ndo (estar[ií]a|podr[ií]a|lo tendr)|plazo de entrega|tardar[ií]ais/i,
      reply: ['Depende de lo que haya que montar. La Auditoría Operativa Inicial dura una semana, y al terminarla te decimos con claridad qué haríamos y cuánto llevaría cada paso.']
    },
    {
      re: /d[oó]nde (est[aá]is|sois|ten[eé]is|se encuentran|trabaj[aá]is|os encuentro)|de d[oó]nde (sois|son)|ubicaci[oó]n|vuestra oficina|en qu[eé] ciudad/i,
      reply: ['Trabajamos con empresas de toda España: en persona cuando hace falta y a distancia cuando es más práctico.']
    },
    {
      re: /(trabaj[aá]is|trabajan|os dedic[aá]is a|ayud[aá]is a) (con |para |a )?(empresas |negocios )?(peque|aut[oó]nom|pymes|grandes|cualquier)|es para (empresas|negocios) peque|sirve para (un )?aut[oó]nom/i,
      reply: ['Sí. Trabajamos sobre todo con pymes y autónomos: es justo donde cada hora que se libera se nota más.']
    },
    {
      re: /qu[eé] (es|incluye|trae)( eso de| exactamente)? (la |una |esa )?auditor|en qu[eé] consiste (la |una |esa )?auditor|auditor[ií]a[^.]{0,25}(qu[eé] es|en qu[eé] consiste|qu[eé] incluye)/i,
      reply: ['La Auditoría Operativa Inicial es el primer paso: durante una semana analizamos cómo trabaja tu empresa y te entregamos un mapa claro de qué consume capacidad, qué se puede automatizar y en qué orden.', 'El informe es tuyo, decidas lo que decidas.']
    },
    {
      re: /chat ?gpt|\bgpt\b|openai|(us[aá]is|utiliz[aá]is|trabaj[aá]is con|hac[eé]is|aplic[aá]is|meter|pon[eé]is) (la |una )?(inteligencia artificial|\bia\b)/i,
      reply: ['Sí, cuando tiene sentido. Usamos IA para lo que una regla no resuelve (entender un correo, clasificar un documento, preparar un borrador de respuesta…), siempre supervisada y para potenciar a tu equipo, no para sustituirlo.']
    },
    {
      re: /y si (luego |despu[eé]s |al final )?no (funciona|me gusta|sale bien|va bien|me convence)|garant[ií]a|qu[eé] pasa si (falla|no funciona|se rompe|algo falla)|y si (se rompe|falla)/i,
      reply: ['Antes de dejar nada en marcha lo probamos contigo y lo ajustamos hasta que funcione como necesitáis.', 'Además, todo queda documentado y a nombre de tu empresa: si algún día dejamos de trabajar juntos, sigue siendo tuyo.']
    },
    {
      once: 'web',
      re: /(necesito|quiero|busco|hac[eé]is|hacer|me hag[aá]is|renovar) (una |mi |la )?(nueva |otra )?(p[aá]gina )?web( nueva)?\s*[.!?]*$|dise[nñ]o web|p[aá]gina web nueva|(necesito|quiero) una p[aá]gina web/i,
      reply: ['Te cuento: no hacemos páginas web como tal. Lo nuestro es que lo que pasa detrás funcione solo, por ejemplo, que las consultas que llegan por la web se respondan, se registren y no se queden sin seguimiento.', 'Si hay algo de eso que os esté costando tiempo, cuéntamelo y lo vemos.']
    },
    {
      re: /auditor[ií]a/i,
      reply: function () {
        if (state.data.interes) return ['Perfecto, eso es justo lo que vamos a preparar.'];
        state.data.interes = AUDIT;
        save();
        return ['Perfecto, te ayudo con la Auditoría Operativa Inicial: en una semana analizamos cómo trabaja tu empresa y te entregamos un mapa claro de dónde se pierde capacidad.', 'Para que el equipo la prepare bien, te hago unas preguntas rápidas.'];
      }
    },
    {
      re: /c[oó]mo est[aá]s|qu[eé] tal est[aá]s|qu[eé] tal (te va|todo|el d[ií]a)|c[oó]mo te va|c[oó]mo va todo/i,
      reply: ['Muy bien, gracias por preguntar.']
    },
    {
      re: /\b(eres|sois|es esto) (un |una )?(bot|robot|m[aá]quina|ia|inteligencia|humana?|persona|real)|hablo con (un|una) (bot|m[aá]quina|persona)|qui[eé]n (va a leer|lee|leer[aá]|ve) (esto|lo que)|lo lee alguien|llega a alguien|una persona (real|de verdad)/i,
      reply: ['Soy una asistente virtual: respondo de forma automática. Todo lo que me cuentes lo revisa después una persona del equipo de SKURX SYSTEMS.']
    },
    {
      re: /cu[aá]nto (cuesta|cobr|vale|sale|costar)|es caro|\bbarato|(precio|tarifa|coste|presupuesto)s?\b[^.!]*\?|qu[eé] (precio|tarifa|coste)|(ten[eé]is|hay) (precios|tarifas)|^(precio|precios|tarifas?)\W*$/i,
      reply: ['Prefiero no darte una cifra sin conocer tu caso: cada empresa es distinta y no queremos proponerte nada que no tenga sentido.', 'Lo que sí puedo hacer es preparar tu caso para que el equipo lo valore contigo.']
    },
    {
      re: /ll[aá]madme|ll[aá]mame|que me llam[eé]is|que me llamen|me llam[aá]is|prefiero que me llam|os lo cuento por tel|mejor por tel[eé]fono|mejor hablar por tel/i,
      call: true,
      reply: ['Claro, te llamamos y nos lo cuentas directamente.']
    },
    {
      re: /hablar con (alguien|una persona|un humano|el equipo)|prefiero (llamar|hablar)|quiero (llamar|hablar con)|no quiero hablar con una m[aá]quina/i,
      reply: ['Claro. Si prefieres hablar directamente con el equipo, puedes escribirnos a info@skurx.es.', 'Y si quieres, seguimos aquí un par de minutos y dejo tu caso preparado para que te llamen ya sabiendo de qué va.']
    },
    {
      re: /c[oó]mo trabaj|vuestro proceso|qu[eé] hac[eé]is|en qu[eé] consist/i,
      reply: HOW_WE_WORK
    }
  ];


  // ---------- ¿La respuesta encaja con la pregunta? ----------
  var WORK = /empresa|negocio|trabaj|equipo|client|tarea|gesti[oó]n|proceso|tiempo|hora|semana|\bmes\b|hacemos|tenemos|llevamos|usamos|pedido|venta|compra|proveedor|emplead|oficina|tienda|servicio|proyecto|correo|excel|papel|programa|\bapp\b|\bweb\b|dato|document|factur|llamad|mensaje|reuni|informe|agenda|cita|stock|almac|contab|presupuest|seguimiento|pendiente|repet|manual|a mano|copi|organiz|coordin|turno|reserva/i;

  var FITS = {
    problema: function (t) { return WORK.test(t) || !!topicOf(t) || (words(t) >= 3 && !/\?/.test(t) && !/^(ja|je|xd|lol)/i.test(t.trim())); },
    detalle: function (t) { return (!/\?/.test(t) && words(t) >= 2) || /^(no s[eé]|ni idea|no lo s[eé]|s[ií]|no)\W*$/i.test(t.trim()) || WORK.test(t) || !!topicOf(t) || ((state.topic && TOPICS[state.topic].parts) || []).some(function (p) { return p.re.test(t); }) || /\d|cada|siempre|todos los|a veces|\byo\b|nosotros|nadie|encarg|diari|semanal/i.test(t); },
    herramientas: function (t) { TOOLS.lastIndex = 0; if (TOOLS.test(t)) { TOOLS.lastIndex = 0; return true; } TOOLS.lastIndex = 0; return (!/\?/.test(t) && words(t) <= 4) || /\b(us(o|a|amos|an)|utiliz|trabaj(o|amos) con|tenemos|llevamos|nos apa[nñ]amos)\b|programa|aplicaci|\bapp\b|software|papel|libreta|agenda|nada|ninguna|a mano|correo|mail|m[oó]vil|ordenador|crm|erp|\bweb\b|herramient|sistema|hoja|tablet|plataforma/i.test(t); },
    tiempo: function (t) { return /\d|hora|\boras\b|minut|d[ií]a|semana|\bmes|mucho|poco|bastante|rato|jornada|nada|medio|media|ni idea|no s[eé]|no lo s[eé]|no sabr|depende|un par|varias|much[ií]simo|cuantas|cu[aá]ntas/i.test(t); },
    empresa: function (t) { return WORK.test(t) || /solo yo|yo solo|\by (una|un|dos|tres|mi)\b|chic[oa]|socio|mi (mujer|marido|herman|pareja)|nosotr|profesor|t[eé]cnicos|comunidades|apartamentos|\d|somos|sector|dedica|aut[oó]nom|freelance|pyme|tienda|restaurante|\bbar\b|cl[ií]nica|despacho|taller|agencia|consultor|distribu|fabric|constru|inmobiliari|hotel|academia|asesor|comercio|e-?commerce|log[ií]stic|transporte|abogad|dental|gimnasio|peluquer|estudio|colegio|\bong\b|asociaci|sol[oa]\b|psic[oó]log|m[eé]dic|fisio|arquitect|dise[nñ]|fot[oó]graf|consult/i.test(t) || (!/\?/.test(t) && words(t) <= 8); }
  };

  var CLARIFY = {
    problema: 'Creo que no te he entendido del todo. ¿Me cuentas qué parte del trabajo diario os consume más tiempo? Por ejemplo, responder a clientes, hacer facturas o pasar datos de un sitio a otro.',
    detalle: 'Perdona, no sé si te he seguido. Me refería a cómo es ese trabajo en el día a día: cada cuánto ocurre, quién lo hace o cómo lo hacéis ahora.',
    herramientas: 'Perdona, creo que no me he explicado bien. Me refería a los programas o aplicaciones que usáis: Excel, el correo, algún programa de gestión… Aunque sea papel, también me sirve.',
    tiempo: 'No hace falta que sea exacto. ¿Diríais que son unas pocas horas a la semana, o más bien varias horas al día?',
    empresa: 'Perdona, no te he entendido bien. ¿A qué se dedica tu empresa, y cuántas personas sois más o menos?'
  };

  function topicOf(text) {
    var found = null;
    // Orden de prioridad: lo más concreto primero («las facturas llegan por correo» es administración).
    ['seguimiento', 'agenda', 'administracion', 'informacion', 'atencion'].some(function (k) {
      if (TOPICS[k].re.test(text)) { found = k; return true; }
      return false;
    });
    return found;
  }

  // «Hola, me llamo Javier» / «soy Javier»: devuelve el nombre y el resto del mensaje.
  var NOT_A_NAME = /^(el|la|los|las|un|una|de|del|muy|nuevo|nueva|aut[oó]nom|gerente|due[nñ]|propietari|responsable|jefe|jefa|director|administrador|encargad|socio|socia|comercial|t[eé]cnic|de)$/i;
  function introduction(text) {
    var m = text.match(/(?:me llamo|me yamo|mi nombre es|my name is|^(?:(?:hola|buenas|hi|hello)[,.!]?\s*)?soy)\s+([a-záéíóúüñ]+)(\s+[a-záéíóúüñ]+)?/i);
    if (!m || NOT_A_NAME.test(m[1]) || m[1].length < 2) return null;
    var second = m[2] && isKnownName(m[2].trim()) && isKnownName(m[1]) ? m[2].trim() : '';
    var used = m[0].length - (m[2] && !second ? m[2].length : 0);
    var rest = text.slice(m.index + used).replace(/^[\s,.;:!y]+/i, '');
    return { name: accent(capitalize(m[1])) + (second ? ' ' + accent(capitalize(second)) : ''), rest: rest };
  }

  var META = /dado por vencid|te (rindes|has rendido)|no me entiendes|no entiendes nada|no te enteras|eres tonta|qu[eé] torpe|no sirves/i;

  // Cómo dirigirse a la persona: el nombre de pila (o compuesto, «María José»), con sus tildes.
  var ACCENTS = { maria: 'María', jose: 'José', jesus: 'Jesús', angel: 'Ángel', angela: 'Ángela', angeles: 'Ángeles', ines: 'Inés', lucia: 'Lucía', sofia: 'Sofía', raul: 'Raúl', ramon: 'Ramón', ruben: 'Rubén', oscar: 'Óscar', alvaro: 'Álvaro', andres: 'Andrés', joaquin: 'Joaquín', julian: 'Julián', martin: 'Martín', nicolas: 'Nicolás', tomas: 'Tomás', sebastian: 'Sebastián', hector: 'Héctor', ivan: 'Iván', cesar: 'César', victor: 'Víctor', belen: 'Belén', rocio: 'Rocío', veronica: 'Verónica', monica: 'Mónica', fatima: 'Fátima', estefania: 'Estefanía', concepcion: 'Concepción', asuncion: 'Asunción', matias: 'Matías', adrian: 'Adrián', agustin: 'Agustín', benjamin: 'Benjamín', simon: 'Simón', lidia: 'Lidia' };
  function accent(word) {
    return ACCENTS[word.toLowerCase()] || word;
  }
  function trato() {
    var parts = (state.data.nombre || '').split(' ').filter(Boolean);
    if (!parts.length) return '';
    var first = accent(parts[0]);
    if (parts[1] && isKnownName(parts[1]) && isKnownName(parts[0])) return first + ' ' + accent(parts[1]);
    return first;
  }

  // ---------- Conversación ----------
  async function handle(text) {
    var step = state.step;

    if (step !== 'fin' && META.test(text)) {
      await say(['Para nada. Solo quiero asegurarme de que el equipo reciba bien tu caso.']);
      return say([reask()]);
    }
    var early = ['saludo', 'inicio', 'problema', 'detalle', 'herramientas', 'tiempo', 'empresa', 'urgencia'].indexOf(step) !== -1;
    var hasContact = /[^\s@]+@[^\s@]+\.[^\s@]{2,}|\+?\d[\d\s.-]{7,}\d/.test(text);
    var late = ['nombre', 'contacto', 'horario'].indexOf(step) !== -1 && !hasContact;
    var dataStep = ['detalle', 'herramientas', 'tiempo', 'empresa', 'urgencia'].indexOf(step) !== -1;
    var questionLike = /\?|^¿/.test(text.trim()) || /^(qu[eé]|c[oó]mo|cu[aá]nto|cu[aá]ndo|d[oó]nde|qui[eé]n|por qu[eé]|pod[eé]is|ten[eé]is|hac[eé]is|us[aá]is|trabaj[aá]is|sois|eres|y si)\b/i.test(text.trim());

    if (early || late) {
      for (var i = 0; i < INTENTS.length; i++) {
        if (INTENTS[i].re.test(text)) {
          if (dataStep && !questionLike && !INTENTS[i].call && !INTENTS[i].once && !/hablar con|m\[aá\]quina/.test(String(INTENTS[i].re))) continue;
          if (INTENTS[i].once) {
            if (state.asked[INTENTS[i].once]) continue;
            state.asked[INTENTS[i].once] = true;
          }
          if (late && !INTENTS[i].call && INTENTS[i].reply !== HOW_WE_WORK && !/tard|d\[oó\]nde|bot|garant/.test(String(INTENTS[i].re)) && INTENTS[i].re !== PRIVACY) continue;
          var isHow = INTENTS[i].reply === HOW_WE_WORK;
          var intentReply = typeof INTENTS[i].reply === 'function' ? INTENTS[i].reply(text) : INTENTS[i].reply;
          if (INTENTS[i].call) {
            state.data.preferencia = 'Llamada';
            if (!state.data.problema) state.data.problema = 'Prefiere contarlo por teléfono';
            save();
            if (!state.data.nombre && state.step !== 'nombre') return ask('nombre', intentReply);
            return ask('contacto', intentReply);
          }
          // Si además cuenta su caso en el mismo mensaje, respondemos a la intención y seguimos con el caso.
          if (words(text) > 12 && (step === 'inicio' || step === 'problema')) {
            await say(intentReply);
            return onProblem(text);
          }
          await say(intentReply);
          if (step === 'inicio' || step === 'problema') {
            state.step = 'problema';
            return say([isHow ? 'Cuando quieras, cuéntame tu caso: ¿qué es lo que más tiempo os consume ahora mismo?' : QUESTIONS.problema]);
          }
          return say([reask()]);
        }
      }
    }

    if (step === 'saludo') return onName(text);

    if (dataStep && /\?/.test(text) && !hasContact) {
      state.data.dudas = state.data.dudas ? state.data.dudas + ' / ' + text : text;
      save();
      await say(['Buena pregunta. Te la dejo apuntada para que el equipo te la responda con detalle.']);
      return say([reask()]);
    }

    // Se presenta con su nombre: lo guardamos y no se lo volvemos a preguntar.
    if (early && !state.data.nombre) {
      var intro = introduction(text);
      if (intro) {
        state.data.nombre = intro.name;
        save();
        var hello = 'Encantada, ' + trato() + '.';
        if ((step === 'inicio' || step === 'problema') && words(intro.rest) >= 4 && FITS.problema(intro.rest)) {
          await say([hello]);
          return onProblem(intro.rest);
        }
        if (step === 'inicio' || step === 'problema') {
          state.step = 'problema';
          return say([hello, QUESTIONS.problema]);
        }
        if (words(intro.rest) < 2) return say([hello, reask()]);
        text = intro.rest;
      }
    }

    // La respuesta no encaja con la pregunta: la primera vez lo aclara; la segunda sigue sin forzar.
    var fitStep = step === 'inicio' ? 'problema' : step;
    var loose = false;
    if (FITS[fitStep] && !/^(hola|buenas|buenos d[ií]as|buenas tardes|hey|qu[eé] tal)[\s.!¡?¿,]*$/i.test(text.trim()) && !(fitStep === 'problema' && words(text) < 4) && !FITS[fitStep](text)) {
      state.offtopic = state.offtopic || {};
      state.offtopic[fitStep] = (state.offtopic[fitStep] || 0) + 1;
      if (state.offtopic[fitStep] === 1) {
        state.step = fitStep;
        save();
        if (fitStep === 'tiempo' && /demasiad|much[ií]simo|un mont[oó]n|una barbaridad|un mundo|infinit|una locura|much[ií]simas/i.test(text)) {
          return say(['Uf, eso suena a mucho.', 'Para hacerme una idea: ¿son unas pocas horas a la semana, o más bien varias horas al día?']);
        }
        return say([CLARIFY[fitStep]]);
      }
      if (fitStep === 'problema' && !/^(no s[eé]|nada|prefiero no|no quiero|paso|ni idea)\b/i.test(text.trim())) {
        return onProblem(text);
      }
      if (fitStep === 'problema') {
        state.data.problema = 'Prefiere contarlo directamente al equipo';
        if (state.data.nombre || state.nameRefused) {
          state.step = 'contacto';
          save();
          return say(['No pasa nada, a veces cuesta ponerlo en palabras. Lo más fácil es que lo hables directamente con el equipo.', '¿Dónde prefieres que te contactemos' + (trato() ? ', ' + trato() : '') + '? Puedes dejarme un email o un teléfono.']);
        }
        return ask('nombre', ['No pasa nada, a veces cuesta ponerlo en palabras. Lo más fácil es que lo hables directamente con el equipo.']);
      }
      loose = true;
    }

    switch (step) {
      case 'inicio':
      case 'problema':
        if (/^(hola|buenas|buenos d[ií]as|buenas tardes|hey|qu[eé] tal)[\s.!¡?¿,]*$/i.test(text.trim())) {
          state.step = 'problema';
          return say(['Hola. ' + QUESTIONS.problema]);
        }
        if (words(text) < 4 && !state.asked.shortProblem) {
          state.step = 'problema';
          state.asked.shortProblem = true;
          state.data.problema = text;
          save();
          return say(['¿Me cuentas un poco más? Con un par de frases me basta para entenderlo bien.']);
        }
        if (state.asked.shortProblem && state.data.problema && state.data.problema !== text && !/ \/ /.test(state.data.problema)) {
          state.data.problema = '';
          text = (state.data.problemaCorto || '') + text;
        }
        return onProblem(text);

      case 'detalle':
        if (/^(no s[eé]|ni idea|no lo s[eé]|pues no s[eé]|no sabr[ií]a)\W*$/i.test(text.trim())) {
          state.asked.followUp = true;
          if (!state.data.detalle) state.data.detalle = 'No lo concreta';
          save();
          if (!state.asked.herramientas) return ask('herramientas', ['Sin problema, eso lo vemos con calma con el equipo.']);
          return ask('tiempo', ['Sin problema, eso lo vemos con calma con el equipo.']);
        }
        state.data.detalle = !state.data.detalle ? text : (state.data.detalle.split(' / ').indexOf(text) === -1 ? state.data.detalle + ' / ' + text : state.data.detalle);
        noteTools(text);
        var echo = channelEcho(text);
        var topicParts = (state.topic && TOPICS[state.topic].parts) || [];
        if (!loose && !state.asked.followUp) {
          var missing = topicParts.filter(function (p) { return !p.re.test(state.data.detalle + ' ' + (state.data.problema || '')); });
          if (missing.length && words(text) < 40) {
            state.asked.followUp = true;
            save();
            return say([echo || pick(ACKS), missing[0].follow]);
          }
        }
        var detAck = loose ? 'De acuerdo, sigamos.' : (echo || whoAck(text) || pick(ACKS));
        if (!state.asked.herramientas) {
          if (state.data.canales || state.data.herramientas) {
            state.step = 'herramientas';
            save();
            var known = (state.data.canales || []).concat((state.data.herramientas || '').split(/, | y /)).filter(Boolean)
              .map(function (n) { return n === 'correo' ? 'el correo' : n === 'teléfono' ? 'el teléfono' : n; })
              .filter(function (n, i, a) { return a.indexOf(n) === i && !/^(Idealista|Fotocasa|Habitaclia|Milanuncios|Wallapop|Booking|Airbnb|Amazon|Google|coches\.net)$/.test(n); });
            var besides = known.length ? 'Además de ' + listJoin(known).replace(/^Además de el /, 'Además del ') : 'Además de eso';
            besides = besides.replace(/^Además de el /, 'Además del ');
            return say([detAck, besides + ', ¿usáis alguna otra herramienta para gestionarlo? Por ejemplo, Excel, un CRM o algún programa de gestión.']);
          }
          return ask('herramientas', [detAck]);
        }
        return ask('tiempo', [detAck]);

      case 'herramientas':
        state.data.herramientas = toolNames(text) || text;
        state.asked.herramientas = true;
        var names = toolNames(text);
        var toolAck = names
          ? 'Perfecto. Con ' + names + ' se puede trabajar muy bien; muchas veces lo que falla no es la herramienta, sino cómo se conecta con lo demás.'
          : 'Perfecto, eso me ayuda a situarlo.';
        return ask('tiempo', [loose ? 'De acuerdo, sigamos.' : toolAck]);

      case 'tiempo':
        state.data.tiempo = text;
        if (state.data.empresa && /\d|sol[oa]\b/.test(state.data.empresa)) return ask('urgencia', [loose ? 'De acuerdo, sigamos.' : timeAck(text)]);
        var known = !state.data.empresa && sectorSaid();
        var sizeKnown = sizeSaid();
        if (known && sizeKnown) {
          state.data.empresa = known[0] + ', ' + sizeKnown;
          return ask('urgencia', [loose ? 'De acuerdo, sigamos.' : timeAck(text), sizeAckFor(sizeKnown)]);
        }
        if (known) {
          state.data.empresa = known[0];
          state.asked.empresaFollow = true;
          state.step = 'empresa';
          save();
          return say([loose ? 'De acuerdo, sigamos.' : timeAck(text), (state.data.sector ? 'Entiendo que sois ' : 'Me has comentado que sois ') + known[1] + '. ¿Cuántas personas sois, más o menos?']);
        }
        return ask('empresa', [loose ? 'De acuerdo, sigamos.' : timeAck(text)]);

      case 'empresa':
        var knownSec = sectorSaid();
        state.data.empresa = !state.data.empresa || (knownSec && sectorRe(knownSec[0]).test(text)) ? text : (state.data.empresa.split(' / ').indexOf(text) !== -1 ? state.data.empresa : state.data.empresa + ' / ' + text);
        var hasSize = /\d|solo yo|yo sol[oa]|sol[oa] yo|\bsol[oa]\b|aut[oó]nom|freelance|\b(uno|dos|tres|cuatro|cinco|seis|siete|ocho|nueve|diez|doce|quince|veinte|treinta|cien)\b|pocos|equipo peque/i.test(state.data.empresa);
        var sectorText = state.data.empresa.toLowerCase().replace(/somos|\d+|personas?|emplead[oa]s?|trabajador[ea]s?|m[aá]s o menos|aproximadamente|en total|unos|unas|\buno\b|\buna\b|\by\b|en la empresa|en el equipo|m[aá]s|menos|solo|[\s,.\/]+/gi, ' ').trim();
        var hasSector = sectorText.split(' ').some(function (w) { return w.length > 2 && !/^(yo|sol[oa]|pocos|equipo|peque[nñ]o)$/.test(w); });
        if (!loose && !state.asked.empresaFollow && (!hasSize || !hasSector)) {
          state.asked.empresaFollow = true;
          save();
          if (!hasSector) {
            var early = sizeAckFor(state.data.empresa);
            if (early) state.asked.sizeAckSaid = true;
            return say([early || 'Gracias.', '¿Y a qué os dedicáis?']);
          }
          return say(['Gracias.', '¿Y cuántas personas sois, más o menos?']);
        }
        var n = parseInt((state.data.empresa.match(/\d+/) || [])[0], 10);
        var sizeAck = !isNaN(n)
          ? (n <= 10 ? 'En equipos de ese tamaño, cada hora que se libera se nota muchísimo.' : 'Con un equipo así, los pequeños atascos se multiplican rápido, así que suele haber bastante margen.')
          : 'Gracias, me sirve para situarme.';
        // Si ya comentó el tamaño del equipo al repreguntar, no lo repite.
        if (state.asked.sizeAckSaid) sizeAck = 'Gracias, me hago una idea.';
        return ask('urgencia', [loose ? 'De acuerdo.' : sizeAck]);

      case 'urgencia':
        state.data.urgencia = text;
        var urgAck = /urge|ya|pronto|cuanto antes|r[aá]pido/i.test(text)
          ? 'Entendido, lo marcaré como prioritario.'
          : /explor|calma|mirando|informando|curiosidad/i.test(text)
            ? 'Me parece muy sensato: entenderlo bien antes de decidir es justo como nos gusta trabajar.'
            : 'Entendido.';
        if (state.nameRefused && !state.data.nombre) return ask('contacto', [urgAck, 'Me gustaría que alguien del equipo lo revise contigo personalmente.']);
        if (state.data.nombre) {
          state.step = 'contacto';
          save();
          return say([urgAck, 'Me gustaría que alguien del equipo lo revise contigo personalmente, ' + trato() + '. ¿Dónde prefieres que te contactemos? Puedes dejarme un email o un teléfono.']);
        }
        return ask('nombre', [urgAck]);

      case 'nombre':
        if (/prefiero no|no quiero|mejor no|no hace falta|an[oó]nim|\bpaso\b|da igual|no te lo (digo|doy)/i.test(text)) {
          state.data.nombre = '';
          return ask('contacto', ['Sin problema.']);
        }
        var byIntro = introduction(text);
        if (byIntro) { state.data.nombre = byIntro.name; return ask('contacto', ['Encantada, ' + trato() + '.']); }
        var name = extractName(text);
        if (!name) return say(['Perdona, no lo he entendido bien. ¿Cómo te llamas?']);
        state.data.nombre = name;
        return ask('contacto', ['Encantada, ' + trato() + '.']);

      case 'contacto':
        var email = (text.match(/[^\s@]+@[^\s@]+\.[^\s@]{2,}/) || [])[0];
        var phone = (text.match(/\+?\d[\d\s.-]{7,}\d/) || [])[0];
        if (!email && !phone) {
          // Pide una reunión, una videollamada o una llamada: se apunta como preferencia.
          var meeting = /presencial|en persona|reuni[oó]n|vernos|quedar|visita|pasarme|pasaros|vuestra oficina|cara a cara/i.test(text) ? 'Reunión presencial'
            : /videollamada|v[ií]deo|zoom|meet|teams/i.test(text) ? 'Videollamada'
            : /ll[aá]mame|que me llam|llamada|por tel[eé]fono/i.test(text) ? 'Llamada' : '';
          if (meeting) {
            state.data.preferencia = meeting;
            save();
            var why = meeting === 'Reunión presencial'
              ? 'Claro, una reunión en persona es perfecta: es como mejor se entiende cómo trabaja una empresa.'
              : meeting === 'Videollamada' ? 'Claro, una videollamada funciona muy bien.' : 'Claro, te llamamos sin problema.';
            return say([why, 'Para organizarla, el equipo necesita poder contactarte. ¿Me dejas un email o un teléfono?'.replace('organizarla', meeting === 'Llamada' ? 'llamarte' : 'organizarla')]);
          }
          if (/\?/.test(text) && !/no s[eé]|no quiero|prefiero no/i.test(text)) {
            return say(['Buena pregunta. Eso lo podrá resolver el equipo contigo directamente.', 'Para ello, ¿me dejas un email o un teléfono?']);
          }
          if (/no s[eé]|no quiero|prefiero no|ni idea|paso|no tengo|mejor no|no me apetece/i.test(text)) {
            state.contactRefused = (state.contactRefused || 0) + 1;
            save();
            if (state.contactRefused > 1) return say(['Entendido. Cuando quieras retomarlo, aquí estaré.']);
            return say(['Sin problema, no hace falta que lo dejes ahora.', 'Si en otro momento prefieres escribirnos tú, estamos en info@skurx.es. Y si cambias de idea, aquí estaré.']);
          }
          state.contactTries = (state.contactTries || 0) + 1;
          save();
          return say([state.contactTries === 1
            ? 'Creo que no lo he entendido bien. ¿Me lo escribes de nuevo? Puede ser un email o un teléfono.'
            : 'Solo necesito un email (algo como nombre@empresa.es) o un número de teléfono. Si prefieres no dejarlo, no pasa nada.']);
        }
        state.data.contacto = [email, phone && phone.replace(/[\s.-]/g, ' ').replace(/\s+/g, ' ').trim()].filter(Boolean).join(' · ');
        if (phone) return ask('horario', ['Apuntado.']);
        return summary(['Apuntado.']);

      case 'horario':
        state.data.horario = text;
        return summary(['Perfecto.']);

      case 'confirmar':
      case 'correccion':
        var newEmail = (text.match(/[^\s@]+@[^\s@]+\.[^\s@]{2,}/) || [])[0];
        var newPhone = (text.match(/\+?\d[\d\s.-]{7,}\d/) || [])[0];
        if (newEmail || newPhone) {
          state.data.contacto = [newEmail || (state.data.contacto || '').split(' · ').filter(function (c) { return /@/.test(c); })[0], newPhone ? newPhone.replace(/[\s.-]/g, ' ').replace(/\s+/g, ' ').trim() : (state.data.contacto || '').split(' · ').filter(function (c) { return !/@/.test(c); })[0]].filter(Boolean).join(' · ');
          return summary(['Corregido.']);
        }
        var newName = /me llamo|mi nombre es|no me llamo/i.test(text) && introduction(text.replace(/no me llamo \S+,?\s*/i, ''));
        if (newName) { state.data.nombre = newName.name; return summary(['Corregido.']); }
        if (state.step === 'correccion') {
          state.data.notas = (state.data.notas ? state.data.notas + ' / ' : '') + text;
          return summary(['Hecho.']);
        }
        if (/^(s[ií]|vale|ok|correcto|perfecto|env[ií]a|adelante|todo bien|est[aá] bien|yes)/i.test(text.trim())) return send();
        state.step = 'correccion';
        save();
        if (/corregir|cambiar|no\b|falta|a[nñ]adir/i.test(text) && words(text) <= 5) {
          return say(['Claro. Escríbeme lo que quieras añadir o corregir y lo incluyo.']);
        }
        state.data.notas = (state.data.notas ? state.data.notas + ' / ' : '') + text;
        return summary(['Lo añado.']);

      case 'fin':
        return say(['Ya tengo todo lo necesario. Si quieres añadir algo más, cuéntaselo al equipo cuando te contacten.']);
    }
  }

  // Por dónde le llegan las cosas, para repetírselo: «os llegan por correo, desde portales como Idealista».
  var CHANNELS = [[/correo|e-?mail|\bmail/i, 'correo'], [/whatsapp/i, 'WhatsApp'], [/tel[eé]fono|llamad/i, 'teléfono'], [/\bweb\b|formulario/i, 'la web'], [/instagram/i, 'Instagram'], [/facebook/i, 'Facebook'], [/linkedin/i, 'LinkedIn']];
  var PORTALS = [[/idealista/i, 'Idealista'], [/fotocasa/i, 'Fotocasa'], [/habitaclia/i, 'Habitaclia'], [/milanuncios/i, 'Milanuncios'], [/wallapop/i, 'Wallapop'], [/booking/i, 'Booking'], [/airbnb/i, 'Airbnb'], [/amazon/i, 'Amazon'], [/google/i, 'Google']];
  function namesIn(list, text) {
    return list.filter(function (c) { return c[0].test(text); }).map(function (c) { return c[1]; });
  }
  function channelEcho(text) {
    if (state.topic !== 'atencion' && state.topic !== 'agenda') return '';
    var ch = namesIn(CHANNELS, text);
    var po = namesIn(PORTALS, text);
    var anyPortal = po.length || /portal/i.test(text);
    var inPerson = /presencial|en persona|en la oficina|mostrador|en tienda|vienen a vernos|se acercan|p[uú]blico/i.test(text);
    if (!ch.length && !anyPortal && !inPerson) return '';
    state.data.canales = ch.concat(po);
    var parts = [];
    if (ch.length) parts.push('por ' + listJoin(ch));
    if (po.length) parts.push('desde ' + (po.length > 1 ? 'portales como ' : '') + listJoin(po));
    else if (anyPortal) parts.push('desde los portales');
    if (inPerson) parts.push('en persona');
    return 'Entiendo: os llegan ' + listJoin(parts) + '.';
  }

  // Reacción al tiempo que se pierde: «varias horas al día» es más de una jornada a la semana.
  function timeAck(text) {
    if (/no s[eé]|no lo s[eé]|no sabr|ni idea|depende/i.test(text) && !/\d/.test(text)) return 'Sin problema: eso es justo lo que medimos juntos en la auditoría.';
    var m = text.match(/\d+([.,]\d+)?/);
    var n = m ? parseFloat(m[0].replace(',', '.')) : NaN;
    var perDay = /al d[ií]a|diari|cada d[ií]a|todos los d[ií]as|por d[ií]a/i.test(text);
    var perMonth = /al mes|mensual|cada mes/i.test(text);
    if (!isNaN(n) && /minut/i.test(text) && !/hora/i.test(text)) n = n / 60;
    var weekly = !isNaN(n) ? (perDay ? n * 5 : perMonth ? n / 4 : n)
      : (/varias|muchas|bastantes/i.test(text) ? (perDay ? 15 : 8) : NaN);
    if (weekly >= 8) {
      return (perDay ? 'Eso es mucho tiempo: al cabo de la semana suma más de una jornada entera.' : 'Eso es más de una jornada de trabajo a la semana.') + ' Ahí suele haber bastante margen.';
    }
    if (weekly > 0 && weekly <= 3) return 'Aunque parezca poco, al cabo del año son muchas horas.';
    return 'Gracias. Aunque sea una estimación, ayuda mucho a ver dónde está el margen.';
  }

  // Sector que el usuario ya ha mencionado en la conversación, para no volver a preguntárselo.
  var SECTORS = [
    [/inmobiliari/i, 'Inmobiliaria', 'una inmobiliaria'], [/gestor[ií]a/i, 'Gestoría', 'una gestoría'], [/asesor[ií]a/i, 'Asesoría', 'una asesoría'],
    [/concesionari/i, 'Concesionario', 'un concesionario'], [/compraventa de (coches|veh[ií]culos)/i, 'Compraventa de vehículos', 'una compraventa de vehículos'],
    [/taller/i, 'Taller', 'un taller'], [/cl[ií]nica dental|dental/i, 'Clínica dental', 'una clínica dental'], [/cl[ií]nica/i, 'Clínica', 'una clínica'],
    [/restaurante/i, 'Restaurante', 'un restaurante'], [/hotel/i, 'Hotel', 'un hotel'], [/academia/i, 'Academia', 'una academia'],
    [/despacho de abogados|abogad/i, 'Despacho de abogados', 'un despacho de abogados'], [/reformas/i, 'Reformas', 'una empresa de reformas'],
    [/constructora/i, 'Constructora', 'una constructora'], [/gimnasio/i, 'Gimnasio', 'un gimnasio'], [/peluquer/i, 'Peluquería', 'una peluquería'],
    [/agencia de viajes/i, 'Agencia de viajes', 'una agencia de viajes'], [/e-?commerce|tienda online/i, 'Tienda online', 'una tienda online'],
    [/administrador[a]? de fincas|administraci[oó]n de fincas/i, 'Administración de fincas', 'una administración de fincas'], [/apartamentos tur[ií]sticos|alquiler vacacional|pisos tur[ií]sticos/i, 'Alquiler vacacional', 'una gestora de alquiler vacacional'],
    [/correduri|corredur[ií]a|seguros/i, 'Correduría de seguros', 'una correduría de seguros'], [/climatizaci|fontaner|electricist|instalador/i, 'Instalaciones', 'una empresa de instalaciones'],
    [/distribu(ci[oó]n|idora|idor)|mayorista/i, 'Distribución', 'una distribuidora'], [/panader[ií]a/i, 'Panadería', 'una panadería'], [/carpinter[ií]a/i, 'Carpintería', 'una carpintería']
  ];
  function sectorSaid() {
    if (state.data.sector) return state.data.sector;
    var said = state.history.filter(function (m) { return m.who === 'user'; }).map(function (m) { return m.text; }).join(' ');
    for (var i = 0; i < SECTORS.length; i++) {
      var m = said.match(SECTORS[i][0]);
      if (!m) continue;
      var before = said.slice(Math.max(0, m.index - 30), m.index);
      if (/(hace|hacen|lleva|llevan|gestiona|pasa|pasamos|mandamos|enviamos|con|a|nos lo hace)\s+(la|el|una|un|nuestra|nuestro)\s*$/i.test(before)) continue;
      return [SECTORS[i][1], SECTORS[i][2]];
    }
    return null;
  }

  function sectorRe(label) {
    for (var i = 0; i < SECTORS.length; i++) if (SECTORS[i][1] === label) return SECTORS[i][0];
    return /$^/;
  }
  function sizeSaid() {
    var said = state.history.filter(function (m) { return m.who === 'user'; }).map(function (m) { return m.text; }).join(' . ');
    var m = said.match(/(\d+)\s*(emplead[oa]s|trabajador[ea]s|personas|profesores|t[eé]cnicos)/i);
    return m ? m[0] : '';
  }

  function sizeAckFor(text) {
    var n = parseInt((text.match(/\d+/) || [])[0], 10);
    if (isNaN(n)) return '';
    return n <= 10 ? 'En equipos de ese tamaño, cada hora que se libera se nota muchísimo.' : 'Con un equipo así, los pequeños atascos se multiplican rápido, así que suele haber bastante margen.';
  }

  // Reacción a quién se encarga de responder.
  function whoAck(text) {
    if (state.topic !== 'atencion' && state.topic !== 'agenda') return '';
    if (/cuando (puedo|puede|podemos|pueden)|quien (puede|pilla|est[eé])|nadie|si hay tiempo/i.test(text)) {
      return /\byo\b|contesto|respondo|me ocupo|lo llevo/i.test(text)
        ? 'Entiendo: las atiendes tú cuando puedes, y eso hace que algunas se queden esperando más de la cuenta.'
        : 'Ahí suele estar el atasco: si no hay nadie claramente al cargo, las consultas se quedan esperando.';
    }
    if (/\byo\b|contesto|respondo|me ocupo|lo llevo/i.test(text)) return 'Entiendo, así que recae sobre ti, además de todo lo demás.';
    return '';
  }

  // Si ya ha nombrado sus herramientas (Excel, Gmail…), no se las volvemos a preguntar.
  // El correo o WhatsApp solos no cuentan: son canales, y conviene saber qué más usan.
  function noteTools(text) {
    TOOLS.lastIndex = 0;
    if (!state.asked.herramientas && TOOLS.test(text)) {
      var names = toolNames(text);
      var onlyChannels = names.split(/, | y /).every(function (n) { return /^(el correo|WhatsApp|Instagram|Idealista|Fotocasa|Habitaclia|Milanuncios|Wallapop|Booking|Airbnb|coches\.net)$/.test(n); });
      state.data.herramientas = names;
      if (!onlyChannels) state.asked.herramientas = true;
    }
  }

  // Nombres habituales, para no confundir una frase («agua fría») con un nombre.
  var COMMON_NAMES = 'alba alberto alejandra alejandro alex alfonso alfredo alicia alma alvaro amaia amparo ana andrea andres angel angela angeles anna antonia antonio ariadna arturo asuncion aurora beatriz belen benito bernardo blanca borja bruno camila carla carlos carles carmen carolina catalina cecilia celia cesar chema clara claudia concepcion concha consuelo cristian cristina daniel daniela david diana diego dolores eduardo elena eloy elisa elsa emilio emma encarna enrique eric ernesto esperanza esteban estefania ester esther eugenia eva fatima federico felipe felix fernando fini francisca francisco gabriel gema gemma gerard gloria gonzalo gregorio guillermo gustavo hector helena hugo ignacio ines inma inmaculada irene isaac isabel ismael ivan jaime javier jesus joan joaquin jordi jorge jose josefa josefina juan juana julia julian julio laia laura leire leo leonor lidia lola lorena lorenzo lourdes lucas lucia luis luisa lydia manolo manu manuel manuela marc marcos margarita maria mariano marina mario marisa marta martin martina mateo matias mercedes miguel mireia miriam monica montse montserrat nacho natalia nerea nicolas noelia nora nuria olga oliver oscar pablo paco paloma paola patricia pau paula pedro pepa pepe pilar pol quique rafael rafa ramon raquel raul rebeca ricardo roberto rocio rodrigo rosa rosario ruben salvador samuel sandra santi santiago sara sebastian sergio silvia sofia sonia susana teresa tomas toni ulises valentina valeria vanesa vanessa veronica vicente victor victoria virginia xavier yolanda'.split(' ');
  function isKnownName(word) {
    var w = word.toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g, '');
    return COMMON_NAMES.indexOf(w) !== -1;
  }

  // Primer paso: el nombre. Si en lugar del nombre cuenta su caso, lo atendemos y el nombre se pide al final.
  async function onName(text) {
    var afterName = async function (before) {
      state.step = 'problema';
      save();
      await say(before.concat(state.data.interes ? ['Para preparar la auditoría, empecemos por lo importante: ¿qué es lo que más tiempo os consume ahora mismo en el día a día?'] : INTRO));
      setQuick(['¿Cómo trabajáis?']);
    };
    var intro = introduction(text);
    if (intro) {
      state.data.nombre = intro.name;
      var company = intro.rest.match(/^(?:de|desde)\s+((?:una?|la|el|mi|nuestra)\s+[^,;.]{3,90}?)(?:,|\s+y)\s+(.+)$/i);
      if (company && words(company[2]) >= 4) {
        var comp = company[1].replace(/^(una?|la|el|mi|nuestra)\s+/i, '');
        state.data.empresa = comp.charAt(0).toUpperCase() + comp.slice(1);
        intro.rest = company[2];
      }
      if (words(intro.rest) >= 4 && FITS.problema(intro.rest)) {
        await say(['Encantada, ' + trato() + '.']);
        return onProblem(intro.rest);
      }
      return afterName(['Encantada, ' + trato() + '.']);
    }
    if (/prefiero no|no quiero|mejor no|no hace falta|an[oó]nim|paso\b|da igual/i.test(text)) {
      state.nameRefused = true;
      return afterName(['Sin problema.']);
    }
    if (/^(hola|buenas|buenos d[ií]as|buenas tardes|buenas noches|hey|qu[eé] tal)[\s.!¡?¿,]*$/i.test(text.trim())) {
      state.greeted = (state.greeted || 0) + 1;
      save();
      if (state.greeted > 1) return afterName(['Empezamos igualmente, y me lo dices cuando quieras.']);
      return say(['Hola. ¿Me dices tu nombre? Así sé cómo dirigirme a ti.']);
    }
    if (words(text) >= 4 && FITS.problema(text)) {
      state.step = 'problema';
      return onProblem(text);
    }
    var name = words(text) <= 3 ? extractName(text) : '';
    var parts = name.split(' ');
    var plausible = name && (isKnownName(parts[0]) || parts.length === 1);
    if (plausible && !NOT_A_NAME.test(parts[0]) && !WORK.test(text)) {
      state.data.nombre = name;
      return afterName(['Encantada, ' + trato() + '.']);
    }
    state.offtopic = state.offtopic || {};
    state.offtopic.saludo = (state.offtopic.saludo || 0) + 1;
    save();
    if (state.offtopic.saludo === 1) return say(['Perdona, no sé si lo he entendido bien. ¿Cuál es tu nombre?']);
    return afterName(['No te preocupes, lo dejamos para luego.']);
  }

  async function onProblem(text) {
    state.data.problema = state.data.problema && state.data.problema !== text ? state.data.problema + ' / ' + text : text;
    noteTools(text);
    var topic = topicOf(text);
    state.topic = topic;
    if (topic === 'informacion') state.asked.herramientas = true;
    state.step = 'detalle';
    save();
    // Si ya lo ha contado con detalle, no le hacemos repetirlo.
    if (words(text) >= 30) {
      state.asked.followUp = true;
      var longAck = [(topic ? TOPICS[topic].ack : 'Gracias por contármelo tan bien.'), 'Con lo que me cuentas ya me hago una buena idea.'];
      if (!state.asked.herramientas) return ask('herramientas', longAck);
      return ask('tiempo', longAck);
    }
    if (topic) {
      if (topic === 'informacion') state.step = 'herramientas';
      return say([TOPICS[topic].ack, TOPICS[topic].ask]);
    }
    return say(['Gracias por contármelo.', '¿Me das un poco más de detalle? Por ejemplo, cada cuánto ocurre o quién se encarga normalmente.']);
  }

  function summary(before) {
    state.step = 'confirmar';
    var d = state.data;
    var list = d.interes ? [['Solicita', d.interes], ['Situación', d.problema]] : [['Situación', d.problema]];
    if (d.detalle) list.push(['Detalle', d.detalle]);
    if (d.herramientas) list.push(['Herramientas', d.herramientas]);
    if (d.tiempo) list.push(['Tiempo dedicado', d.tiempo]);
    if (d.empresa) list.push(['Empresa', d.empresa]);
    if (d.urgencia) list.push(['Urgencia', d.urgencia]);
    list.push(['Nombre', d.nombre || 'Sin indicar']);
    list.push(['Contacto', d.contacto + (d.horario ? ' (' + d.horario.toLowerCase() + ')' : '')]);
    if (d.preferencia) list.push(['Prefiere', d.preferencia]);
    if (d.dudas) list.push(['Preguntas para el equipo', d.dudas]);
    if (d.notas) list.push(['Añadido', d.notas]);
    save();
    return say((before || []).concat([{ text: 'Te resumo lo que me has contado:', list: list }, '¿Está todo bien?'])).then(function () {
      setQuick(['Sí, enviar', 'Quiero corregir algo']);
    });
  }

  async function send() {
    busy = true;
    state.step = 'enviando';
    save();
    var d = state.data;
    var transcript = state.history.map(function (m) {
      return (m.who === 'fini' ? 'Fini: ' : 'Usuario: ') + m.text + (m.list ? '\n' + m.list.map(function (i) { return '  - ' + i[0] + ': ' + i[1]; }).join('\n') : '');
    }).join('\n');

    var ok = true;
    if (CONFIG.web3formsKey) {
      try {
        var res = await fetch('https://api.web3forms.com/submit', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json', Accept: 'application/json' },
          body: JSON.stringify({
            access_key: CONFIG.web3formsKey,
            subject: (d.interes ? 'Solicitud de auditoría: ' : 'Nueva conversación con Fini: ') + d.nombre,
            interes: d.interes || '',
            from_name: 'Fini · SKURX SYSTEMS',
            nombre: d.nombre,
            contacto: d.contacto,
            horario: d.horario || '',
            preferencia: d.preferencia || '',
            situacion: d.problema,
            detalle: d.detalle || '',
            herramientas: d.herramientas || '',
            tiempo: d.tiempo || '',
            empresa: d.empresa || '',
            urgencia: d.urgencia || '',
            notas: d.notas || '',
            dudas: d.dudas || '',
            conversacion: transcript,
            botcheck: ''
          })
        });
        ok = res.ok;
      } catch (e) {
        ok = false;
      }
    } else {
      console.info('[Fini] Modo prueba: no se envía nada.\n\n' + transcript);
    }

    busy = false;
    if (!ok) {
      state.step = 'confirmar';
      save();
      await say(['Vaya, no he podido enviarlo ahora mismo. Puedes intentarlo de nuevo en un momento o escribirnos directamente a info@skurx.es.']);
      return setQuick(['Sí, enviar']);
    }
    state.step = 'fin';
    save();
    await say([
      'Listo' + (trato() ? ', ' + trato() : '') + '. Se lo he pasado al equipo y se pondrán en contacto contigo personalmente en cuanto lo revisen.',
      'Gracias por tu tiempo. Ha sido un placer.'
    ].concat(CONFIG.web3formsKey ? [] : ['(Modo prueba: esta conversación no se ha enviado.)']));
    setQuick(['Empezar de nuevo']);
  }

  function extractName(text) {
    var t = text.trim().replace(/^(hola|buenas)[\s,.!]+/i, '').replace(/^(me llamo|soy|mi nombre es|ll[aá]mame)\s+/i, '').replace(/[.,!¡?¿].*$/, '').trim();
    var parts = t.split(/\s+/).filter(function (w) { return /^[a-záéíóúüñ'-]+$/i.test(w); }).slice(0, 3);
    if (!parts.length || parts[0].length < 2) return '';
    return parts.map(function (w) { return accent(capitalize(w)); }).join(' ');
  }

  var TOOL_STOP = /^(usamos|uso|utilizamos|utilizo|tenemos|trabajamos|trabajo|con|y|el|la|los|las|un|una|de|del|para|por|en|todo|nada|ninguna|ninguno|solo|sólo|pues|bueno|también|tambien|algún|alguna|programa|aplicación|aplicacion|herramienta|sistema|móvil|movil|ordenador|papel|libreta|agenda|mano|hoja|hojas|cálculo|calculo|gestión|gestion|facturación|facturacion|correo|mail|email|web|no|sí|si|lo|le|nos|me|mi|mis|su|sus|otro|otra|otros|además|ademas|más|mas|casi|vale|ok|madrid|barcelona|valencia|sevilla|alicante|m[aá]laga|murcia|bilbao|zaragoza|espa[nñ]a|elche|benidorm|hola|gracias|buenas|septiembre|enero|febrero|marzo|abril|mayo|junio|julio|agosto|octubre|noviembre|diciembre|lunes|viernes)$/i;
  function toolNames(text) {
    TOOLS.lastIndex = 0;
    var found = (text.match(TOOLS) || []).map(function (t) { return t.toLowerCase().replace(/\s+/g, ' '); });
    var names = found.filter(function (t, i) { return found.indexOf(t) === i; }).map(prettyTool);
    // Programas que no conocemos: palabras con mayúscula (Gesden) o una respuesta de una o dos palabras.
    var rest = text.replace(TOOLS, ' ');
    TOOLS.lastIndex = 0;
    var tokens = rest.split(/[\s,.;:()]+/).filter(Boolean);
    var unknown = tokens.filter(function (w, i) {
      return /^[A-ZÁÉÍÓÚÑ][A-Za-zÁÉÍÓÚÑáéíóúñ0-9]{2,}$/.test(w) && !TOOL_STOP.test(w) && !(i === 0 && !names.length && tokens.length > 2);
    });
    if (!names.length && !unknown.length && tokens.length && tokens.length <= 2 && tokens.every(function (w) { return !TOOL_STOP.test(w) && /^[a-záéíóúñ0-9]{3,}$/i.test(w); })) unknown = tokens;
    unknown.forEach(function (w) { var n = prettyTool(w.toLowerCase()); if (names.indexOf(n) === -1 && names.map(function (x) { return x.toLowerCase(); }).indexOf(w.toLowerCase()) === -1) names.push(n); });
    return listJoin(names);
  }

  function prettyTool(t) {
    var map = { correo: 'el correo', correos: 'el correo', excel: 'Excel', gmail: 'Gmail', outlook: 'Outlook', whatsapp: 'WhatsApp', holded: 'Holded', a3: 'A3', sage: 'Sage', factusol: 'FactuSOL', odoo: 'Odoo', hubspot: 'HubSpot', salesforce: 'Salesforce', notion: 'Notion', trello: 'Trello', asana: 'Asana', drive: 'Drive', dropbox: 'Dropbox', shopify: 'Shopify', woocommerce: 'WooCommerce', wordpress: 'WordPress', teams: 'Teams', slack: 'Slack', zoho: 'Zoho', quickbooks: 'QuickBooks', contasol: 'ContaSOL', 'google sheets': 'Google Sheets', crm: 'un CRM', erp: 'un ERP', exel: 'Excel', exell: 'Excel', word: 'Word', sap: 'SAP', 'whatsapp business': 'WhatsApp Business', 'google calendar': 'Google Calendar', 'clinic cloud': 'Clinic Cloud', clinicloud: 'Clinic Cloud', gesden: 'Gesden', gesfincas: 'Gesfincas', smoobu: 'Smoobu', inmovilla: 'Inmovilla', witei: 'Witei', trainingym: 'Trainingym', wodbuster: 'WodBuster', mindbody: 'Mindbody', pipedrive: 'Pipedrive', monday: 'Monday', clickup: 'ClickUp', prestashop: 'PrestaShop', magento: 'Magento', calendly: 'Calendly', contaplus: 'ContaPlus', instagram: 'Instagram', lodgify: 'Lodgify', avantio: 'Avantio', hostaway: 'Hostaway', 'coches.net': 'coches.net', wallapop: 'Wallapop', milanuncios: 'Milanuncios', idealista: 'Idealista', fotocasa: 'Fotocasa', habitaclia: 'Habitaclia', booking: 'Booking', airbnb: 'Airbnb', 'google analytics': 'Google Analytics', dms: 'un DMS' };
    if (/^programa de /.test(t)) return 'un ' + t;
    return map[t] || (t.length <= 4 ? t.toUpperCase() : t.charAt(0).toUpperCase() + t.slice(1));
  }
  function listJoin(items) {
    return items.length < 2 ? items.join('') : items.slice(0, -1).join(', ') + ' y ' + items[items.length - 1];
  }

  // Si el usuario escribe mientras Fini aún responde, sus mensajes se juntan y se atienden al terminar.
  var processing = false;
  var pending = [];

  async function submit(text) {
    text = (text || '').trim();
    if (!text) return;
    if (text === 'Empezar de nuevo') {
      if (processing) return;
      state = fresh();
      save();
      log.innerHTML = '';
      return start();
    }
    setQuick([]);
    push({ who: 'user', text: text });
    pending.push(text);
    if (processing) return;
    processing = true;
    while (pending.length) {
      var joined = pending.join('\n');
      pending = [];
      await wait(300);
      await handle(joined);
    }
    processing = false;
    input.focus({ preventScroll: true });
  }

  async function start(audit) {
    processing = true;
    state.step = 'saludo';
    if (audit) {
      state.data.interes = AUDIT;
      save();
    }
    var sec = state.data.sector;
    if (audit) await say(sec ? [GREETING_AUDIT[0], 'Veo que te interesa la Auditoría Operativa Inicial para ' + sec[2] + '. Te hago unas preguntas rápidas para que el equipo la prepare con tu caso.', GREETING_AUDIT[2]] : GREETING_AUDIT);
    else if (sec) await say([GREETING_AUDIT[0], 'Veo que vienes de la página de ' + sec[2] + '. Te hago unas preguntas rápidas para entender vuestro caso.', GREETING_AUDIT[2]]);
    else await say(GREETING);
    processing = false;
    if (pending.length) {
      var t = pending.join('\n');
      pending = [];
      processing = true;
      await handle(t);
      processing = false;
    }
  }

  // ---------- Formulario ----------
  function autosize() {
    input.style.height = 'auto';
    input.style.height = Math.min(input.scrollHeight, 140) + 'px';
  }
  input.addEventListener('input', autosize);
  input.addEventListener('keydown', function (e) {
    if (e.key === 'Enter' && !e.shiftKey && !e.isComposing) {
      e.preventDefault();
      form.requestSubmit();
    }
  });
  form.addEventListener('submit', function (e) {
    e.preventDefault();
    var text = input.value;
    input.value = '';
    autosize();
    submit(text);
  });

  // Al volver otro día, Fini saluda y retoma la conversación donde se quedó.
  async function welcomeBack() {
    var quickBefore = (state.quick || []).filter(function (q) { return q !== 'Empezar de nuevo'; });
    var name = trato() ? ', ' + trato() : '';
    processing = true;
    if (state.step === 'fin') {
      await say(['Hola de nuevo' + name + '. Ya tenemos tu caso y el equipo se pondrá en contacto contigo.', 'Si quieres contarme algo distinto, podemos empezar una conversación nueva.']);
      setQuick(['Empezar de nuevo']);
    } else if (state.step === 'inicio') {
      setQuick(quickBefore);
    } else {
      if (state.step === 'enviando') state.step = 'confirmar';
      await say(['Hola de nuevo' + name + '. Seguimos donde lo dejamos.'].concat(state.lastQ ? [state.lastQ] : []));
      setQuick(quickBefore.concat(['Empezar de nuevo']));
    }
    processing = false;
    if (pending.length) {
      var t = pending.join('\n');
      pending = [];
      processing = true;
      await handle(t);
      processing = false;
    }
  }

  // ---------- Apertura y cierre del panel ----------
  var trigger = null;
  var scrollY = 0;

  function open(event) {
    event.preventDefault();
    trigger = event.currentTarget;
    var audit = trigger && trigger.getAttribute('data-fini-intent') === 'auditoria';
    // Desde una página de sector: «Inmobiliaria|una inmobiliaria|inmobiliarias»
    var sectorAttr = (trigger && trigger.getAttribute('data-fini-sector')) || document.body.getAttribute('data-fini-sector');
    if (sectorAttr && !state.data.sector) {
      state.data.sector = sectorAttr.split('|');
      save();
    }
    if (audit && state.history.length && !state.data.interes) {
      state.data.interes = AUDIT;
      save();
    }
    scrollY = window.scrollY;
    document.documentElement.classList.add('panel-open');
    panel.showModal();
    if (!log.childElementCount) {
      if (state.history.length) {
        state.history.forEach(render);
        if (isReturnVisit()) welcomeBack();
        else setQuick(state.quick || []);
      } else {
        isReturnVisit();
        start(audit);
      }
    }
    setTimeout(function () { input.focus({ preventScroll: true }); scrollDown(); }, reduceMotion ? 0 : 300);
  }

  function close() {
    panel.classList.add('is-closing');
    var done = function () {
      panel.classList.remove('is-closing');
      panel.close();
    };
    if (reduceMotion) done();
    else setTimeout(done, 220);
  }

  panel.addEventListener('close', function () {
    document.documentElement.classList.remove('panel-open');
    window.scrollTo({ top: scrollY, behavior: 'instant' });
    if (trigger) trigger.focus({ preventScroll: true });
  });
  panel.addEventListener('cancel', function (event) {
    event.preventDefault();
    close();
  });
  panel.addEventListener('click', function (event) {
    if (event.target === panel) close();
  });

  document.querySelectorAll('[data-contact-open]').forEach(function (el) {
    el.addEventListener('click', open);
  });
  panel.querySelectorAll('[data-contact-close]').forEach(function (el) {
    el.addEventListener('click', close);
  });
})();
