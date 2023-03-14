from instrukcje_warunkowe.is_string_empty_or_not import get_empty_string


def test_get_empty_string():
    a = ""
    b = "jhhhjhj"
    expected1 = "Empty"
    expected2 = "Not empty"

    result1 = get_empty_string(a)
    result2 = get_empty_string(b)
    assert result1 == expected1
    assert result2 == expected2