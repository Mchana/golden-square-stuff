from lib.report_length import *

def test_length():
    result = report_length("12")
    assert result == "This string was 2 characters long."

