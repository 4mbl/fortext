"""Style text with ANSI escape codes."""

from .ansi import ESC, RESET, Bg, Fg, Frmt, bg_hex, bg_rgb, fg_hex, fg_rgb


def style(
    text: str,
    fg: Fg | str | tuple[int, int, int] = Fg.DEFAULT,
    bg: Bg | str | tuple[int, int, int] = Bg.DEFAULT,
    frmt: list[Frmt] | None = None,
) -> str:
    """Style a string using ANSI escape codes.

    Args:
        text (str):
            String to style.
        fg (Fg | str | tuple[int, int, int], optional):
            Text (foreground) color. Either a Fg enum, a hex color string, or an RGB tuple.
        bg (Bg | str | tuple[int, int, int], optional):
            Background color. Either a Bg enum, a hex color string, or an RGB tuple.
        frmt (Frmt[Style], optional):
            List of formatting to apply.

    Returns:
        str: Styled text.

    """
    if isinstance(fg, str):
        fore = fg_hex(fg)
    if isinstance(fg, tuple):
        fore = fg_rgb(fg)
    if isinstance(fg, Fg):
        fore = f'{fg.value}'

    if isinstance(bg, str):
        back = bg_hex(bg)
    if isinstance(bg, tuple):
        back = bg_rgb(bg)
    if isinstance(bg, Bg):
        back = f'{bg.value}'

    if frmt is None:
        frmt = []
    else:
        frmt.sort()

    frmt_string = ''
    for f in frmt:
        frmt_string += f';{f.value}'

    return f'{ESC}{fore};{back}{frmt_string}m{text}{RESET}'
