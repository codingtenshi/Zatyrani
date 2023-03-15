from pętle.return_positive_number import get_positive_number
import pytest


@pytest.mark.parametrize("nbs, expected", [
    [[5, 6, 8, 0, -4, -3], [5, 6, 8]],
    [[4, -3, -4, 6], [4, 6]],
    [[0, -2, -4, 8], [8]]
])
def test_get_positive_number(nbs, expected):

    result = get_positive_number(nbs)
    assert result == expected


def test_get_positive_number_with_empty_list():
    nbs = []
    expected = []

    result = get_positive_number(nbs)
    assert result == expected