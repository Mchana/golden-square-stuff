from lib.counter import *

def test_counter_5():
    counter = Counter()
    counter.add(5)
    result = counter.report()
    assert result == "Counted to 5 so far."

def test_counter_nothing():
    counter = Counter()
    result = counter.report()
    assert result == "Counted to 0 so far."

def test_counter_4_then_9():
    counter = Counter()
    counter.add(4)
    counter.add(9)
    result = counter.report()
    assert result == "Counted to 13 so far."