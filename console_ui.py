"""Reusable ANSI console styling utilities."""

import os
import sys


COLORS = {
    "reset": "\033[0m",
    "bold": "\033[1m",
    "gray": "\033[90m",
    "red": "\033[91m",
    "green": "\033[92m",
    "yellow": "\033[93m",
    "blue": "\033[94m",
    "purple": "\033[95m",
    "cyan": "\033[96m",
    "white": "\033[97m",
}

WIDTH = 66


def color_enabled():
    """Disable ANSI colors for redirected output."""

    if "NO_COLOR" in os.environ:
        return False

    if os.environ.get("TERM") == "dumb":
        return False

    return bool(sys.stdout.isatty())


def paint(value, color="white", bold=False):
    """Apply a color and restore the default style."""

    text = str(value)

    if not color_enabled():
        return text

    prefix = COLORS[color]

    if bold:
        prefix += COLORS["bold"]

    return prefix + text + COLORS["reset"]


def line(character="-"):
    """Print a neutral separator."""

    print(paint(character * WIDTH, "gray"))


def header(title, subtitle=None, color="yellow"):
    """Display a section title with vertical spacing."""

    print()
    line("=")

    print(paint(title, color, bold=True))

    if subtitle:
        print(paint(subtitle, "gray"))

    line("=")
    print()


def field(label, value, color="white"):
    """Display a labeled value."""

    print(
        f" {label} : "
        f"{paint(value, color, bold=True)}"
    )


def menu_item(number, label):
    """Display a numbered menu item."""

    print(
        f" {paint(f'[{number}]', 'cyan', True)} "
        f" {label}"
    )


def prompt(message):
    """Read user input using a colored prompt."""

    return input(paint(message, "green", True))


def message(text, color="white"):
    """Display a separated status message."""

    print()
    print(paint(text, color, True))
    print()


def progress_bar(current, total, width=30):
    """Display a text-based progress bar."""

    ratio = current / total if total else 0
    ratio = max(0.0, min(1.0, ratio))

    filled = int(ratio * width)

    bar = (
        paint("#" * filled, "cyan")
        + paint("-" * (width - filled), "gray")
    )

    print(f" [{bar}] {ratio * 100:.0f}%")


def score_bar(score):
    """Display a normalized score bar."""

    progress_bar(score, 100)
