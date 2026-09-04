#!/bin/bash
set -euo pipefail
cd "$(dirname "$0")"

if [[ ! -f node_modules/.bin/wrangler ]]; then
  npm install
fi

echo "Deploying Bonaire site to bonaire-cruise-excursions worker..."
npx wrangler deploy

echo "Done. Check https://bonairecruiseexcursions.com/ in a minute."
