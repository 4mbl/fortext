import pytest

from fortext import permutations


def test_permutations_basic():
    result = list(permutations('abc', max_len=3))
    expected = [
        'a',
        'b',
        'c',
        'ab',
        'ac',
        'ba',
        'bc',
        'ca',
        'cb',
        'abc',
        'acb',
        'bac',
        'bca',
        'cab',
        'cba',
    ]
    assert result == expected


def test_permutations_with_repetition():
    result = list(permutations('ab', max_len=2, min_len=2, allow_repetition=True))
    expected = ['aa', 'ab', 'ba', 'bb']
    assert result == expected


def test_permutations_min_len():
    result = list(permutations('abc', min_len=1))
    expected = ['a', 'b', 'c', 'ab', 'ac', 'ba', 'bc', 'ca', 'cb', 'abc', 'acb', 'bac', 'bca', 'cab', 'cba']  # fmt: off
    assert result == expected


def test_permutations_max_len():
    result = list(permutations('abc', max_len=2))
    expected = ['a', 'b', 'c', 'ab', 'ac', 'ba', 'bc', 'ca', 'cb']
    assert result == expected


def test_permutations_empty_string():
    result = list(permutations('', min_len=1))
    expected: list[str] = []
    assert result == expected


def test_permutations_single_character():
    result = list(permutations('a', min_len=1, max_len=1))
    expected = ['a']
    assert result == expected


def test_permutations_allow_repetition_min_len():
    result = list(permutations('ab', min_len=1, max_len=2, allow_repetition=True))
    expected = ['a', 'b', 'aa', 'ab', 'ba', 'bb']
    assert result == expected


def test_permutations_invalid_min_len():
    result = list(permutations('abc', max_len=3, min_len=5))
    expected: list[str] = []
    assert result == expected


def test_permutations_allow_repetition_with_max_len():
    result = list(permutations('abc', max_len=2, min_len=1, allow_repetition=True))
    expected = ['a', 'b', 'c', 'aa', 'ab', 'ac', 'ba', 'bb', 'bc', 'ca', 'cb', 'cc']
    assert result == expected


def test_permutations_no_repetition_with_max_len():
    result = list(permutations('abc', max_len=2, min_len=1, allow_repetition=False))
    expected = ['a', 'b', 'c', 'ab', 'ac', 'ba', 'bc', 'ca', 'cb']
    assert result == expected
