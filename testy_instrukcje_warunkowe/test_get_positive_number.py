from instrukcje_warunkowe.is_number_positive_negative_or_zero import get_positive_number


def test_get_positive_number():
    a = 5
    expected = True

    result = get_positive_number(a)
    assert result == expected





