# Static Portfolio Build Process

Repeatable workflow for GitHub Pages portfolios (used for Vincent Martinez, July 2026).

## What gets built

- Single-page static site: HTML + CSS + JS
- Hosted free on **GitHub Pages** at `https://GITHUB_USERNAME.github.io/REPO_NAME/`
- Contact form → client email via **FormSubmit** (one-time activation on first submit)
- Optional: Calendly, social links, Stripe/PayPal/Venmo — configured in `js/site-config.js`

## Custom domain vs GitHub URL

| URL type | Example | Who sees it |
|----------|---------|-------------|
| **GitHub Pages (default)** | `jimmythegod100.github.io/web-portfolio` | Your GitHub **account username** — not the client's name |
| **Custom domain (optional)** | `vincentmartinez.com` | Professional branded link — DNS points to GitHub |

The site **files** live in GitHub; the **public link** can stay on github.io or use a purchased domain later.

## New client checklist

1. Copy repo or duplicate `web-portfolio` folder
2. Edit `js/site-config.js` (name, email, URLs)
3. Replace `images/about/` headshot, update copy in `index.html`
4. Match honesty level to client skill (see Vincent revision: Wix beginner vs agency)
5. Create GitHub repo → push → enable Pages (Settings → Pages → branch `main` / root)
6. Update `_next` in contact form to new site URL + `/thanks.html`
7. Client submits test form → activates FormSubmit email
8. Fill `profiles/` markdown for Upwork/Fiverr/LinkedIn if needed

## Integrations (js/site-config.js)

| Field | When to fill | Where it appears |
|-------|--------------|------------------|
| `calendlyUrl` | Client has Calendly | `#book` section + nav "Book a call" |
| `social.*` | Profile URLs | Footer + contact area |
| `payments.*` | Stripe/PayPal/Venmo links | Below contact form |

Empty = section hidden automatically.

## Agent skill

Personal skill: `~/.cursor/skills/static-portfolio-github-pages/SKILL.md`  
Tell any agent: *"Use the static-portfolio-github-pages skill"* to rebuild without re-explaining.

## Repo

https://github.com/jimmythegod100/web-portfolio
