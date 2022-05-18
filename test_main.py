import pytest
from SSNValidator import validateSSN

@pytest.mark.parametrize(
    "SSN, expected",
    [
        ("456-98-8974", True),
        ("000-89-7321", False),
        ("456-78932-1", False),
        ("676-44-0000", False),
        ("666-88-8999", False),
        ("906-88-8999", False),
        ("667-00-8999", False),
        ("766-81-8999", True),
        ("676-44-8999", True)
    ]
)

def test_SSN(SSN, expected):
    assert validateSSN(SSN) == expected