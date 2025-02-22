def karatsuba(x: int, y: int) -> int:
    x_len = len(str(x))
    y_len = len(str(y))

    if min(x_len, y_len) <= 16:
        return x * y

    maxlen = max(x_len, y_len)
    halflen = maxlen // 2

    a = x // (10 ** halflen)
    b = x % (10 ** halflen)
    c = y // (10 ** halflen)
    d = y % (10 ** halflen)

    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    abcd = karatsuba(a + b, c + d)

    return ac * (10 ** (2 * halflen)) + (abcd - ac - bd) * (10 ** halflen) + bd

import random

def python_mult(a: int, b: int) -> int:
    return a*b

def test_mult():
    for _ in range(100000):
        a = random.randint(1, 10**20)
        b = random.randint(1, 10**20)
        
        res1 = karatsuba(a, b)
        res2 = python_mult(a, b)
        
        assert res1 == res2, f"Test failed for a={a}, b={b}: expected {res2}, got {res1}"
    
    print("All tests passed!")

test_mult()

#hardcoded
def special(a: int, b: int) -> None:
    assert karatsuba(a, b) == a * b

def test1(capsys):
    special(1, 2457234756234785678432567834)

def test3(capsys):
    special(12, 2457234756234785678432567834)

def test4(capsys):
    special(36345634563456456456346, 2457234756234785678432567834)