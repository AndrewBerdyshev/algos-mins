def division(a: int, b: int) -> str:
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
    
    if not c:
        c = "0"
    return f"{c.lstrip('0')} and {r}"

print(division(123456789, 12345))

# O(m*n) операций тк у нас два цикла (первый на n итераций, второй на m итераций(максимально))
# в худшем случае мы будем для каждой цифры делителя искать от 1 до m чтобы поделить. O(m*n)
# в лучшем количество итераций второго цикла будет минимальным(1) и количество итераций будет O(n)