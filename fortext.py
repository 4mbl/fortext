from typing import List
from ansi import Fg, Bg, Style, ESC, RESET


def color(text: str,
          fg: Fg = Fg.DEFAULT,
          bg: Bg = Bg.DEFAULT,
          styles: List[Style] = None) -> str:

    if fg is None:
        fg = Fg.DEFAULT

    if bg is None:
        bg = Bg.DEFAULT

    if styles is None:
        styles = []
    else:
        styles.sort()

    style_string = ''
    for style in styles:
        style_string += f';{style.value}'

    return f'{ESC}{fg.value};{bg.value}{style_string}m{text}{RESET}'


print(color("Some text", Fg.RED, Bg.BLUE, [Style.UNDERLINE, Style.ITALIC]))
