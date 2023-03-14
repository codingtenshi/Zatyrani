from instrukcje_warunkowe.is_number_even_or_odd import get_even_or_odd_number


def test_get_even_or_odd_number():
    a = 6
    expected = "Even"

    result = get_even_or_odd_number(a)
    assert result == expected
