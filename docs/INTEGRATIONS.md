# Integrations — job-by-job guide

**You do NOT need to pre-configure integrations before starting a client.**  
The site already has the wiring. When you have a link, edit **one file** and push.

## The only file to edit

`js/site-config.js`

```javascript
integrations: {
  calendlyUrl: '',      // ← paste Calendly event URL
  social: {
    instagram: '',       // ← full profile URL
    tiktok: '',
    // ...
  },
  payments: {
    stripeLink: '',      // ← Stripe Payment Link
    paypalLink: '',
    venmoLink: ''
  }
}
```

Empty = hidden on the site. Filled = appears automatically (`js/integrations.js`).

---

## What to tell the agent (copy-paste examples)

| You say | Agent edits |
|---------|-------------|
| "Add Calendly: https://calendly.com/vincent/15min" | `calendlyUrl` |
| "Add Instagram https://instagram.com/handle" | `social.instagram` |
| "Add TikTok https://tiktok.com/@handle" | `social.tiktok` |
| "Add Stripe pay link https://buy.stripe.com/..." | `payments.stripeLink` |
| "Add PayPal https://paypal.me/name" | `payments.paypalLink` |
| "Remove Calendly" | set `calendlyUrl` to `''` |

Then: commit + push → live in ~1–2 min on GitHub Pages.

**No rebuild, no new pages, no re-explaining the whole project.**

---

## Where each integration appears

| Integration | On the site |
|-------------|-------------|
| Calendly | Nav **Book a call** + `#book` section with embed |
| Social URLs | Footer row + contact section |
| Stripe / PayPal / Venmo | Buttons under contact ("Pay with Card", etc.) |

---

## How to get each link

### Calendly (free tier works)
1. Sign up at [calendly.com](https://calendly.com)
2. Create an event (e.g. "15 Minute Meeting")
3. Copy the event link → `calendlyUrl`

### Instagram / TikTok / etc.
Use the **full profile URL** from the browser address bar, e.g.:
- `https://www.instagram.com/yourhandle/`
- `https://www.tiktok.com/@yourhandle`

### Stripe Payment Link
1. [dashboard.stripe.com](https://dashboard.stripe.com) → Payment Links → Create
2. Set amount/description → copy link → `stripeLink`

### PayPal
`https://paypal.me/YourUsername`

### Venmo
`https://venmo.com/YourUsername`

---

## Vincent's site (current)

All integration fields are **intentionally empty** until Vincent creates accounts and sends you URLs.  
Contact form and email still work without these.

When ready, paste URLs into `js/site-config.js` and push.

---

## Future clients — naming

| Client | GitHub repo name | Local folder |
|--------|------------------|--------------|
| Vincent Martinez | `vincent-web-portfolio` | `~/Projects/vincent-web-portfolio` |
| Next client | `clientname-web-portfolio` | `~/Projects/clientname-web-portfolio` |

Use `scripts/bootstrap-new-client.sh clientname-web-portfolio` to clone the template.
