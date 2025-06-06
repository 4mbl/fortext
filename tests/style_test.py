import pytest

from fortext import Bg, Fg, Frmt, style


def test_style_with_enum_fg_bg():
    result = style('Hello', fg=Fg.RED, bg=Bg.BLACK)
    expected = '\033[31;40mHello\033[0m'
    assert result == expected


def test_style_with_hex_fg_bg():
    result = style('Hello', fg='#FF0000', bg='#00FF00')
    expected = '\033[38;2;255;0;0;48;2;0;255;0mHello\033[0m'
    assert result == expected


def test_style_with_rgb_fg_bg():
    result = style('Hello', fg=(255, 0, 0), bg=(0, 255, 0))
    expected = '\033[38;2;255;0;0;48;2;0;255;0mHello\033[0m'
    assert result == expected


def test_style_with_formatting():
    result = style('Hello', fg=Fg.RED, bg=Bg.BLACK, frmt=[Frmt.BOLD, Frmt.UNDERLINE])
    expected = '\033[31;40;1;4mHello\033[0m'
    assert result == expected


def test_style_with_multiple_formatting():
    result = style('Hello', fg=Fg.GREEN, bg=Bg.YELLOW, frmt=[Frmt.BOLD, Frmt.ITALIC])
    expected = '\033[32;43;1;3mHello\033[0m'
    assert result == expected


def test_style_with_empty_formatting():
    result = style('Hello', fg=Fg.BLUE, bg=Bg.WHITE, frmt=[])
    expected = '\033[34;47mHello\033[0m'
    assert result == expected


def test_style_with_default_fg_bg():
    result = style('Hello')
    expected = '\033[39;49mHello\033[0m'
    assert result == expected


def test_style_with_invalid_fg():
    with pytest.raises(ValueError):
        style('Hello', fg='invalid_color', bg=Bg.BLACK)


def test_style_with_invalid_bg():
    with pytest.raises(ValueError):
        style('Hello', fg=Fg.RED, bg='invalid_color')


def test_style_with_mixed_fg_bg_formats():
    result = style('Test', fg='#0000ff', bg=(255, 255, 255), frmt=[Frmt.ITALIC])
    expected = '\033[38;2;0;0;255;48;2;255;255;255;3mTest\033[0m'
    assert result == expected
