from p5 import simple_interest

def test_simple_interest():
    assert simple_interest(10000, 5, 2) == 1000

def test_simple_interest_2():
    assert simple_interest(5000, 10, 2) == 1000

def test_simple_interest_3():
    assert simple_interest(2000, 5, 3) == 300