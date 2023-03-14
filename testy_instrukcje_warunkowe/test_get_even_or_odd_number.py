from instrukcje_warunkowe.is_number_even_or_odd import get_even_or_odd_number


def test_get_even_or_odd_number():
    a = 6
    b = 5
    expected1 = "Even"
    expected2 = "Odd"

    result1 = get_even_or_odd_number(a)
    result2 = get_even_or_odd_number(b)
    assert result1 == expected1
    assert result2 == expected2


