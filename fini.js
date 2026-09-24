// Fini, la asistente virtual de SKURX: conversación guiada dentro del panel «Hablemos».
// Paso 1 (sin IA): guion propio que adapta las preguntas a lo que cuenta el usuario.
(function () {
  var CONFIG = {
    // El chat solo se activa cuando exista la Política de privacidad.
    // Mientras tanto se puede probar abriendo la web con ?fini=1
    enabled: false,
    // Clave gratuita de https://web3forms.com (asociada a info@skurx.es). Vacía = modo prueba, no se envía nada.
    web3formsKey: '',
    storageKey: 'skurx-fini-v1'
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
    try { sessionStorage.setItem(CONFIG.storageKey, JSON.stringify(state)); } catch (e) {}
  }
  function load() {
    try { return JSON.parse(sessionStorage.getItem(CONFIG.storageKey)); } catch (e) { return null; }
  }

  // ---------- Textos ----------
  var GREETING = [
    'Hola, soy Fini, la asistente virtual de SKURX SYSTEMS.',
    'Muchas empresas llegan hasta aquí porque sienten que el día a día se les come el tiempo: tareas que se repiten, información repartida en mil sitios, cosas que se quedan pendientes…',
    'Si algo de esto te suena, cuéntame un poco tu caso y vemos juntos cómo podemos ayudarte.'
  ];

  var HOW_WE_WORK = [
    'Trabajamos en cuatro pasos. Primero entendemos cómo funciona de verdad la empresa, hablando con quien hace el trabajo.',
    'Después analizamos dónde se está perdiendo tiempo o información, y solo entonces proponemos un cambio, si merece la pena. Si no lo merece, te lo decimos.',
    'Y por último lo ponemos en marcha y comprobamos que funciona en el día a día.'
  ];

  var TOPICS = {
    atencion: {
      re: /client|consulta|correo|e-?mail|mail|whatsapp|llamad|tel[eé]fono|lead|contact|reserva|cita|atenci[oó]n|respond|mensaje/i,
      ack: 'Es de lo más habitual: las consultas llegan por varios sitios y darles respuesta a tiempo se vuelve una tarea en sí misma.',
      ask: 'Cuando entra una consulta, ¿cómo os llega normalmente y quién se encarga de darle respuesta?'
    },
    administracion: {
      re: /factur|presupuest|albar[aá]n|pedido|document|contrat|n[oó]mina|contab|cobro|pago|papeleo|gestor/i,
      ack: 'Ese tipo de trabajo consume muchas horas sin que apenas se note, porque se hace un poco cada día.',
      ask: '¿Ese trabajo lo hacéis a mano cada vez, o hay alguna parte que ya esté automatizada?'
    },
    informacion: {
      re: /excel|hoja|dato|copi|informe|inventario|stock|base de datos|duplic|actualiz|programa|herramient|crm|erp/i,
      ack: 'Lo entiendo. Cuando el mismo dato vive en varios sitios, alguien acaba copiándolo a mano y es fácil que se desordene.',
      ask: '¿Con qué herramientas trabajáis ahora mismo? Aunque sea Excel y el correo, me sirve.'
    },
    seguimiento: {
      re: /seguimiento|olvid|pendient|se (nos )?pasa|se (nos )?pierde|recordar|aviso|plazo|retras|perdemos/i,
      ack: 'Eso pasa mucho: no es falta de ganas, es que hay demasiadas cosas que recordar a la vez.',
      ask: '¿Qué suele quedarse pendiente con más frecuencia, y qué consecuencias tiene cuando pasa?'
    }
  };

  var ACKS = ['Entiendo.', 'Tiene sentido.', 'Vale, me hago una idea.', 'Gracias, eso me ayuda mucho.'];
  var TOOLS = /excel|google sheets|hojas de c[aá]lculo|gmail|outlook|whatsapp|holded|a3|sage|factusol|odoo|hubspot|salesforce|notion|trello|asana|drive|dropbox|shopify|woocommerce|wordpress|teams|slack|zoho|quickbooks|contasol/gi;

  var QUESTIONS = {
    problema: 'Cuéntame, ¿qué es lo que más tiempo os quita ahora mismo?',
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
      push(msg);
      if (/\?$/.test(msg.text)) state.lastQ = msg.text;
      if (i < texts.length - 1) await wait(350);
    }
    busy = false;
  }

  // Retomar la última pregunta tras una duda del usuario: «Volviendo a tu caso, ¿…?»
  function reask() {
    var q = state.lastQ || QUESTIONS.problema;
    q = q.replace(/^.*?(¿)/, '$1').replace(/^¿Y /, '¿');
    return 'Volviendo a tu caso, ' + q.charAt(0) + q.charAt(1).toLowerCase() + q.slice(2);
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
    await say((before || []).concat([QUESTIONS[step]]));
    if (step === 'urgencia') setQuick(['Me urge', 'En los próximos meses', 'Solo estoy explorando']);
    if (step === 'horario') setQuick(['Por la mañana', 'Por la tarde', 'Me da igual']);
  }

  // ---------- Intenciones generales ----------
  var INTENTS = [
    {
      re: /\b(eres|sois|es esto) (un |una )?(bot|robot|m[aá]quina|ia|inteligencia|humana?|persona|real)|hablo con (un|una) (bot|m[aá]quina|persona)/i,
      reply: ['Soy una asistente virtual: respondo de forma automática. Todo lo que me cuentes lo revisa después una persona del equipo de SKURX.']
    },
    {
      re: /precio|tarifa|coste|cu[aá]nto (cuesta|cobr|vale|sale|costar)|es caro|barato/i,
      reply: ['Prefiero no darte una cifra sin conocer tu caso: cada empresa es distinta y no queremos proponerte nada que no tenga sentido.', 'Lo que sí puedo hacer es preparar tu caso para que el equipo lo valore contigo.']
    },
    {
      re: /hablar con (alguien|una persona|un humano|el equipo)|prefiero (llamar|hablar)|quiero (llamar|hablar con)/i,
      reply: ['Claro. Si prefieres hablar directamente con el equipo, tienes el email y el teléfono en la sección de contacto de la web.', 'Y si quieres, seguimos aquí un par de minutos y dejo tu caso preparado para que te llamen ya sabiendo de qué va.']
    },
    {
      re: /c[oó]mo trabaj|vuestro proceso|qu[eé] hac[eé]is|en qu[eé] consist/i,
      reply: HOW_WE_WORK
    }
  ];

  // ---------- Conversación ----------
  async function handle(text) {
    var step = state.step;
    var early = ['inicio', 'problema', 'detalle', 'herramientas', 'tiempo', 'empresa', 'urgencia'].indexOf(step) !== -1;

    if (early) {
      for (var i = 0; i < INTENTS.length; i++) {
        if (INTENTS[i].re.test(text)) {
          var isHow = INTENTS[i].reply === HOW_WE_WORK;
          // Si además cuenta su caso en el mismo mensaje, respondemos a la intención y seguimos con el caso.
          if (words(text) > 12 && (step === 'inicio' || step === 'problema')) {
            await say(INTENTS[i].reply);
            return onProblem(text);
          }
          await say(INTENTS[i].reply);
          if (step === 'inicio' || step === 'problema') {
            state.step = 'problema';
            return say([isHow ? 'Cuando quieras, cuéntame tu caso: ¿qué es lo que más tiempo os quita ahora mismo?' : QUESTIONS.problema]);
          }
          return say([reask()]);
        }
      }
    }

    switch (step) {
      case 'inicio':
      case 'problema':
        if (/^(hola|buenas|buenos d[ií]as|buenas tardes|hey|qu[eé] tal)[\s.!¡?¿,]*$/i.test(text.trim())) {
          state.step = 'problema';
          return say(['Hola. ' + QUESTIONS.problema]);
        }
        if (words(text) < 4) {
          state.step = 'problema';
          return say(['¿Me cuentas un poco más? Con un par de frases me basta para entenderlo bien.']);
        }
        return onProblem(text);

      case 'detalle':
        state.data.detalle = text;
        if (!state.asked.herramientas) return ask('herramientas', [pick(ACKS)]);
        return ask('tiempo', [pick(ACKS)]);

      case 'herramientas':
        state.data.herramientas = text;
        state.asked.herramientas = true;
        var found = (text.match(TOOLS) || []).map(function (t) { return t.toLowerCase(); });
        var uniq = found.filter(function (t, i) { return found.indexOf(t) === i; });
        var toolAck = uniq.length
          ? 'Perfecto. Con ' + listJoin(uniq.map(prettyTool)) + ' se puede trabajar muy bien; muchas veces lo que falla no es la herramienta, sino cómo se conecta con lo demás.'
          : 'Perfecto, eso me ayuda a situarlo.';
        return ask('tiempo', [toolAck]);

      case 'tiempo':
        state.data.tiempo = text;
        return ask('empresa', ['Gracias. Aunque sea una estimación, ayuda mucho a ver dónde está el margen.']);

      case 'empresa':
        state.data.empresa = text;
        var n = parseInt((text.match(/\d+/) || [])[0], 10);
        var sizeAck = !isNaN(n)
          ? (n <= 10 ? 'En equipos de ese tamaño, cada hora que se libera se nota muchísimo.' : 'Con un equipo así, los pequeños atascos se multiplican rápido, así que suele haber bastante margen.')
          : 'Gracias, me sirve para situarme.';
        return ask('urgencia', [sizeAck]);

      case 'urgencia':
        state.data.urgencia = text;
        var urgAck = /urge|ya|pronto|cuanto antes|r[aá]pido/i.test(text)
          ? 'Entendido, lo marcaré como prioritario.'
          : /explor|calma|mirando|informando|curiosidad/i.test(text)
            ? 'Me parece muy sensato: entenderlo bien antes de decidir es justo como nos gusta trabajar.'
            : 'Entendido.';
        return ask('nombre', [urgAck]);

      case 'nombre':
        var name = extractName(text);
        if (!name) return say(['Perdona, no lo he entendido bien. ¿Cómo te llamas?']);
        state.data.nombre = name;
        return ask('contacto', ['Encantada, ' + name + '.']);

      case 'contacto':
        var email = (text.match(/[^\s@]+@[^\s@]+\.[^\s@]{2,}/) || [])[0];
        var phone = (text.match(/\+?\d[\d\s.-]{7,}\d/) || [])[0];
        if (!email && !phone) {
          return say(['Creo que no lo he entendido bien. ¿Me lo escribes de nuevo? Puede ser un email o un teléfono.']);
        }
        state.data.contacto = [email, phone && phone.replace(/[\s.-]/g, ' ').replace(/\s+/g, ' ').trim()].filter(Boolean).join(' · ');
        if (phone) return ask('horario', ['Apuntado.']);
        return summary(['Apuntado.']);

      case 'horario':
        state.data.horario = text;
        return summary(['Perfecto.']);

      case 'confirmar':
        if (/^(s[ií]|vale|ok|correcto|perfecto|env[ií]a|adelante|todo bien|est[aá] bien)/i.test(text.trim())) return send();
        state.step = 'correccion';
        save();
        if (/corregir|cambiar|no\b|falta|a[nñ]adir/i.test(text) && words(text) <= 5) {
          return say(['Claro. Escríbeme lo que quieras añadir o corregir y lo incluyo.']);
        }
        state.data.notas = (state.data.notas ? state.data.notas + ' / ' : '') + text;
        return summary(['Lo añado.']);

      case 'correccion':
        state.data.notas = (state.data.notas ? state.data.notas + ' / ' : '') + text;
        return summary(['Hecho.']);

      case 'fin':
        return say(['Ya tengo todo lo necesario. Si quieres añadir algo más, cuéntaselo al equipo cuando te contacten.']);
    }
  }

  async function onProblem(text) {
    state.data.problema = state.data.problema ? state.data.problema + ' / ' + text : text;
    var topic = null;
    // Orden de prioridad: lo más concreto primero («las facturas llegan por correo» es administración).
    ['administracion', 'seguimiento', 'informacion', 'atencion'].some(function (k) {
      if (TOPICS[k].re.test(text)) { topic = k; return true; }
      return false;
    });
    state.topic = topic;
    if (topic === 'informacion') state.asked.herramientas = true;
    state.step = 'detalle';
    save();
    if (topic) {
      if (topic === 'informacion') state.step = 'herramientas';
      return say([TOPICS[topic].ack, TOPICS[topic].ask]);
    }
    return say(['Gracias por contármelo.', '¿Me das un poco más de detalle? Por ejemplo, cada cuánto ocurre o quién se encarga normalmente.']);
  }

  function summary(before) {
    state.step = 'confirmar';
    var d = state.data;
    var list = [['Situación', d.problema]];
    if (d.detalle) list.push(['Detalle', d.detalle]);
    if (d.herramientas) list.push(['Herramientas', d.herramientas]);
    if (d.tiempo) list.push(['Tiempo dedicado', d.tiempo]);
    if (d.empresa) list.push(['Empresa', d.empresa]);
    if (d.urgencia) list.push(['Urgencia', d.urgencia]);
    list.push(['Nombre', d.nombre]);
    list.push(['Contacto', d.contacto + (d.horario ? ' (' + d.horario.toLowerCase() + ')' : '')]);
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
            subject: 'Nueva conversación con Fini: ' + d.nombre,
            from_name: 'Fini · SKURX SYSTEMS',
            nombre: d.nombre,
            contacto: d.contacto,
            horario: d.horario || '',
            situacion: d.problema,
            detalle: d.detalle || '',
            herramientas: d.herramientas || '',
            tiempo: d.tiempo || '',
            empresa: d.empresa || '',
            urgencia: d.urgencia || '',
            notas: d.notas || '',
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
      'Listo, ' + d.nombre + '. Se lo he pasado al equipo y se pondrán en contacto contigo personalmente en cuanto lo revisen.',
      'Gracias por tu tiempo. Ha sido un placer.'
    ].concat(CONFIG.web3formsKey ? [] : ['(Modo prueba: esta conversación no se ha enviado.)']));
    setQuick(['Empezar de nuevo']);
  }

  function extractName(text) {
    var t = text.trim().replace(/^(me llamo|soy|mi nombre es|ll[aá]mame|hola,? soy)\s+/i, '').replace(/[.,!¡?¿].*$/, '').trim();
    var parts = t.split(/\s+/).filter(function (w) { return /^[a-záéíóúüñ'-]+$/i.test(w); }).slice(0, 3);
    if (!parts.length || parts[0].length < 2) return '';
    return parts.map(capitalize).join(' ');
  }

  function prettyTool(t) {
    var map = { excel: 'Excel', gmail: 'Gmail', outlook: 'Outlook', whatsapp: 'WhatsApp', holded: 'Holded', a3: 'A3', sage: 'Sage', factusol: 'FactuSOL', odoo: 'Odoo', hubspot: 'HubSpot', salesforce: 'Salesforce', notion: 'Notion', trello: 'Trello', asana: 'Asana', drive: 'Drive', dropbox: 'Dropbox', shopify: 'Shopify', woocommerce: 'WooCommerce', wordpress: 'WordPress', teams: 'Teams', slack: 'Slack', zoho: 'Zoho', quickbooks: 'QuickBooks', contasol: 'ContaSOL', 'google sheets': 'Google Sheets' };
    return map[t] || t;
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

  async function start() {
    processing = true;
    state.step = 'inicio';
    await say(GREETING);
    setQuick(['¿Cómo trabajáis?']);
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

  // ---------- Apertura y cierre del panel ----------
  var trigger = null;
  var scrollY = 0;

  function open(event) {
    event.preventDefault();
    trigger = event.currentTarget;
    scrollY = window.scrollY;
    document.documentElement.classList.add('panel-open');
    panel.showModal();
    if (!log.childElementCount) {
      if (state.history.length) {
        state.history.forEach(render);
        setQuick(state.quick || []);
      } else {
        start();
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
