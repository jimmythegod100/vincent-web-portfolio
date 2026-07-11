#!/usr/bin/env bash
# Smoke-test studio API (and optional showcase) once containers are up.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$ROOT"

API_PORT="${STUDIO_API_PORT:-8000}"
SHOWCASE_PORT="${SHOWCASE_FRONTEND_PORT:-8090}"

echo "==> Studio API health (localhost:${API_PORT})"
if ! curl -sf "http://127.0.0.1:${API_PORT}/health" | tee /tmp/studio-health.json; then
  echo
  echo "Studio API not reachable. On the iMac run: make up"
  exit 1
fi
echo

echo "==> Studio API docs"
curl -sf -o /dev/null -w "docs HTTP %{http_code}\n" "http://127.0.0.1:${API_PORT}/docs"

if curl -sf "http://127.0.0.1:${SHOWCASE_PORT}/health" >/dev/null 2>&1; then
  echo "==> Showcase health (localhost:${SHOWCASE_PORT})"
  curl -sf "http://127.0.0.1:${SHOWCASE_PORT}/health"
  echo
else
  echo "==> Showcase not running (optional). Start with: make showcase"
fi

echo
echo "Smoke checks passed."
