import random
import format_table
import solution
import time

def get_random_matrixnn(n):
    return [[random.randint(0, 10000) for _ in range(n)] for __ in range(n)]

def get_2_random_matrixnn(n):
    return get_random_matrixnn(n), get_random_matrixnn(n)

def measure(delegat, args):
    start = time.time()
    delegat(*args)
    end = time.time()
    return end - start

# Is that the name?
def stress_test(delegat, args):
    results = []
    for _ in range(10):
        for i in args:
            results.append(measure(delegat, i))
    return min(results), max(results)

# a point, when strassen is better than recursive
def get_point():
    N = 2
    while True:
        A, B = get_2_random_matrixnn(N) 
        time1 = measure(solution.recursive_multiply, [A, B])
        time2 = measure(solution.strassen, [A, B])
        if time2 > time1 and time1 and time2:
            return N
        N*=2

def benchmark(algos, args):
    best = []
    worst = []
    for i in algos:
        bst, wrst = stress_test(i, args)
        best.append(bst)
        worst.append(wrst)
    return [best, worst]

format_table.format_table(["best", "worst"], ["classic", "recursive", "strassen"], benchmark([solution.multiply, solution.recursive_multiply, solution.strassen], 
           [get_2_random_matrixnn(2**random.randint(4, 6)) for _ in range(10)]))

print(f"At point {get_point()} strassen is better than recursive")