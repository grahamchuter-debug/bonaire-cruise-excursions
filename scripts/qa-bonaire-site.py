"""QA checks for Bonaire World 2.0 Phase 20D."""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
APEX = "https://bonairecruiseexcursions.com"

REQUIRED = [
    ROOT / "index.html",
    ROOT / "bonaire-island-tour" / "index.html",
    ROOT / "klein-bonaire-snorkeling" / "index.html",
    ROOT / "bonaire-cruise-port-guide" / "index.html",
    ROOT / "best-bonaire-shore-excursions" / "index.html",
    ROOT / "contact" / "index.html",
    ROOT / "about" / "index.html",
    ROOT / "privacy" / "index.html",
    ROOT / "terms" / "index.html",
    ROOT / "methodology" / "index.html",
    ROOT / "404.html",
    ROOT / "worker.js",
    ROOT / "robots.txt",
    ROOT / "sitemap.xml",
    ROOT / "images" / "flamingo-salt-flat-tour.jpg",
    ROOT / "css" / "site.css",
    ROOT / "js" / "nav.js",
    ROOT / "js" / "commercial-config.js",
    ROOT / "js" / "booking.js",
    ROOT / "js" / "booking-received.js",
    ROOT / "book" / "bonaire-island-sightseeing-tour" / "index.html",
    ROOT / "book" / "bonaire-island-sightseeing-tour" / "received" / "index.html",
]

BANNED = [
    "ship return guaranteed",
    "back on ship, on time",
    "shoreexcursionsgroup",
    "cabosightseeing",
    "wowatour",
    "cdn.tailwindcss.com",
    "Book now",
    "Book a Tour",
    "AggregateRating",
    "SEG_MANUAL",
]

BOOK_CTA = "/book/bonaire-island-sightseeing-tour"


def fail(msg: str) -> None:
    print(f"FAIL: {msg}")
    sys.exit(1)


def main() -> None:
    for p in REQUIRED:
        if not p.exists():
            fail(f"missing {p.relative_to(ROOT)}")

    flamingo = ROOT / "images" / "flamingo-salt-flat-tour.jpg"
    if not flamingo.is_file():
        fail("flamingo image missing at exact path")

    html_files = [
        p
        for p in list(ROOT.glob("*.html"))
        + list(ROOT.glob("*/index.html"))
        + list(ROOT.glob("book/*/index.html"))
        + list(ROOT.glob("book/*/received/index.html"))
        if not any("_legacy" in part for part in p.parts)
        and "node_modules" not in p.parts
    ]
    for hf in html_files:
        text = hf.read_text(encoding="utf-8")
        low = text.lower()
        if text.count("<h1") != 1:
            fail(f"{hf.relative_to(ROOT)} must have exactly one H1")
        if 'id="main-content"' not in text and "id='main-content'" not in text:
            fail(f"{hf.relative_to(ROOT)} missing main-content")
        if "data-content=" in text or "partials/" in text:
            fail(f"{hf.relative_to(ROOT)} still looks like JS shell")
        for bad in BANNED:
            if bad.lower() in low:
                fail(f"{hf.relative_to(ROOT)} contains banned string: {bad}")
        m = re.search(r'rel="canonical" href="([^"]+)"', text)
        if not m:
            fail(f"{hf.relative_to(ROOT)} missing canonical")
        canon = m.group(1)
        if hf.name == "404.html":
            continue
        if ".html" in canon and not canon.endswith("404.html"):
            fail(f"{hf.relative_to(ROOT)} canonical still .html: {canon}")
        if not canon.startswith(APEX):
            fail(f"{hf.relative_to(ROOT)} canonical not apex: {canon}")

    for slug in ("index.html", "bonaire-island-tour/index.html", "best-bonaire-shore-excursions/index.html"):
        text = (ROOT / slug).read_text(encoding="utf-8")
        if BOOK_CTA not in text:
            fail(f"{slug} missing commercial CTA to {BOOK_CTA}")

    cfg = (ROOT / "js" / "commercial-config.js").read_text(encoding="utf-8")
    for bad in ("cabosightseeing", "SEG_MANUAL", "wowatour", "shoreexcursionsgroup"):
        if bad.lower() in cfg.lower():
            fail(f"commercial-config leaks {bad}")
    if "bonaire-bookings-prod" not in cfg:
        fail("commercial-config must point at prod bookings worker")
    if "flamingo-salt-flat-tour.jpg" in cfg:
        fail("commercial UI must not auto-use flamingo image")

    sm = (ROOT / "sitemap.xml").read_text(encoding="utf-8")
    if ".html" in sm:
        fail("sitemap contains .html")
    if f"{APEX}/bonaire-island-tour" not in sm:
        fail("sitemap missing island tour")
    if "book/" in sm:
        fail("sitemap must not list noindex book routes")

    quarantine = ROOT / "images" / "quarantine"
    if quarantine.exists():
        for q in quarantine.iterdir():
            if not q.is_file():
                continue
            name = q.name
            for hf in html_files:
                if name in hf.read_text(encoding="utf-8"):
                    fail(f"quarantined {name} referenced in {hf.relative_to(ROOT)}")

    if (ROOT / "images" / "hero-catamaran.jpg").exists():
        fail("Cool Runnings hero still in active images/")

    print("QA OK")


if __name__ == "__main__":
    main()
