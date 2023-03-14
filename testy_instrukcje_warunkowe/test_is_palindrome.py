from instrukcje_warunkowe.is_string_palindrome import is_palindrome


def test_is_palindrome():
    a = "racecar"
    expected = "Palindrome"

    result = is_palindrome(a)
    assert result == expected