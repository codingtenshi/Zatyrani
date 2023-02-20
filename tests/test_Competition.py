
from Z.Competition import Competition


def test_get_full_description():
    test_object = Competition("Deep Pits", "14.02.2023", "Nieborowice")
    expected = "Deep Pits 14.02.2023 held on Nieborowice"

    result = test_object.get_full_description()
    assert result == expected

