// Fini en otros idiomas (EN, CA, FR, DE, NL): conversación guiada con las mismas preguntas que la Fini
// en español, pero sin interpretar el texto libre con reglas propias de cada idioma.
// El idioma sale de <html lang>. El correo que llega a info@skurx.es va en español, con el idioma indicado.
(function () {
  var CONFIG = {
    enabled: true,
    // Misma clave gratuita de Web3Forms que la Fini en español (asociada a info@skurx.es).
    web3formsKey: '413a9355-a4b8-472a-a87e-9cbd9b932651',
    keepDays: 30
  };

  var LANG = (document.documentElement.getAttribute('lang') || 'en').slice(0, 2).toLowerCase();

  var T = {
    en: {
      greeting: ['Hi, I’m Fini, the virtual assistant of SKURX SYSTEMS. Nice to meet you.', 'What’s your name? That way I know how to address you.'],
      greetingAudit: ['Hi, I’m Fini, the virtual assistant of SKURX SYSTEMS.', 'I see you’re interested in the Initial Operational Audit: in one week we analyse how your company works and give you a clear map of where capacity is being lost. I’ll ask you a few quick questions so the team can prepare it with your case.', 'First of all, what’s your name?'],
      audit: 'Initial Operational Audit',
      review: 'Free express review',
      reviewLine: 'I see you’re interested in the free express review: 20 minutes in which the team goes over how you work and points out where you’re losing time. I’ll ask you a few quick questions to prepare it.',
      nice: function (n) { return 'Nice to meet you' + (n ? ', ' + n : '') + '.'; },
      q: {
        problema: 'Tell me, what takes up most of your time right now?',
        herramientas: 'And which tools do you work with day to day? Even if it’s just Excel and email, that helps.',
        tiempo: 'Roughly how much time would you say goes into this each week?',
        empresa: 'To get a better picture: what does your company do, and how many people are you, roughly?',
        urgencia: 'Is this already a concern, or are you exploring calmly?',
        contacto: 'Where would you like us to contact you? You can leave an email or a phone number.',
        horario: 'Is there a time of day that suits you best for us to get in touch?'
      },
      quick: {
        tiempo: ['A few hours a week', 'Several hours a day', 'Not sure'],
        urgencia: ['It’s urgent', 'In the coming months', 'Just exploring'],
        horario: ['Morning', 'Afternoon', 'Any time']
      },
      acks: ['I see.', 'That makes sense.', 'Okay, I’m getting the picture.', 'Thanks, that really helps.'],
      badContact: 'I don’t think that’s an email or a phone number. Could you write it again? For example name@company.com or +44 20 1234 5678.',
      summaryIntro: 'Here’s a summary of what you’ve told me:',
      summaryOk: 'Is everything correct?',
      confirm: ['Yes, send', 'I want to add something'],
      addWhat: 'Of course. What would you like to add or correct?',
      labels: { interes: 'Request', problema: 'Situation', herramientas: 'Tools', tiempo: 'Time spent', empresa: 'Company', urgencia: 'Urgency', nombre: 'Name', contacto: 'Contact', notas: 'Added' },
      none: 'Not given',
      sendFail: 'I couldn’t send it just now. You can try again in a moment or write to us directly at info@skurx.es.',
      done: function (n) { return ['Done' + (n ? ', ' + n : '') + '. I’ve passed it on to the team and they’ll contact you personally as soon as they’ve reviewed it.', 'Thank you for your time. It’s been a pleasure.']; },
      restart: 'Start again',
      back: function (n) { return 'Welcome back' + (n ? ', ' + n : '') + '. Let’s pick up where we left off.'; },
      backDone: function (n) { return ['Welcome back' + (n ? ', ' + n : '') + '. We already have your case and the team will be in touch.', 'If you’d like to tell me about something else, we can start a new conversation.']; },
      price: ['I’d rather not give you a figure without knowing your case: every company is different.', 'What I can do is prepare your case so the team can tell you exactly what they would do and what it would cost.'],
      privacy: ['What you tell me here is only used by the SKURX SYSTEMS team to handle your enquiry, and it is not shared with anyone. You’ll find the details in the privacy policy linked just below.'],
      backTo: 'Back to your case: ',
      typing: 'Fini is typing',
      priceRe: /\b(price|prices|cost|costs|how much|fee|fees|quote|budget)\b/i,
      privacyRe: /\b(privacy|personal data|gdpr|data protection|confidential)\b/i,
      nameStrip: /^(hi|hello|hey|good (morning|afternoon|evening))[\s,.!]+|^(my name is|i am|i'm|it's|this is|call me)\s+/gi
    },
    ca: {
      greeting: ['Hola, soc la Fini, l’assistent virtual de SKURX SYSTEMS. És un plaer saludar-te.', 'Com et dius? Així sé com adreçar-me a tu.'],
      greetingAudit: ['Hola, soc la Fini, l’assistent virtual de SKURX SYSTEMS.', 'Veig que t’interessa l’Auditoria Operativa Inicial: en una setmana analitzem com treballa la teva empresa i et lliurem un mapa clar d’on es perd capacitat. Et faig unes preguntes ràpides perquè l’equip la prepari amb el teu cas.', 'Per començar, com et dius?'],
      audit: 'Auditoria Operativa Inicial',
      review: 'Revisió exprés gratuïta',
      reviewLine: 'Veig que t’interessa la revisió exprés gratuïta: 20 minuts en què l’equip revisa amb tu com treballeu i t’assenyala on se us escapa el temps. Et faig unes preguntes ràpides per preparar-la.',
      nice: function (n) { return 'Encantada' + (n ? ', ' + n : '') + '.'; },
      q: {
        problema: 'Explica’m, què és el que més temps us consumeix ara mateix?',
        herramientas: 'I amb quines eines treballeu cada dia? Encara que sigui Excel i el correu, em serveix.',
        tiempo: 'Quant temps diríeu que us hi va a la setmana, més o menys?',
        empresa: 'Per situar-me millor: a què es dedica la teva empresa i quantes persones sou, més o menys?',
        urgencia: 'És una cosa que ja us preocupa o ho esteu explorant amb calma?',
        contacto: 'On prefereixes que et contactem? Pots deixar-me un correu o un telèfon.',
        horario: 'Hi ha algun moment del dia en què et vagi millor que et contactem?'
      },
      quick: {
        tiempo: ['Unes hores a la setmana', 'Diverses hores al dia', 'No ho sé'],
        urgencia: ['Em corre pressa', 'En els propers mesos', 'Només estic explorant'],
        horario: ['Al matí', 'A la tarda', 'M’és igual']
      },
      acks: ['Entenc.', 'Té sentit.', 'D’acord, me’n faig una idea.', 'Gràcies, això m’ajuda molt.'],
      badContact: 'Em sembla que no és un correu ni un telèfon. Me’l pots tornar a escriure? Per exemple nom@empresa.com o 612 345 678.',
      summaryIntro: 'Et resumeixo el que m’has explicat:',
      summaryOk: 'Està tot bé?',
      confirm: ['Sí, envia-ho', 'Vull afegir alguna cosa'],
      addWhat: 'És clar. Què vols afegir o corregir?',
      labels: { interes: 'Sol·licita', problema: 'Situació', herramientas: 'Eines', tiempo: 'Temps dedicat', empresa: 'Empresa', urgencia: 'Urgència', nombre: 'Nom', contacto: 'Contacte', notas: 'Afegit' },
      none: 'Sense indicar',
      sendFail: 'No ho he pogut enviar ara mateix. Pots tornar-ho a provar d’aquí a un moment o escriure’ns directament a info@skurx.es.',
      done: function (n) { return ['Fet' + (n ? ', ' + n : '') + '. Ho he passat a l’equip i es posaran en contacte amb tu personalment tan bon punt ho revisin.', 'Gràcies pel teu temps. Ha estat un plaer.']; },
      restart: 'Començar de nou',
      back: function (n) { return 'Hola de nou' + (n ? ', ' + n : '') + '. Continuem on ho vam deixar.'; },
      backDone: function (n) { return ['Hola de nou' + (n ? ', ' + n : '') + '. Ja tenim el teu cas i l’equip es posarà en contacte amb tu.', 'Si vols explicar-me una altra cosa, podem començar una conversa nova.']; },
      price: ['Prefereixo no donar-te una xifra sense conèixer el teu cas: cada empresa és diferent.', 'El que sí que puc fer és preparar el teu cas perquè l’equip et digui exactament què faria i quant costaria.'],
      privacy: ['El que m’expliquis aquí només ho fa servir l’equip de SKURX SYSTEMS per atendre la teva consulta, i no se cedeix a ningú. Tens els detalls a la política de privacitat, enllaçada aquí sota.'],
      backTo: 'Tornant al teu cas: ',
      typing: 'La Fini està escrivint',
      priceRe: /\b(preu|preus|cost|costa|quant val|quant costa|pressupost|tarifa)\b/i,
      privacyRe: /\b(privacitat|dades personals|rgpd|protecci[oó] de dades|confidencial)\b/i,
      nameStrip: /^(hola|bon dia|bona tarda)[\s,.!]+|^(em dic|soc|el meu nom [eé]s|di[ueé]s-me)\s+/gi
    },
    fr: {
      greeting: ['Bonjour, je suis Fini, l’assistante virtuelle de SKURX SYSTEMS. Ravie de vous saluer.', 'Comment vous appelez-vous ? Ainsi, je saurai comment m’adresser à vous.'],
      greetingAudit: ['Bonjour, je suis Fini, l’assistante virtuelle de SKURX SYSTEMS.', 'Je vois que l’Audit Opérationnel Initial vous intéresse : en une semaine, nous analysons le fonctionnement de votre entreprise et vous remettons une carte claire des endroits où se perd de la capacité. Je vous pose quelques questions rapides pour que l’équipe le prépare avec votre cas.', 'Pour commencer, comment vous appelez-vous ?'],
      audit: 'Audit Opérationnel Initial',
      review: 'Bilan express gratuit',
      reviewLine: 'Je vois que le bilan express gratuit vous intéresse : 20 minutes pendant lesquelles l’équipe passe en revue avec vous votre façon de travailler et vous indique où vous perdez du temps. Je vous pose quelques questions rapides pour le préparer.',
      nice: function (n) { return 'Enchantée' + (n ? ', ' + n : '') + '.'; },
      q: {
        problema: 'Dites-moi, qu’est-ce qui vous prend le plus de temps en ce moment ?',
        herramientas: 'Et avec quels outils travaillez-vous au quotidien ? Même si ce n’est qu’Excel et la messagerie, cela m’aide.',
        tiempo: 'Combien de temps diriez-vous y consacrer par semaine, à peu près ?',
        empresa: 'Pour mieux me situer : quelle est l’activité de votre entreprise et combien êtes-vous, à peu près ?',
        urgencia: 'Est-ce déjà une préoccupation, ou explorez-vous le sujet tranquillement ?',
        contacto: 'Où préférez-vous que nous vous contactions ? Vous pouvez me laisser un e-mail ou un numéro de téléphone.',
        horario: 'Y a-t-il un moment de la journée où il vous convient mieux d’être contacté ?'
      },
      quick: {
        tiempo: ['Quelques heures par semaine', 'Plusieurs heures par jour', 'Je ne sais pas'],
        urgencia: ['C’est urgent', 'Dans les prochains mois', 'J’explore simplement'],
        horario: ['Le matin', 'L’après-midi', 'Peu importe']
      },
      acks: ['Je comprends.', 'C’est logique.', 'D’accord, je m’en fais une idée.', 'Merci, cela m’aide beaucoup.'],
      badContact: 'Je crois que ce n’est ni un e-mail ni un numéro de téléphone. Pouvez-vous le réécrire ? Par exemple nom@entreprise.fr ou +33 6 12 34 56 78.',
      summaryIntro: 'Voici un résumé de ce que vous m’avez dit :',
      summaryOk: 'Tout est correct ?',
      confirm: ['Oui, envoyer', 'Je veux ajouter quelque chose'],
      addWhat: 'Bien sûr. Que souhaitez-vous ajouter ou corriger ?',
      labels: { interes: 'Demande', problema: 'Situation', herramientas: 'Outils', tiempo: 'Temps consacré', empresa: 'Entreprise', urgencia: 'Urgence', nombre: 'Nom', contacto: 'Contact', notas: 'Ajouté' },
      none: 'Non indiqué',
      sendFail: 'Je n’ai pas pu l’envoyer pour le moment. Vous pouvez réessayer dans un instant ou nous écrire directement à info@skurx.es.',
      done: function (n) { return ['C’est fait' + (n ? ', ' + n : '') + '. Je l’ai transmis à l’équipe, qui vous contactera personnellement dès qu’elle l’aura examiné.', 'Merci pour votre temps. Ce fut un plaisir.']; },
      restart: 'Recommencer',
      back: function (n) { return 'Bon retour' + (n ? ', ' + n : '') + '. Reprenons là où nous nous étions arrêtés.'; },
      backDone: function (n) { return ['Bon retour' + (n ? ', ' + n : '') + '. Nous avons déjà votre dossier et l’équipe vous contactera.', 'Si vous souhaitez me parler d’autre chose, nous pouvons commencer une nouvelle conversation.']; },
      price: ['Je préfère ne pas vous donner de chiffre sans connaître votre cas : chaque entreprise est différente.', 'En revanche, je peux préparer votre cas pour que l’équipe vous dise exactement ce qu’elle ferait et combien cela coûterait.'],
      privacy: ['Ce que vous me dites ici est utilisé uniquement par l’équipe de SKURX SYSTEMS pour traiter votre demande, et n’est cédé à personne. Vous trouverez les détails dans la politique de confidentialité, en lien juste en dessous.'],
      backTo: 'Pour revenir à votre cas : ',
      typing: 'Fini est en train d’écrire',
      priceRe: /\b(prix|tarif|tarifs|co[uû]t|combien|devis|budget)\b/i,
      privacyRe: /\b(confidentialit[eé]|donn[eé]es personnelles|rgpd|protection des donn[eé]es|confidentiel)\b/i,
      nameStrip: /^(bonjour|bonsoir|salut)[\s,.!]+|^(je m'appelle|je m’appelle|je suis|moi c'est|mon nom est)\s+/gi
    },
    de: {
      greeting: ['Hallo, ich bin Fini, die virtuelle Assistentin von SKURX SYSTEMS. Schön, Sie zu begrüßen.', 'Wie heißen Sie? Dann weiß ich, wie ich Sie ansprechen kann.'],
      greetingAudit: ['Hallo, ich bin Fini, die virtuelle Assistentin von SKURX SYSTEMS.', 'Wie ich sehe, interessieren Sie sich für die Operative Erstanalyse: In einer Woche analysieren wir, wie Ihr Unternehmen arbeitet, und übergeben Ihnen eine klare Übersicht, wo Kapazität verloren geht. Ich stelle Ihnen ein paar kurze Fragen, damit das Team sie mit Ihrem Fall vorbereiten kann.', 'Zunächst: Wie heißen Sie?'],
      audit: 'Operative Erstanalyse',
      review: 'Kostenloser Express-Check',
      reviewLine: 'Wie ich sehe, interessieren Sie sich für den kostenlosen Express-Check: 20 Minuten, in denen das Team mit Ihnen durchgeht, wie Sie arbeiten, und Ihnen zeigt, wo Ihnen Zeit verloren geht. Ich stelle Ihnen ein paar kurze Fragen, um ihn vorzubereiten.',
      nice: function (n) { return 'Freut mich' + (n ? ', ' + n : '') + '.'; },
      q: {
        problema: 'Erzählen Sie: Was kostet Sie im Moment die meiste Zeit?',
        herramientas: 'Und mit welchen Werkzeugen arbeiten Sie im Alltag? Auch wenn es nur Excel und E-Mail sind, hilft mir das.',
        tiempo: 'Wie viel Zeit geht dafür pro Woche ungefähr drauf?',
        empresa: 'Damit ich es besser einordnen kann: Was macht Ihr Unternehmen, und wie viele Personen sind Sie ungefähr?',
        urgencia: 'Beschäftigt Sie das schon akut, oder schauen Sie sich erst in Ruhe um?',
        contacto: 'Wo sollen wir Sie am liebsten kontaktieren? Sie können mir eine E-Mail-Adresse oder eine Telefonnummer hinterlassen.',
        horario: 'Gibt es eine Tageszeit, zu der wir Sie am besten erreichen?'
      },
      quick: {
        tiempo: ['Ein paar Stunden pro Woche', 'Mehrere Stunden am Tag', 'Weiß ich nicht'],
        urgencia: ['Es ist dringend', 'In den nächsten Monaten', 'Ich schaue mich nur um'],
        horario: ['Vormittags', 'Nachmittags', 'Egal']
      },
      acks: ['Verstehe.', 'Das ergibt Sinn.', 'Gut, ich bekomme ein Bild davon.', 'Danke, das hilft mir sehr.'],
      badContact: 'Das scheint weder eine E-Mail-Adresse noch eine Telefonnummer zu sein. Könnten Sie sie noch einmal schreiben? Zum Beispiel name@firma.de oder +49 30 1234567.',
      summaryIntro: 'Hier eine Zusammenfassung dessen, was Sie mir erzählt haben:',
      summaryOk: 'Stimmt alles?',
      confirm: ['Ja, senden', 'Ich möchte etwas ergänzen'],
      addWhat: 'Natürlich. Was möchten Sie ergänzen oder korrigieren?',
      labels: { interes: 'Anfrage', problema: 'Situation', herramientas: 'Werkzeuge', tiempo: 'Zeitaufwand', empresa: 'Unternehmen', urgencia: 'Dringlichkeit', nombre: 'Name', contacto: 'Kontakt', notas: 'Ergänzt' },
      none: 'Nicht angegeben',
      sendFail: 'Ich konnte es gerade nicht senden. Versuchen Sie es gleich noch einmal oder schreiben Sie uns direkt an info@skurx.es.',
      done: function (n) { return ['Erledigt' + (n ? ', ' + n : '') + '. Ich habe es an das Team weitergegeben, das sich persönlich bei Ihnen meldet, sobald es alles geprüft hat.', 'Vielen Dank für Ihre Zeit. Es war mir eine Freude.']; },
      restart: 'Neu beginnen',
      back: function (n) { return 'Willkommen zurück' + (n ? ', ' + n : '') + '. Machen wir dort weiter, wo wir aufgehört haben.'; },
      backDone: function (n) { return ['Willkommen zurück' + (n ? ', ' + n : '') + '. Wir haben Ihren Fall bereits, und das Team meldet sich bei Ihnen.', 'Wenn Sie mir etwas anderes erzählen möchten, können wir ein neues Gespräch beginnen.']; },
      price: ['Ich möchte Ihnen ungern eine Zahl nennen, ohne Ihren Fall zu kennen: Jedes Unternehmen ist anders.', 'Was ich tun kann: Ihren Fall so vorbereiten, dass das Team Ihnen genau sagen kann, was es tun würde und was es kostet.'],
      privacy: ['Was Sie mir hier erzählen, nutzt ausschließlich das Team von SKURX SYSTEMS, um Ihre Anfrage zu bearbeiten, und es wird an niemanden weitergegeben. Die Details finden Sie in der Datenschutzerklärung, direkt unten verlinkt.'],
      backTo: 'Zurück zu Ihrem Fall: ',
      typing: 'Fini schreibt',
      priceRe: /\b(preis|preise|kosten|kostet|wie viel|angebot|budget|tarif)\b/i,
      privacyRe: /\b(datenschutz|pers[oö]nliche daten|dsgvo|vertraulich)\b/i,
      nameStrip: /^(hallo|guten (morgen|tag|abend)|hi)[\s,.!]+|^(ich hei[sß]e|ich bin|mein name ist|hier ist)\s+/gi
    },
    nl: {
      greeting: ['Hallo, ik ben Fini, de virtuele assistent van SKURX SYSTEMS. Leuk je te begroeten.', 'Hoe heet je? Dan weet ik hoe ik je kan aanspreken.'],
      greetingAudit: ['Hallo, ik ben Fini, de virtuele assistent van SKURX SYSTEMS.', 'Ik zie dat je interesse hebt in de Operationele Startaudit: in één week analyseren we hoe je bedrijf werkt en krijg je een duidelijk overzicht van waar capaciteit verloren gaat. Ik stel je een paar korte vragen zodat het team hem met jouw situatie kan voorbereiden.', 'Om te beginnen: hoe heet je?'],
      audit: 'Operationele Startaudit',
      review: 'Gratis quickscan',
      reviewLine: 'Ik zie dat je interesse hebt in de gratis quickscan: 20 minuten waarin het team met je bekijkt hoe jullie werken en je laat zien waar tijd weglekt. Ik stel je een paar korte vragen om hem voor te bereiden.',
      nice: function (n) { return 'Aangenaam' + (n ? ', ' + n : '') + '.'; },
      q: {
        problema: 'Vertel eens, wat kost jullie op dit moment de meeste tijd?',
        herramientas: 'En met welke tools werken jullie dagelijks? Ook als het alleen Excel en e-mail is, helpt me dat.',
        tiempo: 'Hoeveel tijd gaat daar ongeveer per week in zitten?',
        empresa: 'Om het beter te plaatsen: wat doet je bedrijf, en met hoeveel mensen zijn jullie ongeveer?',
        urgencia: 'Is het al een zorg, of verkennen jullie het rustig?',
        contacto: 'Waar kunnen we je het beste bereiken? Je kunt een e-mailadres of telefoonnummer achterlaten.',
        horario: 'Is er een moment van de dag waarop we je het beste kunnen bereiken?'
      },
      quick: {
        tiempo: ['Een paar uur per week', 'Meerdere uren per dag', 'Weet ik niet'],
        urgencia: ['Het is dringend', 'In de komende maanden', 'Ik verken alleen'],
        horario: ['’s Ochtends', '’s Middags', 'Maakt niet uit']
      },
      acks: ['Ik begrijp het.', 'Dat is logisch.', 'Oké, ik krijg een beeld.', 'Bedankt, dat helpt me veel.'],
      badContact: 'Dat lijkt geen e-mailadres of telefoonnummer. Kun je het nog eens schrijven? Bijvoorbeeld naam@bedrijf.nl of +31 6 12345678.',
      summaryIntro: 'Hier een samenvatting van wat je me hebt verteld:',
      summaryOk: 'Klopt alles?',
      confirm: ['Ja, versturen', 'Ik wil iets toevoegen'],
      addWhat: 'Natuurlijk. Wat wil je toevoegen of corrigeren?',
      labels: { interes: 'Aanvraag', problema: 'Situatie', herramientas: 'Tools', tiempo: 'Bestede tijd', empresa: 'Bedrijf', urgencia: 'Urgentie', nombre: 'Naam', contacto: 'Contact', notas: 'Toegevoegd' },
      none: 'Niet opgegeven',
      sendFail: 'Het versturen lukte nu niet. Probeer het zo nog eens of mail ons direct via info@skurx.es.',
      done: function (n) { return ['Klaar' + (n ? ', ' + n : '') + '. Ik heb het doorgegeven aan het team; zij nemen persoonlijk contact met je op zodra ze het hebben bekeken.', 'Bedankt voor je tijd. Het was me een genoegen.']; },
      restart: 'Opnieuw beginnen',
      back: function (n) { return 'Welkom terug' + (n ? ', ' + n : '') + '. We gaan verder waar we gebleven waren.'; },
      backDone: function (n) { return ['Welkom terug' + (n ? ', ' + n : '') + '. We hebben je aanvraag al en het team neemt contact met je op.', 'Wil je me iets anders vertellen, dan kunnen we een nieuw gesprek beginnen.']; },
      price: ['Ik noem liever geen bedrag zonder je situatie te kennen: elk bedrijf is anders.', 'Wat ik wel kan doen, is je situatie voorbereiden zodat het team je precies kan vertellen wat ze zouden doen en wat het kost.'],
      privacy: ['Wat je me hier vertelt, gebruikt alleen het team van SKURX SYSTEMS om je vraag te behandelen, en het wordt met niemand gedeeld. De details vind je in het privacybeleid, hieronder gelinkt.'],
      backTo: 'Terug naar jouw situatie: ',
      typing: 'Fini is aan het typen',
      priceRe: /\b(prijs|prijzen|kosten|kost|hoeveel|offerte|budget|tarief)\b/i,
      privacyRe: /\b(privacy|persoonsgegevens|avg|gegevensbescherming|vertrouwelijk)\b/i,
      nameStrip: /^(hallo|hoi|goedemorgen|goedemiddag)[\s,.!]+|^(ik heet|ik ben|mijn naam is)\s+/gi
    }
  };

  var L = T[LANG];
  var panel = document.getElementById('panel-contacto');
  if (!L || !CONFIG.enabled || !panel || typeof panel.showModal !== 'function') return;

  var STORAGE = 'skurx-fini-' + LANG + '-v1';
  var ORDER = ['problema', 'herramientas', 'tiempo', 'empresa', 'urgencia', 'contacto', 'horario'];

  var log = panel.querySelector('.chat-log');
  var quick = panel.querySelector('.chat-quick');
  var form = panel.querySelector('.chat-form');
  var input = panel.querySelector('#chat-input');
  var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  var state = load() || fresh();
  function fresh() { return { step: 'inicio', data: {}, history: [], quick: [] }; }
  function save() { state.savedAt = Date.now(); try { localStorage.setItem(STORAGE, JSON.stringify(state)); } catch (e) {} }
  function load() {
    try {
      var s = JSON.parse(localStorage.getItem(STORAGE));
      if (s && Date.now() - (s.savedAt || 0) < CONFIG.keepDays * 864e5) return s;
      localStorage.removeItem(STORAGE);
    } catch (e) {}
    return null;
  }
  function isReturnVisit() {
    try {
      if (sessionStorage.getItem(STORAGE + '-visit')) return false;
      sessionStorage.setItem(STORAGE + '-visit', '1');
    } catch (e) {}
    return true;
  }

  function pick(list) { return list[Math.floor(Math.random() * list.length)]; }
  function wait(ms) { return new Promise(function (r) { setTimeout(r, reduceMotion ? 0 : ms); }); }
  function typingTime(t) { return 450 + Math.min(t.length * 16, 1700); }
  function scrollDown() { log.scrollTop = log.scrollHeight; }
  function name() { return (state.data.nombre || '').split(' ')[0]; }

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
  function push(msg) { state.history.push(msg); save(); render(msg); }

  function showTyping() {
    var row = document.createElement('div');
    row.className = 'chat-msg from-fini typing';
    var last = log.lastElementChild;
    if (!(last && last.classList.contains('from-fini'))) row.classList.add('first');
    var bubble = document.createElement('div');
    bubble.className = 'chat-bubble';
    bubble.setAttribute('aria-label', L.typing);
    bubble.innerHTML = '<span></span><span></span><span></span>';
    row.appendChild(bubble);
    log.appendChild(row);
    scrollDown();
    return row;
  }

  async function say(texts) {
    setQuick([]);
    for (var i = 0; i < texts.length; i++) {
      var msg = typeof texts[i] === 'string' ? { who: 'fini', text: texts[i] } : Object.assign({ who: 'fini' }, texts[i]);
      var dots = showTyping();
      await wait(typingTime(msg.text));
      dots.remove();
      if (/\?/.test(msg.text)) state.lastQ = msg.text;
      push(msg);
      if (i < texts.length - 1) await wait(350);
    }
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
    await say((before || []).concat([L.q[step]]));
    if (L.quick[step]) setQuick(L.quick[step]);
  }

  function nextStep(step) {
    var i = ORDER.indexOf(step);
    return i === -1 || i === ORDER.length - 1 ? null : ORDER[i + 1];
  }

  function extractName(text) {
    var t = text.trim().replace(/^(hello|hi|hey|hola|ciao)[\s,.!]+/i, '').replace(L.nameStrip, '').replace(L.nameStrip, '').replace(/[.,!¡?¿].*$/, '').trim();
    var parts = t.split(/\s+/).filter(function (w) { return /^[\p{L}'’-]+$/u.test(w); }).slice(0, 3);
    if (!parts.length || parts[0].length < 2) return '';
    return parts.map(function (w) { return w.charAt(0).toUpperCase() + w.slice(1).toLowerCase(); }).join(' ');
  }
  function looksLikeContact(text) {
    return /\S+@\S+\.\S+/.test(text) || (text.replace(/\D/g, '').length >= 7);
  }

  function summary() {
    state.step = 'confirmar';
    var d = state.data, lb = L.labels, list = [];
    if (d.interes) list.push([lb.interes, d.interes]);
    ['problema', 'herramientas', 'tiempo', 'empresa', 'urgencia'].forEach(function (k) { if (d[k]) list.push([lb[k], d[k]]); });
    list.push([lb.nombre, d.nombre || L.none]);
    list.push([lb.contacto, d.contacto + (d.horario ? ' (' + d.horario.toLowerCase() + ')' : '')]);
    if (d.notas) list.push([lb.notas, d.notas]);
    save();
    return say([{ text: L.summaryIntro, list: list }, L.summaryOk]).then(function () { setQuick(L.confirm); });
  }

  async function send() {
    state.step = 'enviando';
    save();
    var d = state.data;
    var transcript = state.history.map(function (m) {
      return (m.who === 'fini' ? 'Fini: ' : 'Usuario: ') + m.text + (m.list ? '\n' + m.list.map(function (i) { return '  - ' + i[0] + ': ' + i[1]; }).join('\n') : '');
    }).join('\n');
    var tag = '[' + LANG.toUpperCase() + '] ';
    var ok = true;
    if (CONFIG.web3formsKey) {
      try {
        var res = await fetch('https://api.web3forms.com/submit', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json', Accept: 'application/json' },
          body: JSON.stringify({
            access_key: CONFIG.web3formsKey,
            subject: tag + (d.interes ? (d.interes === L.review ? 'Solicitud de revisión exprés: ' : 'Solicitud de auditoría: ') : 'Nueva conversación con Fini: ') + (d.nombre || ''),
            from_name: 'Fini · SKURX SYSTEMS',
            idioma: LANG.toUpperCase(),
            interes: d.interes || '',
            nombre: d.nombre || '',
            contacto: d.contacto || '',
            horario: d.horario || '',
            situacion: d.problema || '',
            herramientas: d.herramientas || '',
            tiempo: d.tiempo || '',
            empresa: d.empresa || '',
            urgencia: d.urgencia || '',
            notas: d.notas || '',
            pagina: location.pathname,
            conversacion: transcript,
            botcheck: ''
          })
        });
        ok = res.ok;
      } catch (e) { ok = false; }
    } else {
      console.info('[Fini ' + LANG + '] Test mode, nothing sent.\n\n' + transcript);
    }
    if (!ok) {
      state.step = 'confirmar';
      save();
      await say([L.sendFail]);
      return setQuick([L.confirm[0]]);
    }
    state.step = 'fin';
    save();
    await say(L.done(name()));
    setQuick([L.restart]);
  }

  async function handle(text) {
    var step = state.step;

    if (step === 'fin') { await say(L.backDone(name())); return setQuick([L.restart]); }
    if (step === 'confirmar') {
      if (text === L.confirm[0]) return send();
      state.step = 'anadir';
      save();
      return say([L.addWhat]);
    }
    if (step === 'anadir') {
      state.data.notas = (state.data.notas ? state.data.notas + ' · ' : '') + text;
      return summary();
    }

    // Preguntas sueltas a mitad de conversación: precio o privacidad.
    if (step !== 'saludo' && step !== 'contacto' && L.priceRe.test(text)) {
      await say(L.price);
      return say([L.backTo + L.q[step]]).then(function () { if (L.quick[step]) setQuick(L.quick[step]); });
    }
    if (L.privacyRe.test(text) && step !== 'contacto') {
      await say(L.privacy);
      return say([step === 'saludo' ? L.greeting[1] : L.backTo + L.q[step]]).then(function () { if (L.quick[step]) setQuick(L.quick[step]); });
    }

    if (step === 'saludo' || step === 'inicio') {
      state.data.nombre = extractName(text);
      save();
      return ask('problema', [L.nice(name())]);
    }
    if (step === 'contacto') {
      if (!looksLikeContact(text)) return say([L.badContact]);
      state.data.contacto = text.trim();
      save();
      return ask('horario');
    }
    if (step === 'horario') {
      state.data.horario = text.trim();
      save();
      return summary();
    }
    if (ORDER.indexOf(step) !== -1) {
      state.data[step] = text.trim();
      save();
      var next = nextStep(step);
      var ack = (step === 'problema' || step === 'herramientas') ? [pick(L.acks)] : [];
      return ask(next, ack);
    }
  }

  var processing = false;
  var pending = [];
  async function submit(text) {
    text = (text || '').trim();
    if (!text) return;
    if (text === L.restart) {
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

  // data-fini-intent del botón: «auditoria» o «revision» (Revisión exprés).
  function interestFrom(intent) {
    return intent === 'auditoria' ? L.audit : intent === 'revision' ? L.review : null;
  }

  async function start(interest) {
    processing = true;
    state.step = 'saludo';
    if (interest) state.data.interes = interest;
    save();
    await say(interest === L.review ? [L.greetingAudit[0], L.reviewLine, L.greetingAudit[2]] : interest ? L.greetingAudit : L.greeting);
    await drain();
  }

  // Lo que el usuario escribe mientras Fini aún habla se atiende al terminar.
  async function drain() {
    while (pending.length) {
      var t = pending.join('\n');
      pending = [];
      await handle(t);
    }
    processing = false;
  }

  async function welcomeBack() {
    processing = true;
    var keep = (state.quick || []).filter(function (q) { return q !== L.restart; });
    if (state.step === 'fin') {
      await say(L.backDone(name()));
      setQuick([L.restart]);
    } else if (state.step !== 'inicio') {
      if (state.step === 'enviando') state.step = 'confirmar';
      await say([L.back(name())].concat(state.lastQ ? [state.lastQ] : []));
      setQuick(keep.concat([L.restart]));
    }
    await drain();
  }

  function autosize() {
    input.style.height = 'auto';
    input.style.height = Math.min(input.scrollHeight, 140) + 'px';
  }
  input.addEventListener('input', autosize);
  input.addEventListener('keydown', function (e) {
    if (e.key === 'Enter' && !e.shiftKey && !e.isComposing) { e.preventDefault(); form.requestSubmit(); }
  });
  form.addEventListener('submit', function (e) {
    e.preventDefault();
    var text = input.value;
    input.value = '';
    autosize();
    submit(text);
  });

  var trigger = null;
  var scrollY = 0;
  function open(event) {
    event.preventDefault();
    trigger = event.currentTarget;
    var interest = interestFrom(trigger && trigger.getAttribute('data-fini-intent'));
    if (interest && state.history.length && !state.data.interes) { state.data.interes = interest; save(); }
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
        start(interest);
      }
    }
    setTimeout(function () { input.focus({ preventScroll: true }); scrollDown(); }, reduceMotion ? 0 : 300);
  }
  function close() {
    panel.classList.add('is-closing');
    var done = function () { panel.classList.remove('is-closing'); panel.close(); };
    if (reduceMotion) done(); else setTimeout(done, 220);
  }
  panel.addEventListener('close', function () {
    document.documentElement.classList.remove('panel-open');
    window.scrollTo({ top: scrollY, behavior: 'instant' });
    if (trigger) trigger.focus({ preventScroll: true });
  });
  panel.addEventListener('cancel', function (e) { e.preventDefault(); close(); });
  panel.addEventListener('click', function (e) { if (e.target === panel) close(); });
  document.querySelectorAll('[data-contact-open]').forEach(function (el) { el.addEventListener('click', open); });
  panel.querySelectorAll('[data-contact-close]').forEach(function (el) { el.addEventListener('click', close); });
})();
