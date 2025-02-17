import random

def python_division(a: int, b: int) -> tuple:
    return (int(a / b), a % b)

def division(a: int, b: int) -> tuple:
    a_str = str(a) # n
    b_str = str(b) # m
    c = ""
    r = ""

    for digit in a_str:
        r += digit

        mx = 0
        while (mx + 1) * b <= int(r):
            mx += 1
        
        c += str(mx)
        r = str(int(r) - mx*b)
    c = c.lstrip('0')
    return (0 if not c else int(c), int(r))

def test_division():
    for _ in range(100):
        a = random.randint(1, 10**9)
        b = random.randint(1, 10**9)
        
        res11, res12 = division(a, b)
        res21, res22 = python_division(a, b)
        
        assert res11 == res21 and res12 == res22, f"Test failed for a={a}, b={b}: expected {res21}.{res22}, got {res11}.{res12}"
    
    print("All tests passed!")

test_division()

# O(m*n) операций тк у нас два цикла (первый на n итераций, второй на m итераций(максимально))
# в худшем случае мы будем для каждой цифры делителя искать от 1 до m чтобы поделить. O(m*n)
# в лучшем количество итераций второго цикла будет минимальным(1) и количество итераций будет O(n)