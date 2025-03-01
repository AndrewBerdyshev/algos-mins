from typing import List
import random

def quicksort(array: List[int]):
    if len(array) <= 1:
        return array
    N = len(array)
    pivot = array[random.randint(int(N/4), N-1)]
    left = [x for x in array if x < pivot]
    middle = [x for x in array if x == pivot]
    right = [x for x in array if x > pivot]
    return quicksort(left) + middle + quicksort(right)

def test(unsorted):
    python_sorted = sorted(unsorted.copy())
    my_sorted = quicksort(unsorted.copy())
    assert python_sorted == my_sorted, f"Given {unsorted}\nExpected {python_sorted} but got {my_sorted}"

for i in range(1000):
    unsorted = [random.randint(-20, 20) for __ in range(i)]
    test(unsorted)
print("All tests passed!")