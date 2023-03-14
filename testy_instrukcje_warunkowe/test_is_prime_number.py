from instrukcje_warunkowe.is_prime_number import get_prime_number
import pytest


@pytest.mark.parametrize("nb, expected", [
    [11, "Prime"],
    [-1, "Not prime"],
    [0.3, "Not prime"]
])
def test_get_prime_number(nb, expected):

    result = get_prime_number(nb)
    assert result == expected

