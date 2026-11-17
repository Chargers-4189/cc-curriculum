"""Questions for the Python tools. Uses gum (github.com/charmbracelet/gum) like ccm does when
it's installed and you're in a terminal, and a plain prompt otherwise. CCM_NO_GUM=1 turns gum off."""
from __future__ import annotations

import os
import shutil
import subprocess
import sys


GUM = os.environ.get("CCM_GUM") or shutil.which("gum")  # ccm passes the gum it uses (and its colors)


def have_gum() -> bool:
    return (os.environ.get("CCM_NO_GUM") != "1" and bool(GUM) and GUM != "none"
            and sys.stdin.isatty() and sys.stderr.isatty())


def choose(header: str, options: list[str]) -> str | None:
    """Pick one option. Returns None if cancelled or there's no one to ask."""
    if not options or not sys.stdin.isatty():
        return None
    if have_gum():
        r = subprocess.run([GUM, "choose", "--header", header, *options], stdout=subprocess.PIPE, text=True)
        return r.stdout.strip() or None if r.returncode == 0 else None
    print(header, file=sys.stderr)
    for i, o in enumerate(options, 1):
        print(f"  {i}) {o}", file=sys.stderr)
    try:
        pick = input("> ").strip()
    except EOFError:
        return None
    return options[int(pick) - 1] if pick.isdigit() and 1 <= int(pick) <= len(options) else None


def search(header: str, options: list[str]) -> str | None:
    """Pick one option from a long list you can type to search. None if cancelled."""
    if not options or not sys.stdin.isatty():
        return None
    if have_gum():
        r = subprocess.run([GUM, "filter", "--header", header, "--placeholder", "Type to search", "--height", "14"],
                           input="\n".join(options), stdout=subprocess.PIPE, text=True)
        return r.stdout.strip() or None if r.returncode == 0 else None
    return choose(header, options)


def pick_many(header: str, options: list[str]) -> list[str]:
    """Pick any number of options. Returns [] if cancelled or there's no one to ask."""
    if not options or not sys.stdin.isatty():
        return []
    if have_gum():
        r = subprocess.run([GUM, "choose", "--no-limit", "--header", header + " (space to select, enter when done)",
                            *options], stdout=subprocess.PIPE, text=True)
        return [l for l in r.stdout.splitlines() if l] if r.returncode == 0 else []
    print(header, file=sys.stderr)
    for i, o in enumerate(options, 1):
        print(f"  {i}) {o}", file=sys.stderr)
    try:
        picks = input("Numbers separated by spaces, or 'all': ").strip().lower()
    except EOFError:
        return []
    if picks == "all":
        return list(options)
    return [options[int(p) - 1] for p in picks.replace(",", " ").split() if p.isdigit() and 1 <= int(p) <= len(options)]


class Spinner:
    """One spinner for a whole run, so it doesn't flash on and off between steps.

        with Spinner("Checking pages...") as spin:
            for page in pages:
                spin.update(f"Checking {page}...")
                spin.echo("a result line")   # prints above the spinner

    Nothing shows if stderr isn't a terminal (echo still prints)."""

    FRAMES = "⣾⣽⣻⢿⡿⣟⣯⣷"

    def __init__(self, text: str = ""):
        self.text = text
        self._stop = None
        self._lock = None

    def __enter__(self):
        global CURRENT
        CURRENT = self
        if not sys.stderr.isatty():
            return self
        import threading
        self._stop = threading.Event()
        self._lock = threading.Lock()

        def spin():
            i = 0
            while not self._stop.wait(0.1):
                with self._lock:
                    sys.stderr.write(f"\r\033[38;5;36m{self.FRAMES[i % len(self.FRAMES)]}\033[0m "
                                     f"\033[2m{self.text}\033[0m\033[K")
                    sys.stderr.flush()
                i += 1
        self._thread = threading.Thread(target=spin, daemon=True)
        self._thread.start()
        return self

    def update(self, text: str) -> None:
        self.text = text

    def echo(self, line: str = "") -> None:
        if self._lock:
            with self._lock:
                sys.stderr.write("\r\033[K")
                sys.stderr.flush()
                print(line, flush=True)
        else:
            print(line, flush=True)

    def __exit__(self, *exc):
        global CURRENT
        CURRENT = None
        if self._stop:
            self._stop.set()
            self._thread.join()
            sys.stderr.write("\r\033[K")
            sys.stderr.flush()
        return False


CURRENT: Spinner | None = None


def echo(line: str = "") -> None:
    """print(), but above the spinner if one is running."""
    if CURRENT:
        CURRENT.echo(line)
    else:
        print(line, flush=True)


def confirm(question: str) -> bool:
    """Ask a yes/no question (no by default). Returns False when there's no one to ask."""
    if not sys.stdin.isatty():
        return False
    if have_gum():
        return subprocess.run([GUM, "confirm", "--default=false", question]).returncode == 0
    try:
        return input(f"{question} [y/N] ").strip().lower() in ("y", "yes")
    except EOFError:
        return False
