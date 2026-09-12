#!/usr/bin/env python3
"""Build Bonaire Cruise Excursions World 2.0 static site (Phase 20B)."""
from __future__ import annotations

import json
import shutil
from pathlib import Path

from bonaire_config import APEX, DATE, DOMAIN, PROTECTED_ROUTES, ROOT
from bonaire_pages import all_pages


def write_page(path: str, html: str) -> Path:
    if path in ("/", ""):
        out = ROOT / "index.html"
    elif path == "/404.html":
        out = ROOT / "404.html"
    else:
        slug = path.strip("/")
        out = ROOT / slug / "index.html"
        out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html, encoding="utf-8")
    print(f"  wrote {out.relative_to(ROOT)}")
    return out


def write_robots() -> None:
    text = f"""User-agent: *
Allow: /

Sitemap: {APEX}/sitemap.xml
"""
    (ROOT / "robots.txt").write_text(text, encoding="utf-8")
    print("  wrote robots.txt")


def write_sitemap() -> None:
    entries = [
        ("/", "1.0", "weekly"),
        ("/bonaire-island-tour", "0.95", "weekly"),
        ("/klein-bonaire-snorkeling", "0.9", "weekly"),
        ("/best-bonaire-shore-excursions", "0.85", "weekly"),
        ("/bonaire-cruise-port-guide", "0.85", "monthly"),
        ("/about", "0.4", "yearly"),
        ("/contact", "0.4", "yearly"),
        ("/privacy", "0.3", "yearly"),
        ("/terms", "0.3", "yearly"),
        ("/methodology", "0.4", "yearly"),
    ]
    parts = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
    ]
    for path, priority, freq in entries:
        loc = f"{APEX}/" if path == "/" else f"{APEX}{path}"
        parts.append("  <url>")
        parts.append(f"    <loc>{loc}</loc>")
        parts.append(f"    <lastmod>{DATE}</lastmod>")
        parts.append(f"    <changefreq>{freq}</changefreq>")
        parts.append(f"    <priority>{priority}</priority>")
        parts.append("  </url>")
    parts.append("</urlset>")
    parts.append("")
    (ROOT / "sitemap.xml").write_text("\n".join(parts), encoding="utf-8")
    print("  wrote sitemap.xml")


def write_protected_routes() -> None:
    payload = {
        "domain": DOMAIN,
        "apex": APEX,
        "phase": "20B",
        "routes": PROTECTED_ROUTES,
    }
    (ROOT / "protected_routes.json").write_text(
        json.dumps(payload, indent=2) + "\n", encoding="utf-8"
    )
    print("  wrote protected_routes.json")


def clean_generated_dirs() -> None:
    keep_roots = {
        "css",
        "js",
        "images",
        "scripts",
        "shared",
        "workers",
        "public",
        "node_modules",
        ".git",
        ".wrangler",
        "_legacy_phase20a",
    }
    for child in ROOT.iterdir():
        if child.is_dir() and child.name not in keep_roots and not child.name.startswith("."):
            idx = child / "index.html"
            if idx.exists() or not any(child.iterdir()):
                shutil.rmtree(child)
                print(f"  cleaned {child.name}/")


def main() -> None:
    print("Building Bonaire World 2.0…")
    clean_generated_dirs()
    pages = all_pages()
    for path, html in pages.items():
        write_page(path, html)
    write_robots()
    write_sitemap()
    write_protected_routes()
    print("Done.")


if __name__ == "__main__":
    main()
