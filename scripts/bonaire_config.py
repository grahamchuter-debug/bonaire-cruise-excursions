"""Bonaire Cruise Excursions — World 2.0 Phase 20B site configuration."""
from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

DOMAIN = "bonairecruiseexcursions.com"
APEX = f"https://{DOMAIN}"
SITE = "Bonaire Cruise Excursions"
EMAIL = "hello@bonairecruiseexcursions.com"
DATE = "2026-09-12"
ACCENT = "text-teal-300"

FONTS = (
    "https://fonts.googleapis.com/css2?family=Outfit:wght@400;600;700"
    "&family=Source+Sans+3:wght@400;500;600;700&display=swap"
)

HERO_GRADIENT = (
    "linear-gradient(140deg, rgba(0, 45, 85, 0.84) 0%, "
    "rgba(0, 90, 130, 0.68) 40%, rgba(13, 148, 136, 0.48) 70%, "
    "rgba(0, 0, 0, 0.28) 100%)"
)

# Active images only — see images/ATTRIBUTION.md
FLAMINGO = "/images/flamingo-salt-flat-tour.jpg"
FLAMINGO_ALT = (
    "Caribbean flamingos gathered along a shallow lagoon shoreline on Bonaire"
)

CRUISE_PORT = "/images/cruise-port.jpg"
CRUISE_PORT_ALT = (
    "Cruise ship and harbour boats along the Kralendijk waterfront, Bonaire"
)

SNORKEL = "/images/snorkeling-tour.jpg"
SNORKEL_ALT = (
    "Snorkeler swimming beside a coral reef wall in clear Caribbean water"
)

PROTECTED_ROUTES: list[dict] = [
    {"path": "/", "file": "index.html", "kind": "home"},
    {
        "path": "/bonaire-island-tour",
        "file": "bonaire-island-tour/index.html",
        "kind": "flagship",
    },
    {
        "path": "/klein-bonaire-snorkeling",
        "file": "klein-bonaire-snorkeling/index.html",
        "kind": "attraction",
    },
    {
        "path": "/bonaire-cruise-port-guide",
        "file": "bonaire-cruise-port-guide/index.html",
        "kind": "guide",
    },
    {
        "path": "/best-bonaire-shore-excursions",
        "file": "best-bonaire-shore-excursions/index.html",
        "kind": "hub",
    },
    {"path": "/contact", "file": "contact/index.html", "kind": "trust"},
    {"path": "/about", "file": "about/index.html", "kind": "trust"},
    {"path": "/privacy", "file": "privacy/index.html", "kind": "trust"},
    {"path": "/terms", "file": "terms/index.html", "kind": "trust"},
    {"path": "/methodology", "file": "methodology/index.html", "kind": "trust"},
]
