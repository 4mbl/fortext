from fortext.style import style

CLR_KEY = '#e06c75'
CLR_ARR = '#e5c07b'
CLR_DICT = '#ffd700'
CLR_STR = '#98c379'
CLR_NUM = '#d19a58'
CLR_BOOL = '#d19a66'


def syntax_highlight_string(val):
    if isinstance(val, str):
        return style(repr(val), fg=CLR_STR)
    if isinstance(val, int):
        return style(repr(val), fg=CLR_NUM)
    if isinstance(val, bool):
        return style(repr(val), fg=CLR_BOOL)
    return repr(val)


def pretty_print_dict(dictionary: dict,
                      prettify_lists=False,
                      indent: int = 2,
                      curr_indent: int = 0,
                      trailing_comma=False,
                      do_pre_indent=True):
    lcub = style('{', fg=CLR_DICT)
    rcub = style('}', fg=CLR_DICT)

    pre_identation = " " * curr_indent if do_pre_indent else ''
    print(f'{pre_identation}{lcub}')

    for i, (key, val) in enumerate(dictionary.items()):

        pretty_key = style(repr(key), fg=CLR_KEY)

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


def pretty_print_list(
    lst: list,
    trailing_comma=False,
):
    lsqb = style('[', fg=CLR_ARR)
    rsqb = style(']', fg=CLR_ARR)

    print(f'{lsqb}', end='')

    for i, val in enumerate(lst):
        comma = ', ' if (i < len(lst) - 1) else ''
        pretty_value = syntax_highlight_string(val)
        print(f'{pretty_value}{comma}', end='')

    print(f'{rsqb}{"," if trailing_comma else ""}')
