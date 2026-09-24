// Marks the "On this page" entry for the section being read.

const THRESHOLD = 140;

export function initToc() {
  const toc = document.querySelector('.toc');
  if (!toc) return;

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
