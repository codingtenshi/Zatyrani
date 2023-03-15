from pętle.return_negative_number import get_negative_number
import pytest


@pytest.mark.parametrize("ex, expected", [
    [[5, 6, 8, 0, -4, -3], [-4, -3]],
    [[-3, 4, 6, -7], [-3, -7]]
])
def test_get_negative_number(ex, expected):

    result = get_negative_number(ex)
    assert result == expected


def test_get_negative_number_with_empty_list():
    ex = []
    expected = []

    result = get_negative_number(ex)
    assert result == expected