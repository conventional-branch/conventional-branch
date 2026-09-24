// Folds the FAQ into disclosures, one per question. Every language's specification
// page ends with its FAQ, so it is found as the last second-level section rather than
// by a heading whose text differs from language to language.

export function initFaq(body) {
  const sections = body.querySelectorAll(':scope > h2');
  if (!sections.length) return;

  const groups = [];
  let node = sections[sections.length - 1].nextElementSibling;
  while (node && node.tagName !== 'H2') {
    const next = node.nextElementSibling;
    if (node.tagName === 'H3') {
      groups.push({ question: node, answer: [] });
    } else if (groups.length) {
      groups[groups.length - 1].answer.push(node);
    }
    node = next;
  }
  if (groups.length < 2) return;

  groups.forEach(({ question, answer }, index) => {
    const details = document.createElement('details');
    details.className = 'faq-item';
    details.open = index === 0;
    const summary = document.createElement('summary');
    const content = document.createElement('div');
    content.className = 'faq-item__answer';

    question.before(details);
    question.classList.add('faq-item__question');
    summary.append(question);
    answer.forEach((element) => content.append(element));
    details.append(summary, content);
  });

  // A link to a question — the README links to several — opens it.
  const openTarget = () => {
    if (!window.location.hash) return;
    const target = document.getElementById(decodeURIComponent(window.location.hash.slice(1)));
    const item = target && target.closest('details.faq-item');
    if (item) {
      item.open = true;
      target.scrollIntoView();
    }
  };
  openTarget();
  window.addEventListener('hashchange', openTarget);
}
