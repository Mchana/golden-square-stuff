from lib.greet import *

def test greet_gary():
    result = greet(Gary)
    assert result == "Hello, Gary!"
