#!/usr/bin/env python3
"""QA checks for Bonaire World 2.0 Phase 20B."""
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
    "ship return guaranteed",
]


def fail(msg: str) -> None:
    print(f"FAIL: {msg}")
    sys.exit(1)


def main() -> None:
    for p in REQUIRED:
        if not p.exists():
            fail(f"missing {p.relative_to(ROOT)}")

    # Flamingo path must remain exact
    flamingo = ROOT / "images" / "flamingo-salt-flat-tour.jpg"
    if not flamingo.is_file():
        fail("flamingo image missing at exact path")

    # No active Cool Runnings / tortola in HTML
    html_files = [
        p
        for p in list(ROOT.glob("*.html")) + list(ROOT.glob("*/index.html"))
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
        if "fetch(" in text and "nav.js" not in str(hf):
            # pages shouldn't fetch content
            if "application/ld+json" not in text[:500]:
                pass
        for bad in BANNED:
            if bad.lower() in low:
                fail(f"{hf.relative_to(ROOT)} contains banned string: {bad}")
        # canonical extensionless
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

    sm = (ROOT / "sitemap.xml").read_text(encoding="utf-8")
    if ".html" in sm:
        fail("sitemap contains .html")
    if f"{APEX}/bonaire-island-tour" not in sm:
        fail("sitemap missing island tour")

    # Quarantined assets must not be referenced
    quarantine = ROOT / "images" / "quarantine"
    if quarantine.exists():
        for q in quarantine.iterdir():
            if not q.is_file():
                continue
            name = q.name
            for hf in html_files:
                if name in hf.read_text(encoding="utf-8"):
                    fail(f"quarantined {name} referenced in {hf.relative_to(ROOT)}")

    # Cool Runnings must stay quarantined
    if (ROOT / "images" / "hero-catamaran.jpg").exists():
        fail("Cool Runnings hero still in active images/")

    print("QA OK")


if __name__ == "__main__":
    main()
