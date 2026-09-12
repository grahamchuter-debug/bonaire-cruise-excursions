#!/usr/bin/env python3
"""Sync marketing surface into ./public for Workers Assets (excludes booking engine)."""
from __future__ import annotations

import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PUBLIC = ROOT / "public"

INCLUDE = [
    "index.html",
    "404.html",
    "robots.txt",
    "sitemap.xml",
    "css/site.css",
    "js",
    "images",
    "book",
    "about",
    "contact",
    "privacy",
    "terms",
    "methodology",
    "best-bonaire-shore-excursions",
    "bonaire-cruise-port-guide",
    "bonaire-island-tour",
    "klein-bonaire-snorkeling",
]


def main() -> None:
    if PUBLIC.exists():
        shutil.rmtree(PUBLIC)
    PUBLIC.mkdir(parents=True)

    for rel in INCLUDE:
        src = ROOT / rel
        if not src.exists():
            continue
        dest = PUBLIC / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        if src.is_dir():
            shutil.copytree(src, dest, dirs_exist_ok=True)
        else:
            shutil.copy2(src, dest)

    quarantine = PUBLIC / "images" / "quarantine"
    if quarantine.exists():
        shutil.rmtree(quarantine)

    count = sum(1 for p in PUBLIC.rglob("*") if p.is_file())
    print(f"Synced public/ ({count} files)")


if __name__ == "__main__":
    main()
