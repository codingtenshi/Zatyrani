from pętle.return_even_numbers_from_a_list import get_even_numbers
import pytest


@pytest.mark.parametrize("nbs, expected", [
    [[6, 3, 5, 8, 4], [6, 8, 4]],
    [[1, 2, 3, 4, 5], [2, 4]],
    [[2, 2, 3, 6, 1], [2, 2, 6]]
])
def test_get_even_numbers(nbs, expected):

    result = get_even_numbers(nbs)
    assert result == expected


def test_get_even_numbers_is_empty():
    nbs = []
    expected = []

    result = get_even_numbers(nbs)
    assert result == expected




