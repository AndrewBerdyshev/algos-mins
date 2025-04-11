from typing import List

def counting_sort(A: List[str], index: int):
    counts = [0] * 256
    for s in A:
        counts[ord(s[index])] += 1
    prefix_sums = [0] * 256
    for i in range(1, 256):
        prefix_sums[i] = prefix_sums[i-1] + counts[i-1]
    temp = [''] * len(A)
    for s in A:
        char_code = ord(s[index])
        temp[prefix_sums[char_code]] = s
        prefix_sums[char_code] += 1
    A[:] = temp

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