from typing import List

def counting_sort(A: List[str], index: int):
    C = [[] for _ in range(256)]
    for a in A:
        C[ord(a[index])].append(a)
    j = 0
    for i in range(256):
        for c in C[i]:
            A[j] = c
            j+=1

def lsd_radix_sort(array: List[str]):
    for i in range(len(array[0]) - 1, -1, -1):
        counting_sort(array, i)

strings = []
with open("data.txt", "r") as f:
    strings = f.readlines()

temp = strings.copy()

def quicksort_strings(strings):
    if len(strings) <= 1:
        return strings
    else:
        pivot = strings[len(strings) // 2]
        left = [x for x in strings if x < pivot]
        middle = [x for x in strings if x == pivot]
        right = [x for x in strings if x > pivot]
        return quicksort_strings(left) + middle + quicksort_strings(right)

assert quicksort_strings(strings) == sorted(strings)
temp = strings.copy()
lsd_radix_sort(temp)
assert temp == sorted(strings)

import time
def measure(delegat, args):
    start = time.time()
    delegat(*args)
    end = time.time()
    return end - start

import format_table

format_table.format_table(["time"], ["radix", "quick"], [[measure(lsd_radix_sort, [strings.copy()]), measure(quicksort_strings, [strings])]])