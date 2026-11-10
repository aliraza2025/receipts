#!/usr/bin/env bash
# Usage: ./install.sh <claude|codex|cursor|all> [--project DIR]
set -euo pipefail

here="$(cd "$(dirname "$0")" && pwd)"
target="${1:-}"
project=""
if [[ "${2:-}" == "--project" ]]; then
  project="${3:?--project needs a directory}"
fi

dest_for() {
  local agent="$1"
  if [[ -n "$project" ]]; then
    case "$agent" in
      claude) echo "$project/.claude/skills" ;;
      codex)  echo "$project/.agents/skills" ;;
      cursor) echo "$project/.cursor/skills" ;;
    esac
  else
    case "$agent" in
      claude) echo "$HOME/.claude/skills" ;;
      codex)  echo "${CODEX_HOME:-$HOME/.codex}/skills" ;;
      cursor) echo "$HOME/.cursor/skills" ;;
    esac
  fi
}

install_for() {
  local dest
  dest="$(dest_for "$1")"
  mkdir -p "$dest"
  for skill in "$here"/skills/*/; do
    name="$(basename "$skill")"
    rm -rf "${dest:?}/$name"
    cp -R "$skill" "$dest/$name"
  done
  echo "Installed $(ls "$here/skills" | wc -l | tr -d ' ') skills into $dest"
}

case "$target" in
  claude|codex|cursor) install_for "$target" ;;
  all) for a in claude codex cursor; do install_for "$a"; done ;;
  *) echo "Usage: ./install.sh <claude|codex|cursor|all> [--project DIR]" >&2; exit 1 ;;
esac
