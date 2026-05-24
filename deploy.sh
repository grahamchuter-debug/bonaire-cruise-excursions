#!/bin/bash
set -euo pipefail
cd "$(dirname "$0")"

NODE="${NODE:-/Applications/Cursor.app/Contents/Resources/app/resources/helpers/node}"
NPM="${NPM:-./.tools/package/bin/npm-cli.js}"

if [[ ! -x "$NODE" ]]; then
  NODE="$(command -v node)"
fi

if [[ ! -f node_modules/.bin/wrangler ]]; then
  if [[ -f "$NPM" ]]; then
    "$NODE" "$NPM" install
  else
    npm install
  fi
fi

echo "Logging into Cloudflare (browser will open)..."
"$NODE" node_modules/wrangler/bin/wrangler.js login

echo "Deploying Dominica site to bonaire-cruise-excursions worker..."
"$NODE" node_modules/wrangler/bin/wrangler.js deploy

echo "Done. Check https://dominicashoreexcursions.com/ in a minute."
