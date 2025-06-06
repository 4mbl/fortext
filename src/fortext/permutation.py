"""Generate permutations of a string."""

import itertools as it
from collections.abc import Generator


def permutations(
    string: str, max_len: int | None = None, min_len: int = 1, *, allow_repetition: bool = False
) -> Generator[str, None, None]:
    """Generate permutations of a string.

    Args:
        string (str):
            String to permute.
        max_len (int, optional):
            Maximum length of permutations. Defaults to length of the string.
        min_len (int, optional):
            Minimum length of permutations. Defaults to 1.
        allow_repetition (bool, optional):
            Allow repeating characters in a permunation. Defaults to False.

    Yields:
        str: Permutations of the string.

    """
    max_len = len(string) if max_len is None else max_len

    if min_len <= 0:
        min_len = 1

    if min_len > max_len:
        return

    if allow_repetition:
        for i in range(min_len, max_len + 1):
            for p in it.product(string, repeat=i):
                yield ''.join(p)
    else:
        for i in range(min_len, max_len + 1):
            for p in it.permutations(string, i):
                yield ''.join(p)
