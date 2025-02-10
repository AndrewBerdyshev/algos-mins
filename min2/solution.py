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
    assert karatsuba(1234, 5678) == 7006652

def test2(capsys):
    assert karatsuba(0, 12345) == 0

def test3(capsys):
    assert karatsuba(12345, 0) == 0

def test4(capsys):
    assert karatsuba(1, 1) == 1

def test5(capsys):
    assert karatsuba(9999, 9999) == 99980001

def test6(capsys):
    assert karatsuba(123456789, 987654321) == 121932631112635269
