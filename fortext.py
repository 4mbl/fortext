from typing import List, Tuple
from ansi import Fg, Bg, Style, ESC, RESET, bg_hex, bg_rgb, fg_hex, fg_rgb


def color(text: str,
          fg: Fg | str | Tuple[int, int, int] |
          List[int, int, int] = Fg.DEFAULT,
          bg: Bg | str | Tuple[int, int, int] |
          List[int, int, int] = Bg.DEFAULT,
          styles: List[Style] = None) -> str:

    if fg is None:
        fg = Fg.DEFAULT
    if isinstance(fg, str):
        fore = fg_hex(fg)
    if isinstance(fg, tuple):
        fore = fg_rgb(fg)
    if isinstance(fg, Fg):
        fore = fg.value

    if bg is None:
        bg = Bg.DEFAULT
    if isinstance(bg, str):
        back = bg_hex(bg)
    if isinstance(bg, tuple):
        back = bg_rgb(bg)
    if isinstance(bg, Bg):
        back = bg.value

    if styles is None:
        styles = []
    else:
        styles.sort()

    style_string = ''
    for style in styles:
        style_string += f';{style.value}'

    return f'{ESC}{fore};{back}{style_string}m{text}{RESET}'
