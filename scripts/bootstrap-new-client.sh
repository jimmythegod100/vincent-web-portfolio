#!/usr/bin/env bash
# Bootstrap a new portfolio from the Vincent template repo.
# Usage: ./scripts/bootstrap-new-client.sh CLIENT_SLUG [GITHUB_USER]
set -euo pipefail

SLUG="${1:?Usage: bootstrap-new-client.sh client-slug [github-user]}"
GH_USER="${2:-jimmythegod100}"
TARGET="${HOME}/Projects/${SLUG}"

if [[ -d "$TARGET" ]]; then
  echo "ERROR: $TARGET already exists" >&2
  exit 1
fi

cp -R "$(cd "$(dirname "$0")/.." && pwd)" "$TARGET"
rm -rf "$TARGET/.git"
cd "$TARGET"

cp config/client.template.js js/site-config.js

echo "Created $TARGET"
echo "Next:"
echo "  1. Edit js/site-config.js"
echo "  2. Edit index.html copy + images/"
echo "  3. git init && gh repo create ${GH_USER}/${SLUG} --public --source=. --push"
echo "  4. Enable GitHub Pages on main / root"
echo "  5. See docs/PROCESS.md and docs/INTEGRATIONS.md"
