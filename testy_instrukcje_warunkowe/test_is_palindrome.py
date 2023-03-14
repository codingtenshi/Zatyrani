from instrukcje_warunkowe.is_string_palindrome import is_palindrome


def test_is_palindrome():
    a = "racecar"
    b = "peace"
    expected1 = "Palindrome"
    expected2 = "Not palindrome"

    result1 = is_palindrome(a)
    result2 = is_palindrome(b)
    assert result1 == expected1
    assert result2 == expected2