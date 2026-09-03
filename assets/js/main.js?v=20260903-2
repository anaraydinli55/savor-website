(() => {
  const header = document.querySelector('#siteHeader');
  const button = document.querySelector('.menu-button');
  const nav = document.querySelector('#mobileNav');

  const onScroll = () => header?.classList.toggle('scrolled', window.scrollY > 24);
  onScroll();
  window.addEventListener('scroll', onScroll, { passive: true });

  const setMenu = (open) => {
    if (!nav || !button) return;
    nav.classList.toggle('open', open);
    header?.classList.toggle('menu-active', open);
    button.setAttribute('aria-expanded', String(open));
    document.body.classList.toggle('menu-open', open);
    document.documentElement.classList.toggle('menu-open', open);
  };

  button?.addEventListener('click', () => setMenu(!nav?.classList.contains('open')));
  nav?.querySelectorAll('a').forEach((link) => link.addEventListener('click', () => setMenu(false)));
  document.addEventListener('keydown', (event) => {
    if (event.key === 'Escape' && nav?.classList.contains('open')) setMenu(false);
  });
  window.addEventListener('resize', () => {
    if (window.innerWidth > 1080 && nav?.classList.contains('open')) setMenu(false);
  }, { passive: true });

  document.querySelectorAll('[data-reveal]').forEach((el) => {
    if (!('IntersectionObserver' in window)) {
      el.classList.add('is-visible');
      return;
    }
    const observer = new IntersectionObserver(([entry]) => {
      if (entry.isIntersecting) { el.classList.add('is-visible'); observer.disconnect(); }
    }, { threshold: .12 });
    observer.observe(el);
  });

  const form = document.querySelector('[data-contact-form]');
  form?.addEventListener('submit', async (event) => {
    event.preventDefault();
    const status = form.querySelector('[data-form-status]');
    const submitButton = form.querySelector('button[type=submit]');
    submitButton.disabled = true; status.textContent = '';
    try {
      const response = await fetch(form.action, { method: 'POST', body: new FormData(form), headers: { 'X-Requested-With': 'XMLHttpRequest' } });
      const result = await response.json();
      status.textContent = result.message; status.className = result.ok ? 'form-status success' : 'form-status error';
      if (result.ok) form.reset();
    } catch (_) { status.textContent = form.dataset.error; status.className = 'form-status error'; }
    submitButton.disabled = false;
  });
})();
