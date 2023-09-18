from lib.greet import greet

def test_greet ():
    result = greet("Gary")
    assert result == "Hello, Gary!"
