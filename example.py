def add(a, b):
    return a + b

def test_add():
    assert add(2, 3) == 5
    assert add("hello", " world") == "hello world"

def sqrt(x):
    return x**(1./2)

def test_sqrt():
    assert round(sqrt(3.0)**2) == 9

def test_joke():
    assert "hello world" == "hello world"
