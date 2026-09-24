// A copy button on every code block in the rendered Markdown.

const COPY_ICON = '<svg class="icon" width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><rect x="9" y="9" width="11" height="11" rx="2"/><path d="M5 15V6a2 2 0 0 1 2-2h8"/></svg>';

function labels() {
  const { copyLabel = 'Copy', copiedLabel = 'Copied' } = document.body.dataset;
  return { copy: copyLabel, copied: copiedLabel };
}

// For pages served without a secure context, where navigator.clipboard is missing.
function copyWithSelection(text) {
  const area = document.createElement('textarea');
  area.value = text;
  area.setAttribute('readonly', '');
  area.style.position = 'fixed';
  area.style.opacity = '0';
  document.body.append(area);
  area.select();
  try {
    document.execCommand('copy');
  } finally {
    area.remove();
  }
}

async function copy(text, button) {
  try {
    await navigator.clipboard.writeText(text);
  } catch (error) {
    copyWithSelection(text);
  }
  const { copy: idle, copied } = labels();
  const label = button.querySelector('span');
  if (label) label.textContent = copied;
  button.classList.add('is-copied');
  clearTimeout(button.copyTimer);
  button.copyTimer = setTimeout(() => {
    if (label) label.textContent = idle;
    button.classList.remove('is-copied');
  }, 1600);
}

export function initCopy(root) {
  root.querySelectorAll('.markdown-body pre').forEach((pre) => {
    if (pre.parentElement.classList.contains('code-block')) return;
    const wrap = document.createElement('div');
    wrap.className = 'code-block';
    pre.before(wrap);
    wrap.append(pre);

    const button = document.createElement('button');
    button.type = 'button';
    button.className = 'copy-button';
    button.innerHTML = COPY_ICON;
    const label = document.createElement('span');
    label.textContent = labels().copy;
    button.append(label);
    wrap.append(button);
    button.addEventListener('click', () => copy(pre.textContent.replace(/\n$/, ''), button));
  });
}
