# Guterra Broker System — Website

A complete 16-page static website. No build tools or server required — every page is
plain HTML that links one shared stylesheet, so the whole site stays consistent and is
easy to edit.

## Preview it
Unzip, then double-click **`index.html`** (or drag it into any browser). All pages are
linked together through the nav and footer.

## Pages
| File | Page |
|---|---|
| `index.html` | Home |
| `about.html` | About Us |
| `industries.html` | Industries We Serve |
| `areas.html` | Areas We Serve |
| `services.html` | Services overview |
| `services-dry-van.html` … `services-refrigerated.html` | 5 service detail pages |
| `careers.html` | Join Our Team |
| `carriers.html` | Carrier Setup |
| `quote.html` | Request a Quote |
| `contact.html` | Contact Us |
| `legal.html` | Privacy & Terms |
| `404.html` | Not-found page |

## Add your real photos
The site ships with styled placeholders wherever a photo goes (labelled "…photo").
To drop in a real image, add it to `assets/img/` and set it on the placeholder, e.g.:

```html
<div class="photo has-img" style="background-image:url('assets/img/hero-truck.jpg')"></div>
```

Add the `has-img` class to hide the placeholder label. Recommended shots: a hero truck,
your fleet, the team/drivers, loading/equipment, and a handshake for the carriers page.

## Make the forms work
The quote and contact forms are real HTML forms with no backend attached yet. Two easy options:
1. **Form service** (no code): sign up at Formspree, Basin, or similar and set the form's
   `action="https://formspree.io/f/XXXX"` (search `action="#"` in `quote.html` / `contact.html`).
2. **Your own endpoint**: point `action` at your handler and process the POST.

The contact/quote pages also list your phone and email as direct fallbacks.

## Customize the look
All colors, fonts, and spacing live as variables at the top of
`assets/css/styles.css` (the `:root` block). Change `--gold`, `--bg`, or the fonts there
and the whole site updates.

## Notes
- Fonts (Oswald + Inter) load from Google Fonts — an internet connection shows them; offline
  falls back to system fonts.
- The Areas map is a stylised coverage graphic. Swap in an embedded map or real US SVG if you prefer.
- Contact/map on `contact.html` has a placeholder — paste a Google Maps embed there.
- `build.py` is the generator that produced these pages; keep it if you want to regenerate,
  or delete it — it isn't needed to run the site.
