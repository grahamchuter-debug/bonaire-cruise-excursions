/**
 * Bonaire Cruise Excursions — Workers Assets entry (Phase 20B).
 * Canonical: apex HTTPS, extensionless, no trailing slash.
 * .html → extensionless; trailing slash → drop; query preserved.
 * Real 404 — never soft-home.
 * www is NXDOMAIN today — www handling kept for future safety only.
 */
const APEX_HOST = 'bonairecruiseexcursions.com';

const LEGACY_REDIRECTS = {
  '/index': '/',
  '/index.html': '/',
  '/contact.html': '/contact',
  '/about.html': '/about',
  '/privacy.html': '/privacy',
  '/terms.html': '/terms',
  '/methodology.html': '/methodology',
  '/best-bonaire-shore-excursions.html': '/best-bonaire-shore-excursions',
  '/bonaire-cruise-port-guide.html': '/bonaire-cruise-port-guide',
  '/bonaire-island-tour.html': '/bonaire-island-tour',
  '/klein-bonaire-snorkeling.html': '/klein-bonaire-snorkeling',
};

function toCanonicalPath(pathname) {
  let path = pathname || '/';
  if (path.toLowerCase().endsWith('.html')) {
    path = path.slice(0, -5);
    if (path.toLowerCase().endsWith('/index')) path = path.slice(0, -6);
    if (path === '' || path === '/index') path = '/';
  }
  if (path.length > 1 && path.endsWith('/')) {
    path = path.replace(/\/+$/, '') || '/';
  }
  return path || '/';
}

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    const host = url.hostname.toLowerCase();
    const isWww = host === `www.${APEX_HOST}`;
    const isHttp = url.protocol === 'http:';
    const rawPath = url.pathname || '/';
    const rawLower = rawPath.toLowerCase();
    const hasHtml = rawLower.endsWith('.html');
    const hasTrail =
      rawPath.length > 1 && rawPath.endsWith('/') && !rawPath.includes('.');

    const is404Doc = rawLower === '/404.html';

    // Block public leakage of legacy fragment paths and booking engine internals
    if (
      rawLower.startsWith('/content/') ||
      rawLower.startsWith('/partials/') ||
      rawLower.startsWith('/shared/') ||
      rawLower.startsWith('/workers/') ||
      rawLower.startsWith('/scripts/') ||
      rawLower.startsWith('/node_modules/') ||
      rawLower === '/content' ||
      rawLower === '/partials' ||
      rawLower === '/shared' ||
      rawLower === '/workers' ||
      rawLower === '/scripts' ||
      rawLower === '/node_modules'
    ) {
      const notFound = await env.ASSETS.fetch(new URL('/404.html', url.origin));
      return new Response(notFound.body, {
        status: 404,
        headers: {
          'content-type': 'text/html; charset=utf-8',
          'cache-control': 'no-store',
        },
      });
    }

    const legacyTarget = LEGACY_REDIRECTS[rawLower] || LEGACY_REDIRECTS[rawPath];
    if (legacyTarget && !is404Doc) {
      const dest = new URL(url.toString());
      dest.hostname = APEX_HOST;
      dest.protocol = 'https:';
      dest.pathname = legacyTarget;
      if (dest.toString() !== url.toString()) {
        return Response.redirect(dest.toString(), 301);
      }
    }

    if ((isWww || isHttp || hasHtml || hasTrail) && !is404Doc) {
      const dest = new URL(url.toString());
      dest.hostname = APEX_HOST;
      dest.protocol = 'https:';
      dest.pathname = toCanonicalPath(rawPath);
      if (dest.toString() !== url.toString()) {
        return Response.redirect(dest.toString(), 301);
      }
    }

    if (isWww || isHttp) {
      const dest = new URL(url.toString());
      dest.hostname = APEX_HOST;
      dest.protocol = 'https:';
      if (dest.toString() !== url.toString()) {
        return Response.redirect(dest.toString(), 301);
      }
    }

    const assetResponse = await env.ASSETS.fetch(request);

    if (assetResponse.status === 404) {
      const notFound = await env.ASSETS.fetch(new URL('/404.html', url.origin));
      return new Response(notFound.body, {
        status: 404,
        headers: {
          'content-type': 'text/html; charset=utf-8',
          'cache-control': 'no-store',
        },
      });
    }

    return assetResponse;
  },
};
