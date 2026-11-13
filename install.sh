#!/usr/bin/env bash
# Installs the `ccm` curriculum tool.
#   curl -fsSL https://raw.githubusercontent.com/Chargers-4189/cc-curriculum/main/install.sh | bash
set -euo pipefail

REPO="${CCM_REPO:-Chargers-4189/cc-curriculum}"
REF="${CCM_INSTALL_REF:-main}"
BIN_DIR="${CCM_BIN_DIR:-$HOME/.local/bin}"
URL="https://raw.githubusercontent.com/$REPO/$REF/tools/ccm"

fail() { printf 'install: %s\n' "$*" >&2; exit 1; }

for cmd in curl tar; do
  command -v "$cmd" >/dev/null 2>&1 || fail "'$cmd' is required but not installed"
done

tmp=$(mktemp "${TMPDIR:-/tmp}/ccm-install.XXXXXX")
trap 'rm -f "$tmp"' EXIT

curl -fsSL "$URL" -o "$tmp" || fail "could not download $URL"
head -n 1 "$tmp" | grep -q '^#!/usr/bin/env bash' || fail "downloaded file is not the ccm script"
bash -n "$tmp" || fail "downloaded ccm script has syntax errors"

mkdir -p "$BIN_DIR"
chmod +x "$tmp"
mv "$tmp" "$BIN_DIR/ccm"
trap - EXIT

echo "Installed ccm to $BIN_DIR/ccm"

case ":$PATH:" in
  *":$BIN_DIR:"*) ;;
  *)
    rc="$HOME/.bashrc"
    case "${SHELL:-}" in */zsh) rc="$HOME/.zshrc" ;; esac
    line="export PATH=\"$BIN_DIR:\$PATH\""
    if [ -f "$rc" ] && grep -qsF "$line" "$rc"; then :; else
      printf '\n# Added by ccm installer\n%s\n' "$line" >> "$rc"
      echo "Added $BIN_DIR to PATH in $rc"
    fi
    echo "Open a new terminal (or run: source $rc) before using ccm."
    ;;
esac

if ! command -v javac >/dev/null 2>&1 && ! ls -d "$HOME"/wpilib/*/jdk/bin >/dev/null 2>&1; then
  echo "Note: Java (JDK 17+) was not found. You need it for 'ccm test'."
fi

echo "Try: ccm list"
