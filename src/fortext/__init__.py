"""API entry point for the forfiles package."""

from .ansi import Bg, Fg, Frmt, print_styles, print_styles_all
from .permutation import permutations
from .style import style
from .syntax import DEFAULT_SYNTAX_HIGHLIGHT_COLORS, highlight

__all__ = [
    'DEFAULT_SYNTAX_HIGHLIGHT_COLORS',
    'Bg',
    'Fg',
    'Frmt',
    'highlight',
    'permutations',
    'print_styles',
    'print_styles_all',
    'style',
]
