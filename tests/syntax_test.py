import pytest

from fortext import SyntaxHighlightingOptions, highlight


def test_highlight_basic_dict():
    value = {'key1': 'value1', 'key2': 2}
    result = highlight(value)
    expected = "\033[38;2;255;215;0;49m{\033[0m\n  \033[38;2;224;108;117;49m'key1'\033[0m: \033[38;2;152;195;121;49m'value1'\033[0m,\n  \033[38;2;224;108;117;49m'key2'\033[0m: \033[38;2;209;154;88;49m2\033[0m\n\033[38;2;255;215;0;49m}\033[0m"
    assert result == expected


def test_highlight_basic_list():
    value = ['item1', 2, True]
    result = highlight(value)
    expected = "\033[38;2;255;215;0;49m[\033[0m\n  \033[38;2;152;195;121;49m'item1'\033[0m,\n  \033[38;2;209;154;88;49m2\033[0m,\n  \033[38;2;209;154;88;49mTrue\033[0m\n\033[38;2;255;215;0;49m]\033[0m"
    assert result == expected


def test_highlight_with_trailing_comma():
    options = SyntaxHighlightingOptions(
        indent=2,
        curr_indent=0,
        trailing_comma=True,
        pre_indent=True,
        colors={
            'key': '#e06c75',
            'arr': '#ffd700',
            'dict': '#ffd700',
            'str': '#98c379',
            'num': '#d19a58',
            'bool': '#d19a66',
        },
    )
    value = {'key1': 'value1', 'key2': 2}
    result = highlight(value, options=options)
    expected = "\033[38;2;255;215;0;49m{\033[0m\n  \033[38;2;224;108;117;49m'key1'\033[0m: \033[38;2;152;195;121;49m'value1'\033[0m,\n  \033[38;2;224;108;117;49m'key2'\033[0m: \033[38;2;209;154;88;49m2\033[0m\n\033[38;2;255;215;0;49m}\033[0m,\n"
    assert result == expected


def test_highlight_with_pre_indent():
    options = SyntaxHighlightingOptions(
        indent=2,
        curr_indent=0,
        trailing_comma=False,
        pre_indent=True,
        colors={
            'key': '#e06c75',
            'arr': '#ffd700',
            'dict': '#ffd700',
            'str': '#98c379',
            'num': '#d19a58',
            'bool': '#d19a66',
        },
    )
    value = {'key1': 'value1', 'key2': 2}
    result = highlight(value, options=options)
    expected = "\033[38;2;255;215;0;49m{\033[0m\n  \033[38;2;224;108;117;49m'key1'\033[0m: \033[38;2;152;195;121;49m'value1'\033[0m,\n  \033[38;2;224;108;117;49m'key2'\033[0m: \033[38;2;209;154;88;49m2\033[0m\n\033[38;2;255;215;0;49m}\033[0m"
    assert result == expected


def test_highlight_with_custom_colors():
    custom_colors = {
        'key': '#ff5733',
        'arr': '#33ff57',
        'dict': '#5733ff',
        'str': '#f0f0f0',
        'num': '#f0f0f0',
        'bool': '#f0f0f0',
    }
    options = SyntaxHighlightingOptions(
        indent=2, curr_indent=0, trailing_comma=False, pre_indent=True, colors=custom_colors
    )
    value = {'key1': 'value1', 'key2': 2}
    result = highlight(value, options=options)
    expected = "\033[38;2;87;51;255;49m{\033[0m\n  \033[38;2;255;87;51;49m'key1'\033[0m: \033[38;2;240;240;240;49m'value1'\033[0m,\n  \033[38;2;255;87;51;49m'key2'\033[0m: \033[38;2;240;240;240;49m2\033[0m\n\033[38;2;87;51;255;49m}\033[0m"
    assert result == expected


def test_highlight_with_empty_dict():
    value: dict[None, None] = {}
    result = highlight(value)
    expected = '\033[38;2;255;215;0;49m{\033[0m\n\033[38;2;255;215;0;49m}\033[0m'
    assert result == expected


def test_highlight_with_empty_list():
    value: list[None] = []
    result = highlight(value)
    expected = '\033[38;2;255;215;0;49m[\033[0m\n\033[38;2;255;215;0;49m]\033[0m'
    assert result == expected


def test_highlight_str_value():
    value = 'hello world'
    result = highlight(value)
    expected = "\033[38;2;152;195;121;49m'hello world'\033[0m"
    assert result == expected


def test_highlight_bool_value():
    value = True
    result = highlight(value)
    expected = '\033[38;2;209;154;88;49mTrue\033[0m'
    assert result == expected


def test_highlight_int_value():
    value = 42
    result = highlight(value)
    expected = '\033[38;2;209;154;88;49m42\033[0m'
    assert result == expected


def test_highlight_float_value():
    value = 3.14
    result = highlight(value)
    expected = '\033[38;2;209;154;88;49m3.14\033[0m'
    assert result == expected


def test_highlight_invalid_type():
    value = object()
    result = highlight(value)
    expected = 'object'
    assert result == expected


def test_highlight_list_with_trailing_comma():
    options = SyntaxHighlightingOptions(
        indent=2,
        curr_indent=0,
        trailing_comma=True,
        pre_indent=True,
        colors={
            'key': '#e06c75',
            'arr': '#ffd700',
            'dict': '#ffd700',
            'str': '#98c379',
            'num': '#d19a58',
            'bool': '#d19a66',
        },
    )
    value = ['item1', 'item2']
    result = highlight(value, options=options)
    expected = "\033[38;2;255;215;0;49m[\033[0m\n  \033[38;2;152;195;121;49m'item1'\033[0m,\n  \033[38;2;152;195;121;49m'item2'\033[0m\n\033[38;2;255;215;0;49m]\033[0m,\n"
    assert result == expected
