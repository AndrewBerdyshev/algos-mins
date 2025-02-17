def karatsuba(x: int, y: int) -> int:
    x_str = str(x)
    y_str = str(y)

    if len(x_str) == 1 or len(y_str) == 1:
        return x * y

    maxlen = max(len(x_str), len(y_str))
    halflen = maxlen // 2

    a = x // (10 ** halflen)
    b = x % (10 ** halflen)
    c = y // (10 ** halflen)
    d = y % (10 ** halflen)

    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    abcd = karatsuba(a + b, c + d)

    return ac * (10 ** (2 * halflen)) + (abcd - ac - bd) * (10 ** halflen) + bd

def test1(capsys):
    assert karatsuba(1234, 5678) == 1234 * 5678

def test2(capsys):
    assert karatsuba(0, 12345) == 0

def test3(capsys):
    assert karatsuba(12345, 0) == 0

def test4(capsys):
    assert karatsuba(1, 1) == 1

def test5(capsys):
    assert karatsuba(9999, 9999) == 9999 * 9999

def test6(capsys):
    assert karatsuba(123456789, 987654321) == 123456789 * 987654321

def test7(capsys):
    assert karatsuba(123456789, 98) == 123456789 * 98

def test8(capsys):
    assert karatsuba(98, 1234567892323) == 98 * 1234567892323

def test9(capsys):
    assert karatsuba(9, 123456789232112121212123) == 9 * 123456789232112121212123

# import random

# def python_mult(a: int, b: int) -> int:
#     return a*b

# def test_mult():
#     for _ in range(1000):
#         a = random.randint(1, 10**9)
#         b = random.randint(1, 10**9)
        
#         res1 = karatsuba(a, b)
#         res2 = python_mult(a, b)
        
#         assert res1 == res2, f"Test failed for a={a}, b={b}: expected {res2}, got {res1}"
    
#     print("All tests passed!")

# test_mult()