import AnchorJS from 'anchor-js';
import { initMenus } from './modules/menus';
import { initChecker } from './modules/checker';
import { enhanceExamples } from './modules/examples';
import { initFaq } from './modules/faq';
import { initCopy } from './modules/copy';
import { initToc } from './modules/toc';

function start() {
  initMenus();
  document.querySelectorAll('[data-checker]').forEach(initChecker);
  document.querySelectorAll('.spec__body').forEach((body) => {
    enhanceExamples(body);
    initFaq(body);
  });
  initCopy(document);

  // A "#" beside each heading, for citing a section of the specification.
  const anchors = new AnchorJS({ placement: 'right', icon: '#' });
  anchors.add('.markdown-body h2:not(.spec__title), .markdown-body h3:not(.faq-item__question)');

  initToc();
}

if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', start);
} else {
  start();
}
