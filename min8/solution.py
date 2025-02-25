def get_zero_matrixnn(n):
    return  [[0 for _ in range(n)] for __ in range(n)]

def multiply(a, b): # 1
    ln = len(a)
    res = get_zero_matrixnn(ln)
    for i in range(ln):
        for j in range(ln):
            for k in range(ln):
                res[i][j] += a[i][k] * b[k][j]
    return res

def sum(a, b):
    ln = len(a)
    res = get_zero_matrixnn(ln)
    for i in range(ln):
        for j in range(ln):
            res[i][j] = a[i][j] + b[i][j]
    return res

def get_part(a, begin, end):
    res = []
    for i in range(begin[0], end[0]+1):
        temp = []
        for j in range(begin[1], end[1]+1):
            temp.append(a[i][j])
        res.append(temp)
    return res

def set_part(a, begin, end, res):
    k = 0
    l = 0
    for i in range(begin[0], end[0]+1):
        for j in range(begin[1], end[1]+1):
            #print(i, j, k, l, begin, end, a, res)
            res[i][j] = a[k][l]
            l+=1
        l=0
        k+=1
    k=0

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

    res = get_zero_matrixnn(ln)
    set_part(sum(multiply(A, E), multiply(B, G)), [0, 0], [n-1, n-1], res)
    set_part(sum(multiply(A, F), multiply(B, H)), [0, n], [n-1, m], res)
    set_part(sum(multiply(C, E), multiply(D, G)), [n, 0], [m, n-1], res)
    set_part(sum(multiply(C, F), multiply(D, H)), [n, n], [m, m], res)
    return res

# print(recursive_multiply(
# [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]],
# [[17, 18, 19, 20], [21, 22, 23, 24], [25, 26, 27, 28], [29, 30, 31, 32]]))

def neg(a):
    res = get_zero_matrixnn(len(a))
    for i in range(len(a)):
        for j in range(len(a[0])):
            res[i][j] = -a[i][j]
    return res

def strassen(a, b):
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

    P1 = strassen(A, sum(F, neg(H)))
    P2 = strassen(sum(A, B), H)
    P3 = strassen(sum(C, D), E)
    P4 = strassen(D, sum(G, neg(E)))
    P5 = strassen(sum(A, D), sum(E, H))
    P6 = strassen(sum(B, neg(D)), sum(G, H))
    P7 = strassen(sum(A, neg(C)), sum(E, F))

    Q1 = sum(sum(sum(P5, P4), neg(P2)), P6)
    Q2 = sum(P1, P2)
    Q3 = sum(P3, P4)
    Q4 = sum(sum(sum(P1, P5), neg(P3)), neg(P7))

    res = get_zero_matrixnn(ln)
    set_part(Q1, [0, 0], [n-1, n-1], res)
    set_part(Q2, [0, n], [n-1, m], res)
    set_part(Q3, [n, 0], [m, n-1], res)
    set_part(Q4, [n, n], [m, m], res)
    return res