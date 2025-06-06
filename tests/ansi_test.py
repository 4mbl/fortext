import pytest

from fortext import (
    Bg,
    Fg,
    Frmt,
    print_styles,
    print_styles_all,
)

# internal imports for testing
from fortext.ansi import bg_hex, bg_rgb, fg_hex, fg_rgb, hex2rgb


def test_fg_rgb():
    assert fg_rgb((255, 0, 0)) == '38;2;255;0;0'
    assert fg_rgb((0, 255, 0)) == '38;2;0;255;0'
    assert fg_rgb((0, 0, 255)) == '38;2;0;0;255'


def test_fg_hex():
    assert fg_hex('#FF0000') == '38;2;255;0;0'
    assert fg_hex('00FF00') == '38;2;0;255;0'
    assert fg_hex('#0000FF') == '38;2;0;0;255'


def test_bg_rgb():
    assert bg_rgb((255, 0, 0)) == '48;2;255;0;0'
    assert bg_rgb((0, 255, 0)) == '48;2;0;255;0'
    assert bg_rgb((0, 0, 255)) == '48;2;0;0;255'


def test_bg_hex():
    assert bg_hex('#FF0000') == '48;2;255;0;0'
    assert bg_hex('00FF00') == '48;2;0;255;0'
    assert bg_hex('#0000FF') == '48;2;0;0;255'


def test_hex2rgb():
    assert hex2rgb('#FF0000') == (255, 0, 0)
    assert hex2rgb('00FF00') == (0, 255, 0)
    assert hex2rgb('#0000FF') == (0, 0, 255)
    assert hex2rgb('123456') == (18, 52, 86)


@pytest.mark.parametrize('ansi_type,expected_type', [(Fg, Fg), (Bg, Bg), (Frmt, Frmt)])
def test_print_styles(ansi_type, expected_type):
    from io import StringIO
    import sys

    captured_output = StringIO()
    sys.stdout = captured_output

    print_styles(ansi_type)

    for style in expected_type:
        assert f'\033[{style.value}mExample Text' in captured_output.getvalue()

    sys.stdout = sys.__stdout__  # reset stdout


def test_print_styles_all():
    from io import StringIO
    import sys

    captured_output = StringIO()
    sys.stdout = captured_output

    print_styles_all()

    for style in Fg:
        assert f'\033[{style.value}mExample Text' in captured_output.getvalue()
    for style in Bg:
        assert f'\033[{style.value}mExample Text' in captured_output.getvalue()
    for style in Frmt:
        assert f'\033[{style.value}mExample Text' in captured_output.getvalue()

    sys.stdout = sys.__stdout__  # reset stdout
