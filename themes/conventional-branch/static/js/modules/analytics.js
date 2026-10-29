// Google Analytics events, sent through the gtag() that head.html defines.
//
// A page without it, or one whose tag throws, loses the event and nothing else: what
// a reader came to do must never depend on analytics.

export function track(name, params) {
  if (typeof window.gtag !== 'function') return;
  try {
    window.gtag('event', name, params);
  } catch (error) {
    // Nothing to recover; the event is simply not counted.
  }
}
