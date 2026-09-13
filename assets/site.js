document.documentElement.classList.add('js');
const menuToggle = document.querySelector('[data-menu-toggle]');
const nav = document.querySelector('[data-nav]');
const disclosure = document.querySelector('.nav-disclosure');
const mobile = window.matchMedia('(max-width: 980px)');
const background = [...document.querySelectorAll('main, footer')];
const inertBefore = new Map();

function closeDisclosure({ restoreFocus = false } = {}) {
  if (!disclosure) return;
  disclosure.open = false;
  if (restoreFocus) disclosure.querySelector('summary').focus();
}
function closeMenu({ restoreFocus = false } = {}) {
  nav?.classList.remove('open');
  document.body.classList.remove('menu-open');
  if (menuToggle) {
    menuToggle.setAttribute('aria-expanded', 'false');
    menuToggle.setAttribute('aria-label', 'Ouvrir le menu');
    menuToggle.textContent = 'Menu';
  }
  for (const [element, original] of inertBefore) element.inert = original;
  inertBefore.clear();
  closeDisclosure();
  if (restoreFocus) menuToggle?.focus();
}
function openMenu() {
  if (!menuToggle || !nav) return;
  nav.classList.add('open');
  document.body.classList.add('menu-open');
  menuToggle.setAttribute('aria-expanded', 'true');
  menuToggle.setAttribute('aria-label', 'Fermer le menu');
  menuToggle.textContent = 'Fermer';
  background.forEach(element => { inertBefore.set(element, element.inert); element.inert = true; });
}
menuToggle?.addEventListener('click', () => nav?.classList.contains('open') ? closeMenu() : openMenu());
nav?.querySelectorAll('a[href]').forEach(link => link.addEventListener('click', () => closeMenu()));
document.addEventListener('click', event => {
  if (disclosure?.open && !disclosure.contains(event.target)) closeDisclosure();
});
disclosure?.addEventListener('focusout', event => {
  if (event.relatedTarget && !disclosure.contains(event.relatedTarget)) closeDisclosure();
});
disclosure?.querySelector('summary').addEventListener('keydown', event => {
  if (event.key === 'ArrowDown') {
    event.preventDefault();
    disclosure.open = true;
    disclosure.querySelector('a').focus();
  }
});
document.addEventListener('keydown', event => {
  if (event.key === 'Escape') {
    if (disclosure?.open) { event.preventDefault(); closeDisclosure({ restoreFocus: true }); }
    else if (nav?.classList.contains('open')) { event.preventDefault(); closeMenu({ restoreFocus: true }); }
  }
  if (event.key !== 'Tab' || !nav?.classList.contains('open')) return;
  const items = [menuToggle, ...nav.querySelectorAll('summary, a[href]')].filter(element => element.getClientRects().length);
  const first = items[0], last = items[items.length - 1];
  if (event.shiftKey && document.activeElement === first) { event.preventDefault(); last.focus(); }
  else if (!event.shiftKey && document.activeElement === last) { event.preventDefault(); first.focus(); }
});
mobile.addEventListener('change', () => closeMenu());
