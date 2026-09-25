// The branch-name checker on the homepage.
//
// The page renders the checker in the state of its first example; this makes it live.
// A name is judged by the regex published in spec.json, which the page embeds. The
// finer rules below only explain *why* a name fails, and suggest the nearest valid one.

// A description as the grammar defines it: lowercase letters and digits, words joined
// by single hyphens, and dots between the parts of a version number.
const DESCRIPTION = /^[a-z0-9]+(?:\.[a-z0-9]+)*(?:-[a-z0-9]+(?:\.[a-z0-9]+)*)*$/;

// Near misses worth correcting rather than only rejecting.
const TYPE_TYPOS = {
  features: 'feature',
  bug: 'bugfix',
  bugs: 'bugfix',
  fixes: 'fix',
  hot: 'hotfix',
  releases: 'release',
  chores: 'chore',
};

// In a monospace face every character is 0.6em wide, which is what lets the name be
// sized to fit its line.
const ADVANCE = 0.6;

export function initChecker(root) {
  const dataNode = root.querySelector('[data-checker-data]');
  if (!dataNode) return;

  const data = JSON.parse(dataNode.textContent);
  const pattern = new RegExp(data.regex);
  const trunk = new Set(data.trunk);
  const types = new Map();
  data.types.forEach((type) => {
    [type.type, ...(type.aliases || [])].forEach((name) => types.set(name, type));
  });

  const find = (selector) => root.querySelector(selector);
  const input = find('[data-input]');
  const stage = find('[data-stage]');
  const brackets = {
    type: find('[data-bracket="type"]'),
    sep: find('[data-bracket="sep"]'),
    desc: find('[data-bracket="desc"]'),
    whole: find('[data-bracket="whole"]'),
  };
  const wholeLabel = brackets.whole.querySelector('.bracket__label');
  const readings = find('[data-readings]');
  const person = find('[data-person]');
  const json = find('[data-json]');
  const pipeline = find('[data-pipeline]');
  const error = find('[data-error]');
  const message = find('[data-message]');
  const fix = find('[data-fix]');
  const fixName = find('[data-fix-name]');
  const empty = find('[data-empty]');
  const status = find('[data-status]');
  const statusText = find('[data-status-text]');
  const announcer = find('[data-announce]');

  let suggestion = '';
  let announceTimer = 0;

  function reason(name, type, desc, typeKnown) {
    const m = data.messages;
    if (/[A-Z]/.test(name)) return m.uppercase;
    if (/\s/.test(name)) return m.space;
    if (/_/.test(name)) return m.underscore;
    if (!typeKnown) return m.unknownType.replace('{type}', type);
    if (desc === '') return m.empty;
    if (desc.includes('/')) return m.slash;
    if (/[^a-z0-9.-]/.test(desc)) return m.chars;
    if (/--/.test(desc)) return m.doubleHyphen;
    if (/\.\./.test(desc)) return m.doubleDot;
    if (/^[-.]/.test(desc)) return m.leading;
    if (/[-.]$/.test(desc)) return m.trailing;
    if (/-\.|\.-/.test(desc)) return m.hyphenDot;
    return m.grammar;
  }

  function suggest(name, type, desc) {
    const lowered = type.trim().toLowerCase();
    const fixedType = TYPE_TYPOS[lowered] || lowered;
    const fixedDesc = desc
      .trim()
      .toLowerCase()
      .replace(/[\s_/]+/g, '-')
      .replace(/[^a-z0-9.-]/g, '')
      .replace(/(?:-\.|\.-)+/g, '.')
      .replace(/-{2,}/g, '-')
      .replace(/\.{2,}/g, '.')
      .replace(/^[-.]+|[-.]+$/g, '');
    const candidate = `${fixedType}/${fixedDesc}`;
    return candidate !== name && pattern.test(candidate) ? candidate : '';
  }

  function analyze(name) {
    const base = { state: 'empty', split: false, whole: false };
    if (name === '') return base;

    if (trunk.has(name)) {
      return {
        ...base,
        state: 'ok',
        whole: true,
        caption: data.labels.trunk,
        reading: {
          person: data.trunkReading.person,
          human: data.trunkReading.human,
          json: [['trunk', name]],
          pipeline: data.trunkReading.pipeline,
        },
      };
    }

    const slash = name.indexOf('/');
    if (slash < 0) {
      return { ...base, state: 'bad', whole: true, caption: data.labels.missing, message: data.messages.missingType, fix: '' };
    }

    const type = name.slice(0, slash);
    const desc = name.slice(slash + 1);
    const info = types.get(type);
    const parts = {
      ...base,
      split: true,
      typeLength: type.length,
      descLength: desc.length,
      typeKnown: Boolean(info),
      descValid: DESCRIPTION.test(desc),
    };

    if (info && pattern.test(name)) {
      return {
        ...parts,
        state: 'ok',
        reading: {
          person: info.person,
          human: desc.split('-').join(' '),
          json: [['type', info.type], ['category', info.category], ['description', desc]],
          pipeline: info.pipeline,
        },
      };
    }
    return { ...parts, state: 'bad', message: reason(name, type, desc, parts.typeKnown), fix: suggest(name, type, desc) };
  }

  function fit(length) {
    const width = stage.clientWidth;
    if (!width) return;
    const largest = Math.min(72, width / 11);
    const size = Math.max(16, Math.min(largest, width / (Math.max(length, 10) * ADVANCE)));
    stage.style.setProperty('--fs', `${size.toFixed(2)}px`);
  }

  function renderJson(rows) {
    json.textContent = '{\n';
    rows.forEach(([key, value], index) => {
      const k = document.createElement('span');
      k.className = 'tok-k';
      k.textContent = JSON.stringify(key);
      const v = document.createElement('span');
      v.className = 'tok-s';
      v.textContent = JSON.stringify(value);
      json.append('  ', k, ': ', v, index < rows.length - 1 ? ',\n' : '\n');
    });
    json.append('}');
  }

  function render() {
    const name = input.value;
    const result = analyze(name);
    fit(name.length);

    brackets.type.hidden = !result.split;
    brackets.sep.hidden = !result.split;
    brackets.desc.hidden = !result.split;
    brackets.whole.hidden = !result.whole;
    if (result.split) {
      brackets.type.style.setProperty('--len', result.typeLength);
      brackets.desc.style.setProperty('--len', result.descLength);
      brackets.type.classList.toggle('is-bad', !result.typeKnown);
      brackets.desc.classList.toggle('is-bad', !result.descValid);
    }
    if (result.whole) {
      brackets.whole.style.setProperty('--len', Math.max(name.length, 1));
      brackets.whole.classList.toggle('is-bad', result.state !== 'ok');
      wholeLabel.textContent = result.caption;
    }

    readings.hidden = result.state !== 'ok';
    error.hidden = result.state !== 'bad';
    empty.hidden = result.state !== 'empty';

    if (result.state === 'ok') {
      person.textContent = `${result.reading.person}: `;
      const em = document.createElement('em');
      em.textContent = `“${result.reading.human}”`;
      person.append(em);
      renderJson(result.reading.json);
      pipeline.textContent = result.reading.pipeline;
    } else if (result.state === 'bad') {
      message.textContent = result.message;
      suggestion = result.fix;
      fix.hidden = !suggestion;
      fixName.textContent = suggestion;
    }

    const verdict = result.state === 'ok' ? 'ok' : result.state === 'bad' ? 'bad' : 'waiting';
    status.classList.toggle('is-bad', verdict === 'bad');
    status.classList.toggle('is-waiting', verdict === 'waiting');
    statusText.textContent = data.status[verdict];

    // Screen readers hear the verdict once typing pauses, not on every keystroke.
    clearTimeout(announceTimer);
    announceTimer = setTimeout(() => {
      announcer.textContent = verdict === 'bad' ? `${data.status.bad}. ${result.message}` : data.status[verdict];
    }, 600);
  }

  input.addEventListener('input', render);
  root.querySelectorAll('[data-example]').forEach((button) => {
    button.addEventListener('click', () => {
      input.value = button.dataset.example;
      render();
    });
  });
  fix.addEventListener('click', () => {
    if (!suggestion) return;
    input.value = suggestion;
    render();
    input.focus();
  });

  let frame = 0;
  window.addEventListener('resize', () => {
    cancelAnimationFrame(frame);
    frame = requestAnimationFrame(() => fit(input.value.length));
  });

  render();
}
