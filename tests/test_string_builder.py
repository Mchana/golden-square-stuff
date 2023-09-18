from lib.string_builder import *

def test_nothing_len():
    builder = StringBuilder()
    result = builder.size()
    assert result == 0

def test_nothing_input():
    builder = StringBuilder()
    result = builder.output()
    assert result == ''

def test_one_input():
    builder = StringBuilder()
    builder.add("buddy")
    result =  builder.output()
    assert result == "buddy"

def test_one_input_len():
    builder = StringBuilder()
    builder.add("buddy")
    result = builder.size()
    assert result == 5

def test_add_strings():
    builder = StringBuilder()
    builder.add("Morning ")
    builder.add("buddy!")
    result = builder.output()
    assert result == "Morning buddy!"
