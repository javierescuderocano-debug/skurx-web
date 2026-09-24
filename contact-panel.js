// Panel de contacto: se abre sobre la página y, al cerrarlo, deja al usuario en el mismo punto.
(function () {
  var panel = document.getElementById('panel-contacto');
  if (!panel || typeof panel.showModal !== 'function') return;

  var note = panel.querySelector('.panel-note');
  var trigger = null;
  var scrollY = 0;

  function open(event) {
    event.preventDefault();
    trigger = event.currentTarget;
    scrollY = window.scrollY;
    note.textContent = '';
    document.documentElement.classList.add('panel-open');
    panel.showModal();
  }

  function close() {
    panel.classList.add('is-closing');
    var done = function () {
      panel.classList.remove('is-closing');
      panel.close();
    };
    if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) done();
    else setTimeout(done, 220);
  }

  panel.addEventListener('close', function () {
    document.documentElement.classList.remove('panel-open');
    window.scrollTo({ top: scrollY, behavior: 'instant' });
    if (trigger) trigger.focus({ preventScroll: true });
  });

  // Esc: usamos la misma animación de cierre.
  panel.addEventListener('cancel', function (event) {
    event.preventDefault();
    close();
  });

  // Clic fuera del panel (sobre el fondo).
  panel.addEventListener('click', function (event) {
    if (event.target === panel) close();
  });

  document.querySelectorAll('[data-contact-open]').forEach(function (el) {
    el.addEventListener('click', open);
  });
  panel.querySelectorAll('[data-contact-close]').forEach(function (el) {
    el.addEventListener('click', close);
  });

  panel.querySelectorAll('[data-copy]').forEach(function (btn) {
    btn.addEventListener('click', function () {
      var value = btn.getAttribute('data-copy');
      if (!navigator.clipboard) return;
      navigator.clipboard.writeText(value).then(function () {
        note.textContent = 'Copiado: ' + value;
      });
    });
  });
})();
