def merge(array, start, mid, end):
    left = start
    right = mid + 1
    while left <= mid and right <= end:
        if array[left] <= array[right]:
            left += 1
        else:
            preserve = array[right]
            for i in range(right, left, -1):
                array[i] = array[i - 1]
            array[left] = preserve
            left += 1
            mid += 1
            right += 1

def merge_sort_args(array, start, end):
    if start < end:
        mid = (start + end) // 2
        merge_sort_args(array, start, mid)
        merge_sort_args(array, mid + 1, end)
        merge(array, start, mid, end)
    
def merge_sort(array):
    merge_sort_args(array, 0, len(array) - 1)

import random
for _ in range(1000):
    unsorted = [random.randint(-20, 20) for __ in range(random.randint(1, 20))]
    python_sorted = sorted(unsorted.copy())
    my_sorted = unsorted.copy()
    merge_sort(my_sorted)
    assert python_sorted == my_sorted, f"Expected {python_sorted} but got {my_sorted}"
print("All tests passed!")