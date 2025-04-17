import numpy as np

def get_zero_matrixnn(n):
    return  [[0 for _ in range(n)] for __ in range(n)]

def multiply(a, b):
    return np.matmul(a, b)

def get_part(matrix, start, end):
    return matrix[start[0]:end[0]+1, start[1]:end[1]+1]

def set_part(part, start, end, matrix):
    matrix[start[0]:end[0]+1, start[1]:end[1]+1] = part

def recursive_multiply(a, b): # 2
    ln = len(a)
    if ln == 2:
        return multiply(a, b)
    n = ln // 2
    m = ln - 1

    A = get_part(a, [0, 0], [n-1, n-1])
    B = get_part(a, [0, n], [n-1, m])
    C = get_part(a, [n, 0], [m, n-1])
    D = get_part(a, [n, n], [m, m])
    E = get_part(b, [0, 0], [n-1, n-1])
    F = get_part(b, [0, n], [n-1, m])
    G = get_part(b, [n, 0], [m, n-1])
    H = get_part(b, [n, n], [m, m])

    res = np.zeros((ln, ln))
    set_part(multiply(A, E) + multiply(B, G), [0, 0], [n-1, n-1], res)
    set_part(multiply(A, F) + multiply(B, H), [0, n], [n-1, m], res)
    set_part(multiply(C, E) + multiply(D, G), [n, 0], [m, n-1], res)
    set_part(multiply(C, F) + multiply(D, H), [n, n], [m, m], res)
    return res

def strassen(a, b): # 3
    ln = len(a)
    if ln == 2:
        return multiply(a, b)
    n = ln // 2
    m = ln - 1

    A = get_part(a, [0, 0], [n-1, n-1])
    B = get_part(a, [0, n], [n-1, m])
    C = get_part(a, [n, 0], [m, n-1])
    D = get_part(a, [n, n], [m, m])
    E = get_part(b, [0, 0], [n-1, n-1])
    F = get_part(b, [0, n], [n-1, m])
    G = get_part(b, [n, 0], [m, n-1])
    H = get_part(b, [n, n], [m, m])

    P1 = strassen(A, F-H)
    P2 = strassen(A+B, H)
    P3 = strassen(C+D, E)
    P4 = strassen(D, G-E)
    P5 = strassen(A+D, E+H)
    P6 = strassen(B-D, G+H)
    P7 = strassen(A-C, E+F)

    Q1 = P5+P4-P2+P6
    Q2 = P1+P2
    Q3 = P3+P4
    Q4 = P1+P5-P3-P7

    res = np.zeros((ln, ln))
    set_part(Q1, [0, 0], [n-1, n-1], res)
    set_part(Q2, [0, n], [n-1, m], res)
    set_part(Q3, [n, 0], [m, n-1], res)
    set_part(Q4, [n, n], [m, m], res)
    return res