from instrukcje_warunkowe.is_yaer_is_leap_or_not import get_leap_year


def test_get_leap_year():
    year1 = 2024
    year2 = 2023
    expected1 = "Leap year"
    expected2 = "Not leap year"

    result1 = get_leap_year(year1)
    result2 = get_leap_year(year2)
    assert result1 == expected1
    assert result2 == expected2
