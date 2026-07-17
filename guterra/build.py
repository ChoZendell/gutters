#!/usr/bin/env python3
"""Assemble the Guterra site: shared chrome + per-page <main> content."""
import os, pathlib

OUT = pathlib.Path(__file__).parent
PHONE = "(909) 309-0323"
PHONE_HREF = "tel:+19093090323"
EMAIL = "dispatch@guterrabrokersystem.com"
ADDRESS = "5143 Rio Bravo Drive, Banning, CA 92220"

def ic(name, cls="ic"):
    return f'<svg class="{cls}" aria-hidden="true"><use href="assets/img/icons.svg#i-{name}"></use></svg>'

# ---------------------------------------------------------------- nav model
WHO = [("about.html","About Us"),("industries.html","Industries We Serve"),("areas.html","Areas We Serve")]
SERVICES = [("services.html","All Services"),("services-dry-van.html","Dry Van"),
            ("services-flatbed.html","Flatbed & Heavy Haul"),("services-ltl.html","LTL & Partial Loads"),
            ("services-expedited.html","Expedited Delivery"),("services-refrigerated.html","Refrigerated Transport")]

def header(active):
    def cur(f): return ' aria-current="page"' if f == active else ''
    def sub(items):
        return "".join(f'<a href="{f}"{cur(f)}>{t}</a>' for f, t in items)
    who_open = 'aria-current="page"' if active in [f for f,_ in WHO] else ''
    svc_open = 'aria-current="page"' if active in [f for f,_ in SERVICES] else ''
    return f'''  <div class="topbar">
    <div class="wrap topbar__inner">
      <a href="{PHONE_HREF}">{ic("phone","")}<span>{PHONE}</span></a>
      <a href="mailto:{EMAIL}">{ic("mail","")}<span>{EMAIL}</span></a>
    </div>
  </div>
  <header class="site-header">
    <nav class="wrap nav" aria-label="Primary">
      <a class="brand" href="index.html"><span class="brand__mark">G</span>GU<b>TERRA</b></a>
      <button class="nav__toggle" aria-label="Toggle menu" aria-expanded="false" aria-controls="menu">
        <span></span><span></span><span></span>
      </button>
      <ul class="nav__links" id="menu">
        <li><a href="index.html"{cur("index.html")}>Home</a></li>
        <li class="has-sub"><a href="about.html" {who_open}>Who We Are</a><div class="subnav">{sub(WHO)}</div></li>
        <li class="has-sub"><a href="services.html" {svc_open}>Services</a><div class="subnav">{sub(SERVICES)}</div></li>
        <li><a href="carriers.html"{cur("carriers.html")}>Carriers</a></li>
        <li><a href="careers.html"{cur("careers.html")}>Careers</a></li>
        <li><a href="contact.html"{cur("contact.html")}>Contact</a></li>
        <li class="nav__cta"><a class="btn" href="quote.html">Request a Quote</a></li>
      </ul>
    </nav>
  </header>'''

def footer():
    return f'''  <footer class="site-footer">
    <div class="wrap">
      <div class="footer-grid">
        <div class="footer-about">
          <a class="brand" href="index.html"><span class="brand__mark">G</span>GU<b>TERRA</b></a>
          <p>Full-service transport &amp; emergency expedite. Reliable freight solutions delivered with confidence, nationwide.</p>
        </div>
        <div>
          <h4>Company</h4>
          <a href="about.html">About Us</a><br><a href="industries.html">Industries Served</a><br>
          <a href="areas.html">Areas Served</a><br><a href="careers.html">Careers</a><br>
          <a href="carriers.html">Carrier Setup</a>
        </div>
        <div>
          <h4>Services</h4>
          <a href="services-dry-van.html">Dry Van</a><br><a href="services-flatbed.html">Flatbed &amp; Heavy Haul</a><br>
          <a href="services-ltl.html">LTL &amp; Partial</a><br><a href="services-expedited.html">Expedited</a><br>
          <a href="services-refrigerated.html">Refrigerated</a>
        </div>
        <div>
          <h4>Get in Touch</h4>
          <a href="{PHONE_HREF}">{PHONE}</a><br>
          <a href="mailto:{EMAIL}">{EMAIL}</a><br>
          <span style="color:var(--muted);font-size:.9rem;line-height:1.7;display:inline-block;margin-top:.2rem">{ADDRESS}</span><br>
          <a class="btn btn--ghost" style="margin-top:1rem" href="quote.html">Request a Quote {ic("arrow","")}</a>
        </div>
      </div>
      <div class="footer-bottom">
        <span>&copy; 2026 Guterra Broker System. All rights reserved.</span>
        <span><a href="legal.html">Privacy Policy</a> &nbsp;·&nbsp; <a href="legal.html#terms">Terms &amp; Conditions</a></span>
      </div>
    </div>
  </footer>'''

def page(filename, title, desc, active, main):
    html = f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title} — Guterra Broker System</title>
  <meta name="description" content="{desc}">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Oswald:wght@400;500;600;700&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="assets/css/styles.css">
</head>
<body>
{header(active)}
  <main id="main">
{main}
  </main>
{footer()}
  <script src="assets/js/main.js"></script>
</body>
</html>'''
    (OUT / filename).write_text(html, encoding="utf-8")
    print("wrote", filename)

# ============================================================ shared blocks
def banner(eyebrow, title, lead, crumb):
    return f'''    <section class="banner">
      <div class="wrap">
        <p class="breadcrumb"><a href="index.html">Home</a> / {crumb}</p>
        <p class="eyebrow" style="margin-top:1rem">{eyebrow}</p>
        <h1 class="display">{title}</h1>
        <p class="lead">{lead}</p>
      </div>
    </section>'''

def cta_band(title, sub, btn_text, btn_href):
    return f'''    <section class="cta-band">
      <div class="wrap">
        <div><h2>{title}</h2><p>{sub}</p></div>
        <a class="btn" href="{btn_href}">{btn_text} {ic("arrow","")}</a>
      </div>
    </section>'''

# service data: (file, name, subtitle, lead, group_label, pills[(icon,label)], features[], tagline_a, tagline_b, icon)
SERVICE_PAGES = [
 ("services-dry-van.html","Dry Van Services","Versatile and secure dry van solutions for your freight.",
  "Enclosed, weather-protected trailers for general freight of nearly every kind — moved on time, every time, across the country.",
  "Ideal For",[("box","General Freight"),("layers","Consumer Goods"),("store","Retail Products"),("truck","And More")],
  ["Secure, enclosed trailers","Multiple trailer sizes available","On-time pickup &amp; delivery","Nationwide coverage"],
  "Safe. Secure. On Time.","Every Time.","truck"),
 ("services-flatbed.html","Flatbed &amp; Heavy Haul","Reliable flatbed solutions for oversized and heavy equipment.",
  "Step-deck, flatbed and specialized trailers with the permits, planning and drivers to move your heaviest, most awkward loads.",
  "We Handle",[("gear","Machinery"),("layers","Steel &amp; Metal"),("hardhat","Construction Materials"),("wrench","Large Equipment")],
  ["Step deck, flatbed &amp; specialized trailers","Permits &amp; route planning","Experienced heavy-haul drivers","Nationwide heavy-haul expertise"],
  "Built for Heavy Loads.","Driven by Experts.","flatbed"),
 ("services-ltl.html","LTL &amp; Partial Loads","Cost-effective shipping for smaller, shared loads.",
  "When you don't need a full trailer, our LTL and partial network gets your freight there affordably — without sacrificing reliability.",
  "Ideal For",[("box","Small Shipments"),("layers","Fewer Pallets"),("dollar","Cost Savings"),("gear","Flexible Options")],
  ["Competitive pricing","Nationwide LTL network","Reliable transit times","Real-time tracking"],
  "Right Size. Right Price.","Right on Time.","layers"),
 ("services-expedited.html","Expedited Delivery","Time-critical freight delivered fast and safely.",
  "When the clock is the constraint, our expedite team dispatches dedicated capacity and keeps you updated until it's delivered.",
  "When You Need It",[("bolt","Urgent Shipments"),("clock","Time-Sensitive"),("shield","Emergency Freight"),("star","Critical Deliveries")],
  ["Fast pickup &amp; delivery","Dedicated transportation","24/7 support","Real-time updates"],
  "When Time Matters,","We Deliver.","bolt"),
 ("services-refrigerated.html","Refrigerated Transport","Temperature-controlled solutions that protect your products.",
  "Reefer capacity with continuous monitoring and multi-temperature options to keep perishable and sensitive freight in spec, end to end.",
  "Ideal For",[("box","Food &amp; Beverages"),("shield","Pharmaceuticals"),("snow","Frozen Goods"),("tractor","Produce")],
  ["Temperature-controlled trailers","Multi-temperature options","Continuous monitoring","Food-safety compliant"],
  "Keeping It Cool.","Keeping It Safe.","thermo"),
]

def features_list(items):
    return "".join(f'<li><span class="tick">{ic("check","")}</span><span>{t}</span></li>' for t in items)

def pills(items):
    return "".join(f'<div class="pill">{ic(i)}<span>{t}</span></div>' for i, t in items)

# ================================================================= HOME
home_services = ""
SVC_CARDS = [
 ("services-dry-van.html","truck","Dry Van","Versatile and secure dry van solutions for your general freight."),
 ("services-flatbed.html","flatbed","Flatbed","Flatbed &amp; heavy haul for oversized and heavy loads."),
 ("services-ltl.html","layers","LTL &amp; Partial","Cost-effective shipping for smaller, shared shipments."),
 ("services-expedited.html","bolt","Expedited","Time-critical freight delivered fast and safely."),
 ("services-refrigerated.html","thermo","Refrigerated","Temperature-controlled solutions that protect your products."),
]
for f,i,t,d in SVC_CARDS:
    home_services += f'''<a class="card reveal" href="{f}">
        <div class="card__media photo" data-label="{t} photo"></div>
        <div class="card__body">{ic(i)}<h3>{t}</h3><p>{d}</p>
          <span class="card__link">Learn more {ic("arrow","")}</span></div></a>'''

FEATURES = [
 ("clock","On-Time Delivery","Punctual, reliable, every time."),
 ("users","Customer Dedicated","Your success is our priority."),
 ("warehouse","Warehousing","Secure storage and inventory solutions."),
 ("shield","Quality Transport","Safe, secure and compliant hauling."),
 ("gear","Equipment Versatility","The right equipment for every load."),
 ("headset","24/7 Customer Care","We're here when you need us."),
]
feature_strip = "".join(f'<div class="feature reveal">{ic(i)}<h4>{t}</h4><p>{d}</p></div>' for i,t,d in FEATURES)

WHY = ["Experienced logistics professionals","Nationwide carrier network",
       "Real-time tracking &amp; communication","Flexible solutions for every industry",
       "Commitment to safety &amp; compliance"]

home_main = f'''    <section class="hero">
      <div class="wrap hero__inner">
        <p class="eyebrow">Full-Service Transport &amp; Emergency Expedite</p>
        <h1 class="display">Reliable Freight<br>Solutions.<br><span class="gold">Delivered</span> With Confidence.</h1>
        <p class="lead">Entrust us as your full-service transport and emergency expedite partner — moving your freight safely, on time, across all 48 states.</p>
        <div class="hero__actions">
          <a class="btn" href="quote.html">Request a Quote {ic("arrow","")}</a>
          <a class="btn btn--ghost" href="services.html">Explore Services</a>
        </div>
      </div>
    </section>

    <section class="feature-strip">
      <div class="wrap"><div class="grid">{feature_strip}</div></div>
    </section>

    <section class="section">
      <div class="wrap">
        <div class="center stack">
          <p class="eyebrow">Our Services</p>
          <h2 class="h-xl">Comprehensive Transportation Solutions</h2>
          <p class="lead">From dry van to reefer, we match the right equipment to every shipment.</p>
        </div>
        <div class="grid cards mt-l">{home_services}</div>
      </div>
    </section>

    <section class="section section--alt">
      <div class="wrap split split--wide-text">
        <div class="stack">
          <p class="eyebrow">About Guterra Broker System</p>
          <h2 class="h-xl">Why Shippers &amp; Carriers Choose Guterra</h2>
          <p class="lead">We combine dependable, experienced logistics with a dedicated team focused on delivering excellence — and tailored transportation solutions across the nation.</p>
          <ul class="checklist mt-s">{features_list(WHY)}</ul>
          <div class="mt-s"><a class="btn" href="about.html">More About Us {ic("arrow","")}</a></div>
        </div>
        <div class="photo" data-label="Guterra fleet photo" style="min-height:360px"></div>
      </div>
    </section>

{cta_band("Ready to move your freight?","Get a fast, competitive quote from our team today.","Request a Quote","quote.html")}'''

page("index.html","Reliable Freight Solutions","Guterra Broker System — full-service transport and emergency expedite. Reliable freight solutions delivered with confidence, nationwide.","index.html",home_main)

# ================================================================= ABOUT
ABOUT_POINTS = ["Dedicated logistics experts","Advanced technology","Nationwide coverage","Customer-first approach"]
VALUES = [("shield","Integrity","We do the right thing, always."),
          ("check","Reliability","You can count on us to deliver."),
          ("users","Safety","Protecting our people, your freight, and the road."),
          ("hands","Teamwork","Stronger together, for your success.")]
ABOUT_STATS = [("10+","Years of Experience"),("5K+","Satisfied Customers"),("25K+","Loads Delivered"),("48","States Served")]
values_html = "".join(f'<div class="tile reveal">{ic(i)}<h3>{t}</h3><p>{d}</p></div>' for i,t,d in VALUES)
about_stats = "".join(f'<div class="stat"><b>{n}</b><span>{l}</span></div>' for n,l in ABOUT_STATS)

about_main = f'''{banner("About Guterra Broker System","Driven by Integrity.<br>Focused on Results.","We combine experienced logistics professionals with technology and a customer-first approach to move your business forward.","Who We Are")}

    <section class="section">
      <div class="wrap split">
        <div class="photo" data-label="Team / operations photo" style="min-height:380px"></div>
        <div class="stack">
          <p class="eyebrow">Who We Are</p>
          <h2 class="h-lg">More Than a Transportation Provider</h2>
          <p class="lead">At Guterra Broker System, we're more than a transportation provider. With years of industry experience, a vast carrier network, and a commitment to excellence, we deliver solutions that keep your business moving.</p>
          <ul class="checklist mt-s">{features_list(ABOUT_POINTS)}</ul>
        </div>
      </div>
    </section>

    <section class="section section--alt">
      <div class="wrap center stack">
        <p class="eyebrow">Our Mission</p>
        <h2 class="h-lg" style="max-width:22ch;margin-inline:auto">To deliver dependable, efficient, and innovative transportation solutions that exceed our customers' expectations.</h2>
      </div>
    </section>

    <section class="section">
      <div class="wrap">
        <div class="center stack"><p class="eyebrow">Our Values</p><h2 class="h-xl">What We Stand For</h2></div>
        <div class="grid cards mt-l">{values_html}</div>
      </div>
    </section>

    <section class="section section--tight section--alt">
      <div class="wrap"><div class="stats">{about_stats}</div></div>
    </section>

{cta_band("Let's build something reliable.","Partner with a broker that puts results first.","Contact Us","contact.html")}'''

page("about.html","About Us","Driven by integrity, focused on results. Learn about Guterra Broker System's mission, values, and nationwide logistics expertise.","about.html",about_main)

# ================================================================= INDUSTRIES
INDUSTRIES = [
 ("hardhat","Construction","We haul the materials and equipment that build our future."),
 ("box","Packaging &amp; Distribution","Reliable freight solutions for your supply chain."),
 ("wrench","Equipment","Safe transport for heavy machinery and equipment."),
 ("tractor","Agriculture","Moving America's harvest with care and speed."),
 ("factory","Manufacturing","Support for manufacturers with on-time deliveries."),
 ("store","Retail","Efficient transport to keep shelves stocked."),
]
ind_html = "".join(f'<div class="tile reveal">{ic(i)}<h3>{t}</h3><p>{d}</p></div>' for i,t,d in INDUSTRIES)
industries_main = f'''{banner("Industries We Serve","Industries We Serve","Tailored transport solutions for the industries that keep America moving.","Industries")}

    <section class="section">
      <div class="wrap"><div class="grid cards">{ind_html}</div></div>
    </section>

    <section class="section section--alt">
      <div class="wrap center stack">
        <h2 class="h-xl" style="max-width:20ch;margin-inline:auto">No matter the industry, we deliver with reliability and care.</h2>
        <div class="mt-s"><a class="btn" href="quote.html">Request a Quote {ic("arrow","")}</a></div>
      </div>
    </section>'''
page("industries.html","Industries We Serve","Guterra provides tailored transport for construction, agriculture, manufacturing, retail, equipment, and distribution.","industries.html",industries_main)

# ================================================================= AREAS
AREA_POINTS = [("badge","48 States Covered"),("pin","Regional &amp; Local Expertise"),
               ("truck","Fast &amp; Reliable Delivery"),("headset","24/7 Support")]
AREA_STATS = [("48","States"),("250+","Carrier Partners"),("99%","On-Time Delivery"),("24/7","Support")]
area_points = "".join(f'<li><span class="tick">{ic(i,"")}</span><span><b>{t}</b></span></li>' for i,t in AREA_POINTS)
area_stats = "".join(f'<div class="stat"><b>{n}</b><span>{l}</span></div>' for n,l in AREA_STATS)

# simple stylised US map with pins
pins = [(140,120),(200,90),(260,140),(320,110),(390,95),(450,130),(510,120),(560,100),
        (170,200),(240,180),(300,210),(360,190),(430,175),(490,205),(540,180),
        (200,260),(280,250),(350,270),(420,255),(480,270),(150,160),(600,150)]
pin_svg = "".join(f'<circle class="pin{" big" if k%5==0 else ""}" cx="{x}" cy="{y}" r="{5 if k%5==0 else 3.5}"/>' for k,(x,y) in enumerate(pins))
usmap = f'''<svg class="usmap" viewBox="0 0 640 340" role="img" aria-label="United States coverage map">
  <path class="land" d="M60 150 L120 80 L210 60 L340 55 L470 65 L560 60 L610 90 L620 150 L600 210 L560 250 L470 285 L360 300 L250 295 L160 270 L100 230 L70 195 Z"/>
  {pin_svg}
</svg>'''

areas_main = f'''{banner("Areas We Serve","Areas We Serve","Nationwide coverage. Local expertise. From coast to coast, Guterra delivers reliable freight solutions across all 48 contiguous states.","Areas")}

    <section class="section">
      <div class="wrap split">
        <div class="photo" data-label="" style="padding:1.5rem;display:grid;place-items:center;background:var(--surface)">{usmap}</div>
        <div class="stack">
          <p class="eyebrow">Coast to Coast</p>
          <h2 class="h-lg">Wherever Your Freight Needs to Go</h2>
          <p class="lead">Guterra Broker System provides reliable freight solutions across the nation, combining nationwide reach with regional know-how.</p>
          <ul class="checklist mt-s">{area_points}</ul>
        </div>
      </div>
    </section>

    <section class="section section--tight section--alt">
      <div class="wrap"><div class="stats">{area_stats}</div></div>
    </section>

    <section class="section">
      <div class="wrap center stack">
        <h2 class="h-xl">Wherever you need to go, <span class="gold">we'll get your freight there.</span></h2>
        <div class="mt-s"><a class="btn" href="quote.html">Request a Quote {ic("arrow","")}</a></div>
      </div>
    </section>'''
page("areas.html","Areas We Serve","Nationwide coverage with local expertise across all 48 states. Guterra delivers your freight coast to coast.","areas.html",areas_main)

# ================================================================= SERVICES OVERVIEW
SVC_OVERVIEW = [
 ("services-dry-van.html","truck","Dry Van","Versatile and secure dry van solutions."),
 ("services-flatbed.html","flatbed","Flatbed &amp; Heavy Haul","Reliable transport for oversized and heavy loads."),
 ("services-ltl.html","layers","LTL &amp; Partial Loads","Cost-effective shipping for smaller, shared shipments."),
 ("services-expedited.html","bolt","Expedited Delivery","Time-critical freight delivered fast and safely."),
 ("services-refrigerated.html","thermo","Refrigerated Transport","Temperature-controlled solutions that protect your products."),
]
svc_rows = ""
for f,i,t,d in SVC_OVERVIEW:
    svc_rows += f'''<a class="card reveal" href="{f}">
      <div class="card__body" style="flex-direction:row;align-items:center;gap:1.1rem">
        <span style="flex:none;width:52px;height:52px;border-radius:6px;background:rgba(245,179,1,.12);display:grid;place-items:center">{ic(i)}</span>
        <span style="flex:1"><h3 style="font-size:1.1rem">{t}</h3><p style="margin-top:.2rem">{d}</p></span>
        {ic("arrow")}
      </div></a>'''
services_main = f'''{banner("Our Services","Our Services","Comprehensive transportation solutions designed to meet your unique shipping needs.","Services")}

    <section class="section">
      <div class="wrap split split--wide-text">
        <div class="grid" style="gap:1rem">{svc_rows}</div>
        <div class="photo" data-label="Fleet on the road" style="min-height:420px"></div>
      </div>
    </section>

    <section class="section section--alt">
      <div class="wrap center stack">
        <h2 class="h-xl">Safe. Secure. On Time. <span class="gold">Every Time.</span></h2>
        <div class="mt-s"><a class="btn" href="quote.html">Request a Quote {ic("arrow","")}</a></div>
      </div>
    </section>'''
page("services.html","Our Services","Dry van, flatbed, LTL, expedited, and refrigerated transport — comprehensive freight solutions from Guterra Broker System.","services.html",services_main)

# ================================================================= SERVICE DETAILS
for f,name,subtitle,lead,group,pill_items,feats,ta,tb,icon in SERVICE_PAGES:
    _eyebrow = "Services / " + name.replace("&amp;", "&")
    _crumb = '<a href="services.html">Services</a> / ' + name
    m = f'''{banner(_eyebrow, name, lead, _crumb)}

    <section class="section">
      <div class="wrap split">
        <div class="photo" data-label="{name.replace("&amp;","&")} photo" style="min-height:360px"></div>
        <div class="stack">
          <p class="eyebrow">{group}</p>
          <h2 class="h-lg">{subtitle}</h2>
          <div class="pills mt-s">{pills(pill_items)}</div>
        </div>
      </div>
    </section>

    <section class="section section--alt">
      <div class="wrap split split--wide-text">
        <div class="stack">
          <p class="eyebrow">Features &amp; Benefits</p>
          <h2 class="h-lg">Why Choose This Service</h2>
          <ul class="checklist mt-s">{features_list(feats)}</ul>
          <div class="mt-s"><a class="btn" href="quote.html">Request a Quote {ic("arrow","")}</a></div>
        </div>
        <div class="photo" data-label="Loading / equipment photo" style="min-height:320px"></div>
      </div>
    </section>

    <section class="section section--tight">
      <div class="wrap center">
        <h2 class="h-xl">{ta} <span class="gold">{tb}</span></h2>
      </div>
    </section>'''
    page(f, name.replace("&amp;","&"), f"{subtitle} Guterra Broker System — {name.replace('&amp;','and')}.", f, m)

# ================================================================= CAREERS
CAREER_PERKS = [("dollar","Competitive Pay","Rewarding compensation for driven people."),
                ("heart","Great Benefits","Support for you and your family."),
                ("chart","Growth Opportunities","Room to build a real career."),
                ("users","Supportive Team","Work alongside people who have your back.")]
perks = "".join(f'<div class="tile reveal">{ic(i)}<h3>{t}</h3><p>{d}</p></div>' for i,t,d in CAREER_PERKS)
careers_main = f'''{banner("Join Our Team","Join Our Team","We're always looking for driven individuals to join our growing team.","Careers")}

    <section class="section">
      <div class="wrap split">
        <div class="stack">
          <p class="eyebrow">Why Work With Us</p>
          <h2 class="h-lg">Drive Your Career Forward</h2>
          <p class="lead">At Guterra, our people are the engine behind every on-time delivery. If you take pride in your work and want to grow, we'd like to meet you.</p>
        </div>
        <div class="photo" data-label="Driver / team photo" style="min-height:340px"></div>
      </div>
      <div class="wrap"><div class="grid cards mt-l">{perks}</div></div>
    </section>

{cta_band("Drive Your Career Forward","Apply today and be part of the Guterra team.","Apply Now","contact.html")}'''
page("careers.html","Join Our Team","Competitive pay, great benefits, and growth. Join the Guterra Broker System team and drive your career forward.","careers.html",careers_main)

# ================================================================= CARRIERS
CARRIER_REQ = ["Active MC Authority","Valid Insurance","Safe Driving Record","Reliable Equipment"]
CARRIER_WHY = [("clock","Fast Response","Quick load offers and dispatch."),
               ("dollar","Competitive Rates","Fair, transparent pay."),
               ("shield","Reliable Service","A partner you can count on."),
               ("headset","24/7 Support","Help whenever you need it.")]
cwhy = "".join(f'<div class="tile reveal">{ic(i)}<h3>{t}</h3><p>{d}</p></div>' for i,t,d in CARRIER_WHY)
carriers_main = f'''{banner("Carrier Setup","Carrier Setup","Partner with Guterra Broker System and grow your business.","Carriers")}

    <section class="section">
      <div class="wrap split">
        <div class="stack">
          <p class="eyebrow">Become a Carrier</p>
          <h2 class="h-lg">Requirements to Get Started</h2>
          <p class="lead">Joining our network is straightforward. Meet the requirements below and our team will help you get set up quickly.</p>
          <ul class="checklist mt-s">{features_list(CARRIER_REQ)}</ul>
          <div class="mt-s"><a class="btn" href="contact.html">Become a Carrier {ic("arrow","")}</a></div>
        </div>
        <div class="photo" data-label="Handshake / partnership photo" style="min-height:360px"></div>
      </div>
    </section>

    <section class="section section--alt">
      <div class="wrap">
        <div class="center stack"><p class="eyebrow">Why Partner With Us</p><h2 class="h-xl">Let's Build a Strong Partnership</h2></div>
        <div class="grid cards mt-l">{cwhy}</div>
      </div>
    </section>

{cta_band("Ready to haul with Guterra?","Get set up in our carrier network today.","Get Started","contact.html")}'''
page("carriers.html","Carrier Setup","Partner with Guterra Broker System. Active MC authority, valid insurance, and reliable equipment get you started fast.","carriers.html",carriers_main)

# ================================================================= QUOTE
QUOTE_WHY = [("clock","Fast Response"),("dollar","Competitive Rates"),("shield","Reliable Service"),("headset","24/7 Support")]
qwhy = "".join(f'<li><span class="tick">{ic(i,"")}</span><span><b>{t}</b></span></li>' for i,t in QUOTE_WHY)
EQUIP = ["Dry Van","Flatbed","Step Deck","Reefer / Refrigerated","LTL / Partial","Expedited","Not sure — help me choose"]
equip_opts = "".join(f"<option>{e}</option>" for e in EQUIP)
quote_main = f'''{banner("Request a Quote","Request a Quote","Tell us about your shipment and we'll handle the rest — with a fast, competitive response.","Request a Quote")}

    <section class="section">
      <div class="wrap split split--wide-text">
        <form class="form" action="#" method="post" novalidate>
          <div class="row cols-2">
            <div class="field"><label>Full Name <span class="req">*</span></label><input name="name" placeholder="John Smith" required></div>
            <div class="field"><label>Company Name</label><input name="company" placeholder="Company LLC"></div>
          </div>
          <div class="row cols-2">
            <div class="field"><label>Email Address <span class="req">*</span></label><input type="email" name="email" placeholder="you@company.com" required></div>
            <div class="field"><label>Phone Number <span class="req">*</span></label><input type="tel" name="phone" placeholder="{PHONE}" required></div>
          </div>
          <div class="row cols-2">
            <div class="field"><label>Pickup Location <span class="req">*</span></label><input name="pickup" placeholder="City, State" required></div>
            <div class="field"><label>Delivery Location <span class="req">*</span></label><input name="delivery" placeholder="City, State" required></div>
          </div>
          <div class="row cols-2">
            <div class="field"><label>Commodity</label><input name="commodity" placeholder="What are you shipping?"></div>
            <div class="field"><label>Equipment</label><select name="equipment">{equip_opts}</select></div>
          </div>
          <div class="field"><label>Weight (lbs)</label><input name="weight" placeholder="e.g. 12,000"></div>
          <div class="field"><label>Additional Details</label><textarea name="details" placeholder="Dimensions, timing, special requirements…"></textarea></div>
          <div class="field file"><label>Attach Files</label><input type="file" name="files" multiple></div>
          <button class="btn" type="submit">Submit Request {ic("arrow","")}</button>
          <p class="form__note">Our team will review your request and get back to you shortly.</p>
        </form>
        <aside>
          <div class="tile" style="border-left-width:4px">
            <p class="eyebrow">Why Request From Us</p>
            <ul class="checklist mt-s">{qwhy}</ul>
            <hr style="border:none;border-top:1px solid var(--line);margin:1.4rem 0">
            <p style="color:var(--muted);font-size:.92rem">Prefer to talk? Call <a class="gold" href="{PHONE_HREF}">{PHONE}</a> or email <a class="gold" href="mailto:{EMAIL}">{EMAIL}</a>.</p>
          </div>
        </aside>
      </div>
    </section>'''
page("quote.html","Request a Quote","Get a fast, competitive freight quote from Guterra Broker System. Tell us about your shipment and we'll handle the rest.","quote.html",quote_main)

# ================================================================= CONTACT
INFO = [("phone","Phone",f'<a href="{PHONE_HREF}">{PHONE}</a>'),
        ("mail","Email",f'<a href="mailto:{EMAIL}">{EMAIL}</a>'),
        ("pin","Address",f'<span>{ADDRESS}</span>'),
        ("clock","Hours","<span>Mon–Fri: 7:00 AM – 6:00 PM<br>Sat: 8:00 AM – 2:00 PM</span>")]
info_html = "".join(f'<li><span class="ic">{ic(i,"")}</span><div><b>{t}</b>{v}</div></li>' for i,t,v in INFO)
contact_main = f'''{banner("Contact Us","We're Here to Help.","Get in touch with the Guterra team — for quotes, carrier setup, or anything else.","Contact")}

    <section class="section">
      <div class="wrap split">
        <div class="stack">
          <p class="eyebrow">Get in Touch</p>
          <h2 class="h-lg">Reach the Guterra Team</h2>
          <ul class="info-list mt-m">{info_html}</ul>
        </div>
        <form class="form" action="#" method="post" novalidate>
          <div class="row cols-2">
            <div class="field"><label>Full Name <span class="req">*</span></label><input name="name" placeholder="John Smith" required></div>
            <div class="field"><label>Email Address <span class="req">*</span></label><input type="email" name="email" placeholder="you@company.com" required></div>
          </div>
          <div class="row cols-2">
            <div class="field"><label>Phone Number</label><input type="tel" name="phone" placeholder="{PHONE}"></div>
            <div class="field"><label>Subject</label><input name="subject" placeholder="How can we help?"></div>
          </div>
          <div class="field"><label>Message <span class="req">*</span></label><textarea name="message" placeholder="Tell us what you need…" required></textarea></div>
          <button class="btn" type="submit">Send Message {ic("arrow","")}</button>
          <p class="form__note">We typically respond within one business day.</p>
        </form>
      </div>
      <div class="wrap mt-l">
        <div class="map" data-label="Map">Map — Banning, CA · embed Google Maps here</div>
      </div>
    </section>'''
page("contact.html","Contact Us","Contact Guterra Broker System. Call (909) 309-0323, email dispatch@guterrabrokersystem.com, or send us a message.","contact.html",contact_main)

# ================================================================= LEGAL
legal_main = f'''{banner("Privacy &amp; Terms","Privacy &amp; Terms","How we handle your information, and the terms that govern use of our services.","Legal")}

    <section class="section">
      <div class="wrap legal">
        <div>
          <h2 id="privacy">Privacy Policy</h2>
          <p>At Guterra Broker System, we value your privacy. This notice describes how we collect and use your information.</p>
          <h3>Information We Collect</h3>
          <p>We may collect the information you provide directly — such as your name, contact details, company, and shipment details — when you request a quote, contact us, or apply to our carrier network.</p>
          <h3>How We Use Information</h3>
          <p>We use your information to respond to inquiries, provide quotes, coordinate transportation, and improve our services. We do not sell your personal information.</p>
          <h3>Data Security</h3>
          <p>We take reasonable measures to protect your information from unauthorized access, disclosure, or misuse.</p>
          <h3>Contact Us</h3>
          <p>If you have questions about this policy, contact us at <a class="gold" href="mailto:{EMAIL}">{EMAIL}</a>.</p>
        </div>
        <div>
          <h2 id="terms">Terms &amp; Conditions</h2>
          <p>By using our website and services, you agree to the following terms and conditions.</p>
          <h3>Use of Services</h3>
          <p>Our services are provided for lawful freight and logistics purposes. You agree to provide accurate shipment information and to use our services responsibly.</p>
          <h3>Responsibilities</h3>
          <p>Guterra coordinates transportation between shippers and carriers. Responsibilities for freight, insurance, and delivery are governed by the applicable transportation agreements.</p>
          <h3>Limitation of Liability</h3>
          <p>To the extent permitted by law, Guterra is not liable for indirect or consequential damages arising from the use of our services.</p>
          <h3>Changes to Terms</h3>
          <p>We may update these terms from time to time. Continued use of our services constitutes acceptance of any changes.</p>
        </div>
      </div>
    </section>'''
page("legal.html","Privacy & Terms","Guterra Broker System privacy policy and terms & conditions.","legal.html",legal_main)

# ================================================================= 404
error_main = f'''    <section class="error-hero hero">
      <div class="wrap center stack" style="position:relative;z-index:1">
        <p class="code">4<span>0</span>4</p>
        <h1 class="h-xl">Page Not Found</h1>
        <p class="lead" style="margin-inline:auto">The page you're looking for doesn't exist or has been moved.</p>
        <div class="mt-s" style="display:flex;gap:.8rem;justify-content:center;flex-wrap:wrap">
          <a class="btn" href="index.html">Go Back Home {ic("arrow","")}</a>
          <a class="btn btn--ghost" href="contact.html">Contact Us</a>
        </div>
      </div>
    </section>'''
page("404.html","404 — Page Not Found","The page you're looking for doesn't exist or has been moved.","","404.html".replace("404.html",""))
# fix: 404 shouldn't highlight a nav item
page("404.html","404 — Page Not Found","The page you're looking for doesn't exist or has been moved.","",error_main)

print("\\nDONE — all pages generated.")
