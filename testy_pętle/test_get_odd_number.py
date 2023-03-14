from pętle.return_odd_numbers_from_a_list import get_odd_numbers
import pytest


@pytest.mark.parametrize("nbs, expected", [
    [[6, 3, 5, 8, 4], [3, 5]],
    [[2, 1, -5, 4], [1, -5]],
    [[-5, -7], [-5, -7]]
])
def test_get_odd_numbers(nbs, expected):

    result = get_odd_numbers(nbs)
    assert result == expected


def test_get_odd_numbers_with_empty_list():
    nbs = []
    expected = []

    result = get_odd_numbers(nbs)
    assert result == expected

