import solution

def special_mult(a, b, c, delegat):
    res = delegat(a, b)
    assert res == c, f"Expected {a} * {b} to be {c}, but got {res}"

special_mult([[1, 2, 3], [4, 5, 6], [7, 8, 9]], \
            [[10, 11, 12], [13, 14, 15], [16, 17, 18]], \
            [[84, 90, 96], [201, 216, 231], [318, 342, 366]], solution.multiply)

def special_part(a, b, e, c):
    res = solution.get_part(a, b, e)
    assert res == c, f"Expected {c}, but got {res}"

special_part([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [0, 1], [2, 2], [[2, 3], [5, 6], [8, 9]])

def special_sum(a, b, c):
    res = solution.sum(a, b)
    assert res == c, f"Expected {a} + {b} to be {c}, but got {res}"

special_sum([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]], \
            [[11, 13, 15], [17, 19, 21], [23, 25, 27]])

def special_mult2(a, b, delegat1, delegat2):
    res1 = delegat1(a, b)
    res2 = delegat2(a, b)
    assert res1 == res2, f"Expected {res1}, but got {res2}"

special_mult2([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]],
[[17, 18, 19, 20], [21, 22, 23, 24], [25, 26, 27, 28], [29, 30, 31, 32]],
solution.multiply,
solution.recursive_multiply)

special_mult2([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]],
[[17, 18, 19, 20], [21, 22, 23, 24], [25, 26, 27, 28], [29, 30, 31, 32]],
solution.multiply,
solution.strassen)

print("All tests passed!")