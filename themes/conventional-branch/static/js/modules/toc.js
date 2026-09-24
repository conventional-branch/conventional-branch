// Marks the "On this page" entry for the section being read. On a phone the outline is
// a disclosure that starts closed, so the text comes first; on a wider screen it is always
// open and its label is only a label. Crossing the breakpoint, by rotating a tablet or
// resizing a window, switches between the two.

const THRESHOLD = 140;
const PHONE = '(max-width: 899px)';

function initDisclosure(details) {
  const summary = details.querySelector('summary');
  const phone = window.matchMedia(PHONE);
  const sync = () => {
    details.open = !phone.matches;
    summary.inert = !phone.matches;
  };
  sync();
  phone.addEventListener('change', sync);
}

export function initToc() {
  const toc = document.querySelector('.toc');
  if (!toc) return;

  const details = toc.querySelector('.toc__details');
  if (details) initDisclosure(details);

  const entries = [];
  toc.querySelectorAll('a[href^="#"]').forEach((link) => {
    const target = document.getElementById(decodeURIComponent(link.hash.slice(1)));
    if (target) entries.push({ link, target });
  });
  if (!entries.length) return;

  let active = null;
  let frame = 0;

  const update = () => {
    frame = 0;
    let current = null;
    for (const entry of entries) {
      if (entry.target.getBoundingClientRect().top > THRESHOLD) break;
      current = entry;
    }
    if (current === active) return;
    if (active) {
      active.link.classList.remove('is-active');
      active.link.removeAttribute('aria-current');
    }
    active = current;
    if (active) {
      active.link.classList.add('is-active');
      active.link.setAttribute('aria-current', 'location');
    }
  };

  window.addEventListener('scroll', () => {
    if (!frame) frame = requestAnimationFrame(update);
  }, { passive: true });
  update();
}
