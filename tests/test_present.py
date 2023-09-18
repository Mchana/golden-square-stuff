import pytest 
from lib.present import *

def test_none():
    present = Present()
    with pytest.raises(Exception) as e:
        present.unwrap()
    error_message = str(e.value)
    assert error_message == "No contents have been wrapped."

def test_some():
    present = Present()
    contents = "bagel"
    present.wrap(contents)
    with pytest.raises(Exception) as e:
        present.wrap("mould")
    error_message = str(e.value)
    assert error_message == "A contents has already been wrapped."