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
    strings = [x.strip() for x in strings]

temp = strings.copy()

def bubble_sort_strings(strings):
    n = len(strings)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if strings[j] > strings[j + 1]:
                strings[j], strings[j + 1] = strings[j + 1], strings[j]
                swapped = True
        if not swapped:
            break
    return strings

# assert bubble_sort_strings(strings) == sorted(strings)
# temp = strings.copy()
# lsd_radix_sort(temp)
# assert temp == sorted(strings)

import time
def measure(delegat, args):
    start = time.time()
    delegat(*args)
    end = time.time()
    return end - start

import format_table

format_table.format_table(["time"], ["radix", "bubble"], [[measure(lsd_radix_sort, [strings.copy()]), measure(bubble_sort_strings, [strings])]])