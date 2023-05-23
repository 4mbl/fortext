from fortext.style import style

DEFAULT_SYNTAX_HIGHLIGHT_COLORS = {
    'key': '#e06c75',
    'arr': '#ffd700',
    'dict': '#ffd700',
    'str': '#98c379',
    'num': '#d19a58',
    'bool': '#d19a66',
}


def syntax_highlight(val: any,
                     indent=2,
                     curr_indent=0,
                     trailing_comma: bool = False,
                     do_pre_indent=True,
                     colors=None):
    if colors is None:
        colors = DEFAULT_SYNTAX_HIGHLIGHT_COLORS
    if isinstance(val, dict):
        return pretty_dict(val,
                           indent=indent,
                           curr_indent=curr_indent,
                           trailing_comma=trailing_comma,
                           pre_indent=do_pre_indent,
                           colors=colors)
    if isinstance(val, list):
        return pretty_list(val,
                           indent=indent,
                           curr_indent=curr_indent,
                           trailing_comma=trailing_comma,
                           pre_indent=do_pre_indent,
                           colors=colors)
    if isinstance(val, str):
        return style(repr(val), fg=colors['str'])
    if isinstance(val, int):
        return style(repr(val), fg=colors['num'])
    if isinstance(val, bool):
        return style(repr(val), fg=colors['bool'])
    return repr(val)


def pretty_dict(dictionary: dict,
                indent: int = 2,
                curr_indent: int = 0,
                trailing_comma: bool = False,
                pre_indent: bool = True,
                colors=None):
    if colors is None:
        colors = DEFAULT_SYNTAX_HIGHLIGHT_COLORS

    lcub = style('{', fg=colors['dict'])
    rcub = style('}', fg=colors['dict'])

    pre_identation = " " * curr_indent if pre_indent else ''
    output_str = f'{pre_identation}{lcub}\n'

    for i, (key, val) in enumerate(dictionary.items()):
        pretty_key = style(repr(key), fg=colors['key'])
        pretty_value = syntax_highlight(val,
                                        indent=indent,
                                        curr_indent=indent + curr_indent,
                                        do_pre_indent=False,
                                        colors=colors)

        comma = ',' if (i < len(dictionary) - 1) else ''
        output_str += f'{" "*(curr_indent + indent)}{pretty_key}: {pretty_value}{comma}\n'

    trailing_comma = ",\n" if trailing_comma else ""
    output_str += f'{" "* curr_indent}{rcub}{trailing_comma}'
    return output_str


def pretty_list(lst: list,
                indent: int = 2,
                curr_indent: int = 0,
                trailing_comma: bool = False,
                pre_indent: bool = True,
                colors=None):
    if colors is None:
        colors = DEFAULT_SYNTAX_HIGHLIGHT_COLORS

    lsqb = style('[', fg=colors['arr'])
    rsqb = style(']', fg=colors['arr'])

    pre_identation = " " * curr_indent if pre_indent else ''
    output_str = f'{pre_identation}{lsqb}\n'

    for i, val in enumerate(lst):
        pretty_value = syntax_highlight(val,
                                        indent=indent,
                                        curr_indent=indent + curr_indent,
                                        do_pre_indent=False,
                                        colors=colors)
        comma = ',' if (i < len(lst) - 1) else ''
        output_str += f'{" "*(curr_indent + indent)}{pretty_value}{comma}\n'

    trailing_comma = ",\n" if trailing_comma else ""
    output_str += f'{" "* curr_indent}{rsqb}{trailing_comma}'
    return output_str
