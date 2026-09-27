/* Botón flotante: pasa a la siguiente sección de la página; al final, vuelve arriba. */
(function () {
  var b = document.querySelector('.next-section');
  if (!b) return;
  var smooth = !(window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches);
  function sections() { return [].slice.call(document.querySelectorAll('main > section')); }
  function next() {
    var limit = window.innerHeight * 0.15, s = sections();
    for (var i = 0; i < s.length; i++) if (s[i].getBoundingClientRect().top > limit + 4) return s[i];
    return null;
  }
  function update() {
    var end = !next() || window.innerHeight + window.scrollY >= document.documentElement.scrollHeight - 4;
    b.classList.toggle('is-top', end);
    b.setAttribute('aria-label', end ? b.getAttribute('data-top-label') : b.getAttribute('data-next-label'));
    b.classList.toggle('is-hidden', !!document.querySelector('dialog[open]'));
  }
  b.addEventListener('click', function () {
    var n = next();
    if (!n || b.classList.contains('is-top')) window.scrollTo({ top: 0, behavior: smooth ? 'smooth' : 'auto' });
    else n.scrollIntoView({ behavior: smooth ? 'smooth' : 'auto', block: 'start' });
  });
  window.addEventListener('scroll', update, { passive: true });
  window.addEventListener('resize', update);
  document.addEventListener('click', function () { setTimeout(update, 50); });
  if (sections().length < 2) b.hidden = true;
  update();
})();
