import random
import format_table
import solution
import time
import numpy as np

def get_random_matrixnn(n):
    return np.array([[random.randint(0, 10000) for _ in range(n)] for __ in range(n)])

def get_2_random_matrixnn(n):
    return get_random_matrixnn(n), get_random_matrixnn(n)

def measure(delegat, args):
    start = time.time()
    delegat(*args)
    end = time.time()
    return end - start

benchmarks = []
algos_temp = [solution.multiply, solution.recursive_multiply, solution.strassen]
algos = ["classic", "recursive", "strassen"]
results = []
for algo in algos_temp:
    temp = []
    for i in range(1, 8):
        n = 2**i
        temp.append(measure(algo, get_2_random_matrixnn(n)))
        if f"{n}x{n}" not in benchmarks:
            benchmarks.append(f"{n}x{n}")
    results.append(temp)
    
format_table.format_table(benchmarks, algos, results)
