(function () {
  const cfg = window.SITE_CONFIG;
  if (!cfg) return;

  const { integrations } = cfg;
  const social = integrations.social || {};
  const payments = integrations.payments || {};

  const SOCIAL_LABELS = {
    instagram: 'Instagram',
    facebook: 'Facebook',
    tiktok: 'TikTok',
    youtube: 'YouTube',
    linkedin: 'LinkedIn',
    x: 'X'
  };

  function hasSocial() {
    return Object.values(social).some((url) => url && url.trim());
  }

  function renderSocial(container) {
    if (!container || !hasSocial()) return;

    const frag = document.createDocumentFragment();
    Object.entries(social).forEach(([key, url]) => {
      if (!url || !url.trim()) return;
      const a = document.createElement('a');
      a.href = url.trim();
      a.target = '_blank';
      a.rel = 'noopener noreferrer';
      a.className = 'social-link';
      a.textContent = SOCIAL_LABELS[key] || key;
      frag.appendChild(a);
    });
    container.appendChild(frag);
    container.hidden = false;
  }

  function renderCalendly() {
    const section = document.getElementById('book');
    const embed = document.getElementById('calendly-embed');
    const url = (integrations.calendlyUrl || '').trim();
    if (!section || !embed || !url) return;

    section.hidden = false;
    const navBook = document.getElementById('nav-book');
    if (navBook) navBook.hidden = false;

    const iframe = document.createElement('iframe');
    iframe.src = url.replace(/\/?$/, '/') + '?hide_gdpr_banner=1';
    iframe.title = 'Schedule a call';
    iframe.loading = 'lazy';
    embed.appendChild(iframe);
  }

  function renderPayments(container) {
    if (!container) return;

    const links = [
      { key: 'stripeLink', label: 'Pay with Card (Stripe)' },
      { key: 'paypalLink', label: 'PayPal' },
      { key: 'venmoLink', label: 'Venmo' }
    ];

    const frag = document.createDocumentFragment();
    let count = 0;

    links.forEach(({ key, label }) => {
      const url = (payments[key] || '').trim();
      if (!url) return;
      const a = document.createElement('a');
      a.href = url;
      a.target = '_blank';
      a.rel = 'noopener noreferrer';
      a.className = count === 0 ? 'btn btn-primary' : 'btn btn-ghost';
      a.textContent = label;
      frag.appendChild(a);
      count += 1;
    });

    if (count === 0) return;
    container.appendChild(frag);
    container.hidden = false;
  }

  renderSocial(document.getElementById('footer-social'));
  renderSocial(document.getElementById('contact-social'));
  renderCalendly();
  renderPayments(document.getElementById('payment-links'));
})();
