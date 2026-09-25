// The examples table on a specification page marks each name ✅ or ❌. This draws those
// marks as icons and highlights the part of each invalid name that breaks a rule.
//
// The Markdown is left exactly as it is: tests/conformance.py reads the table from it,
// in all eleven languages, and holds every row to the specification's regex.

const ICON = {
  valid: '<svg class="icon" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M5 12.5l4.5 4.5L19 7.5"/></svg>',
  invalid: '<svg class="icon" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false"><path d="M6 6l12 12"/><path d="M18 6L6 18"/></svg>',
};

// Every match of `re` in `text`, as [start, end) ranges shifted by `offset`.
function matches(re, text, offset = 0) {
  const global = new RegExp(re.source, 'g');
  const ranges = [];
  let match = global.exec(text);
  while (match) {
    ranges.push([match.index + offset, match.index + offset + match[0].length]);
    match = global.exec(text);
  }
  return ranges;
}

// The characters that make a name invalid, found in the order the rules are usually
// explained: case, spaces and underscores, the type, then the description's separators.
function offending(name, knownTypes) {
  if (/[A-Z]/.test(name)) return matches(/[A-Z]/, name);
  if (/\s/.test(name)) return matches(/\s/, name);
  if (/_/.test(name)) return matches(/_/, name);

  const slash = name.indexOf('/');
  if (slash < 0) return [[0, name.length]];
  const type = name.slice(0, slash);
  const desc = name.slice(slash + 1);
  const at = slash + 1;

  if (knownTypes.size && !knownTypes.has(type)) return [[0, slash]];
  if (/--/.test(desc)) return matches(/-{2,}/, desc, at);
  if (/\.\./.test(desc)) return matches(/\.{2,}/, desc, at);
  if (/^[-.]/.test(desc)) return [[at, at + 1]];
  if (/[-.]$/.test(desc)) return [[name.length - 1, name.length]];
  if (/-\.|\.-/.test(desc)) return matches(/-\.|\.-/, desc, at);
  return [];
}

function highlight(code, ranges) {
  if (!ranges.length) return;
  const text = code.textContent;
  const parts = [];
  let last = 0;
  ranges.forEach(([start, end]) => {
    if (start > last) parts.push(document.createTextNode(text.slice(last, start)));
    const mark = document.createElement('mark');
    mark.textContent = text.slice(start, end);
    parts.push(mark);
    last = end;
  });
  if (last < text.length) parts.push(document.createTextNode(text.slice(last)));
  code.replaceChildren(...parts);
}

export function enhanceExamples(body) {
  const knownTypes = new Set((body.dataset.specTypes || '').split(' ').filter(Boolean));

  body.querySelectorAll('table').forEach((table) => {
    const rows = table.tBodies[0] ? Array.from(table.tBodies[0].rows) : [];
    const marks = rows.map((row) => (row.cells[1] ? row.cells[1].textContent.trim() : ''));
    if (!rows.length || !marks.every((mark) => mark === '✅' || mark === '❌')) return;

    table.classList.add('examples');
    rows.forEach((row, index) => {
      const valid = marks[index] === '✅';
      const verdict = document.createElement('span');
      verdict.className = `verdict verdict--${valid ? 'valid' : 'invalid'}`;
      verdict.innerHTML = valid ? ICON.valid : ICON.invalid;
      // The original mark stays for screen readers, which read it in any language.
      const label = document.createElement('span');
      label.className = 'visually-hidden';
      label.textContent = marks[index];
      verdict.append(label);
      row.cells[1].replaceChildren(verdict);

      if (!valid) {
        const code = row.cells[0].querySelector('code');
        if (code) highlight(code, offending(code.textContent, knownTypes));
      }
    });
  });
}
