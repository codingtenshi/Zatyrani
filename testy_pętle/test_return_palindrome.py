from pętle.return_palindrome import get_palindrome


def test_get_palindrome():
    palindrom = "racecar"
    expected = "Is palindrome"

    result = get_palindrome(palindrom)
    assert result == expected


def test_get_palindrome():
    palindrom = "nos"
    expected = "Is not palindrome"

    result = get_palindrome(palindrom)
    assert result == expected
