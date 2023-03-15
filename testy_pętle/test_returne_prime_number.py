from pętle.return_prime_number import get_prime_number
import pytest


@pytest.mark.parametrize("nbs, expected", [
    [[11, 0, 2.3, -2, 2, 4], [11, 2, 4]],
    [[2, 4, 9.8, 1, -4, -5], [2, 4]],
    [[-3, 0.4, 1, 3, 5], [3, 5]]
])
def test_get_prime_number(nbs, expected):

    result = get_prime_number(nbs)
    assert result == expected