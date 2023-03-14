from instrukcje_warunkowe.is_number_positive_negative_or_zero import get_positive_number


def test_get_positive_number():
    a = 5
    b = 0
    c = -5
    expected1 = "Positive"
    expected2 = "Zero"
    expected3 = "Negative"

    result1 = get_positive_number(a)
    result2 = get_positive_number(b)
    result3 = get_positive_number(c)
    assert result1 == expected1
    assert result2 == expected2
    assert result3 == expected3




