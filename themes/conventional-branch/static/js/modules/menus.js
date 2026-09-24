// The header's menus are <details> elements, so they work without this script. It adds
// what a menu is expected to do: one open at a time, closed by Escape or a click outside.

export function initMenus() {
  const menus = Array.from(document.querySelectorAll('details.menu'));
  if (!menus.length) return;

  menus.forEach((menu) => {
    menu.addEventListener('toggle', () => {
      if (!menu.open) return;
      menus.forEach((other) => {
        if (other !== menu) other.open = false;
      });
    });
  });

  document.addEventListener('click', (event) => {
    menus.forEach((menu) => {
      if (menu.open && !menu.contains(event.target)) menu.open = false;
    });
  });

  document.addEventListener('keydown', (event) => {
    if (event.key !== 'Escape') return;
    menus.forEach((menu) => {
      if (!menu.open) return;
      menu.open = false;
      menu.querySelector('summary').focus();
    });
  });
}
