from instrukcje_warunkowe.is_string_empty_or_not import get_empty_string


def test_get_empty_string():
    a = ""
    expected = ""

    result = get_empty_string(a)
    assert result == expected