from lomuteandhoar import partition_lomuto
import random
from typing import *

def kth_recursive(array: List[int], k: int, low: int, high: int) -> int:
    if len(array) == 1: return array[0]

    p, _ = partition_lomuto(array, low, high)

    if p + 1 == k:
        return array[p]
    elif p + 1 > k:
        return kth(array[:p], k)
    else:
        return kth(array[p + 1:], k - p - 1)

def kth(array: List[int], k: int) -> int:
    return kth_recursive(array, k, 0, len(array) - 1)

def test(unsorted):
    python_sorted = sorted(unsorted.copy())
    k = random.randint(1, len(unsorted))
    kt = kth(unsorted.copy(), k)
    assert python_sorted[k-1] == kt, f"Given {unsorted} - {k}\nExpected {python_sorted[k-1]} but got {kt}"

def thousandTest():
    for i in range(1, 1000):
        unsorted = [random.randint(-20, 20) for __ in range(i)]
        test(unsorted)

thousandTest()
print("All tests passed!")