import pytest
from lib.password_checker import *

def test_valid():
    passwordchecker = PasswordChecker()
    result = passwordchecker.check("validpass")
    assert result == True

def test_invalid():
    passwordchecker = PasswordChecker()
    with pytest.raises(Exception) as e:
        error_message = passwordchecker.check("invalid")
        assert error_message == "Invalid password, must be 8+ characters."
