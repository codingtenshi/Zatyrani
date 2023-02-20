
from Z.Initiatives import Initiatives


def test_get_full_description():
    test_object = Initiatives("Slow running -", "running for everyone", "Tuesday", "7.00 p.m", "zadupie")
    expected = "Slow running - running for everyone held on Tuesday at 7.00 p.m"

    result = test_object.get_full_description()
    assert result == expected