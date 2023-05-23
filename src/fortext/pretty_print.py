from fortext.style import style

SYNTAX_HIGHLIGHT_COLORS = {
    'key': '#e06c75',
    'arr': '#e5c07b',
    'dict': '#ffd700',
    'str': '#98c379',
    'num': '#d19a58',
    'bool': '#d19a66',
}


def syntax_highlight_string(val, colors=None):
    if colors is None:
        colors = SYNTAX_HIGHLIGHT_COLORS
    if isinstance(val, str):
        return style(repr(val), fg=colors['str'])
    if isinstance(val, int):
        return style(repr(val), fg=colors['num'])
    if isinstance(val, bool):
        return style(repr(val), fg=colors['bool'])
    return repr(val)


def pretty_print_dict(dictionary: dict,
                      prettify_lists=False,
                      indent: int = 2,
                      curr_indent: int = 0,
                      trailing_comma=False,
                      do_pre_indent=True,
                      colors=None):
    if colors is None:
        colors = SYNTAX_HIGHLIGHT_COLORS

    lcub = style('{', fg=colors['dict'])
    rcub = style('}', fg=colors['dict'])

    pre_identation = " " * curr_indent if do_pre_indent else ''
    print(f'{pre_identation}{lcub}')

    for i, (key, val) in enumerate(dictionary.items()):

        pretty_key = style(repr(key), fg=colors['key'])

        if isinstance(val, dict):
            print(f'{" "*(curr_indent + indent)}{pretty_key}: ', end='')
            pretty_print_dict(val,
                              indent=curr_indent + indent,
                              curr_indent=curr_indent + indent,
                              trailing_comma=True,
                              do_pre_indent=False)
            continue
        if isinstance(val, list) and prettify_lists:
            print(f'{" "*(curr_indent + indent)}{pretty_key}: ', end='')
            pretty_print_list(val)
            continue

        comma = ',' if (i < len(dictionary) - 1) else ''

        pretty_value = syntax_highlight_string(val)

        print(
            f'{" "*(curr_indent + indent)}{pretty_key}: {pretty_value}{comma}')

    print(f'{" "* curr_indent}{rcub}{"," if trailing_comma else ""}')


def pretty_print_list(lst: list, trailing_comma=False, colors=None):
    if colors is None:
        colors = SYNTAX_HIGHLIGHT_COLORS

    lsqb = style('[', fg=colors['arr'])
    rsqb = style(']', fg=colors['arr'])

    print(f'{lsqb}', end='')

    for i, val in enumerate(lst):
        comma = ', ' if (i < len(lst) - 1) else ''
        pretty_value = syntax_highlight_string(val)
        print(f'{pretty_value}{comma}', end='')

    print(f'{rsqb}{"," if trailing_comma else ""}')
