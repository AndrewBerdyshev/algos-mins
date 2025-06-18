from typing import List

def swap(a: List, i: int, j: int):
    c = a[i]
    a[i] = a[j]
    a[j] = c

def implace_linear_sort(array: List[int], sorted1: tuple[int, int], sorted2: tuple[int, int], buffer: tuple[int, int]):
    sorted1_len = sorted1[1] - sorted1[0] + 1
    sorted2_len = sorted2[1] - sorted2[0] + 1
    buffer_len = buffer[1] - buffer[0] + 1
    assert buffer_len == sorted1_len + sorted2_len, f"{array}\n{sorted1}\n{sorted2}\n{buffer}"
    i, j, k = sorted1[0], sorted2[0], buffer[0]
    while i <= sorted1[1] and j <= sorted2[1] and k <= buffer[1]:
        if array[i] < array[j]:
            swap(array, k, i)
            k+=1
            i+=1
        else:
            swap(array, k, j)
            k+=1
            j+=1

    while i <= sorted1[1]:
        swap(array, k, i)
        k+=1
        i+=1
    while j <= sorted2[1]:
        swap(array, k, j)
        k+=1
        j+=1

def part_len(a: tuple[int, int]):
    return a[1] - a[0] + 1

# palces first element in it's right place
def insert(array, slice):
    for i in range(slice[0], slice[1]):
        if array[i] > array[i+1]:
            swap(array, i, i+1)

def merge(array: List[int], slice: tuple[int, int]):
    ln = part_len(slice)
    if ln <= 1:
        return
    if ln == 2:
        if array[slice[0]] > array[slice[1]]:
            swap(array, slice[0], slice[1])
        return
    if ln == 3:
        merge(array, (slice[0]+1, slice[1]))
        insert(array, slice)
        return
    
    quarter = ln // 4
    left = slice[0], slice[0] + quarter - 1
    right = slice[0] + quarter * 2, slice[1]
    buffer = slice[0] + quarter, slice[1]

    merge(array, left)
    merge(array, right)
    implace_linear_sort(array, left, right, buffer)

    lnq = quarter // 2
    isshift = False

    while True:
        # in case unsorted part is odd. so we shift it by one, 
        # making it even appropriately making subsequent parts equal in length. 
        # the preserved element will be inserted later

        temp = part_len((left[0], buffer[0]-1))
        if temp % 2 != 0:
            left = (left[0]+1, left[1])
            isshift = True
            
        left = left[0], left[0] + lnq - 1
        right = buffer[0], buffer[1]
        buffer = left[0] + lnq, buffer[1]   

        if part_len(left) == 0:
            insert(array, slice)
            return
        
        merge(array, left)
        implace_linear_sort(array, left, right, buffer)
        if isshift:
            # Let's go back to the moment before we shifted. 
            # you might think that insert will ruin everything, 
            # but in the worst case, a sorted element from the buffer may get into the "unsorted part", 
            # which will not spoil the situation.
            insert(array, slice)
            left = (left[0]-1, left[1])
            isshift = False
            lnq = (lnq + 1) // 2
        else:
            lnq //= 2
    
def merge_sort(array: List[int]):
    merge(array, (0, len(array)-1))

import random

def test(unsorted):
    python_sorted = sorted(unsorted.copy())
    my_sorted = unsorted.copy()
    merge_sort(my_sorted)
    assert python_sorted == my_sorted, f"Given {unsorted}\nExpected {python_sorted} but got {my_sorted}"

test([13, 99, 51, 28, 91, 30, 34, 111, 56, 22, 37, 12, 1, 5, 15, 60])
test([-9, -13, -11, -15, 3, -12, -7, -19, -11, 16, -16, 1, -15, -8, -1])
test([-3, 2, 0, 1, 4, 7, 5])
test([13, 99, 51, 28, 91, 30, 34, 111, 56, 22, 37, 12])
test([5, 11, -16, -4, -15, 13, -2, -11, -12, -20, 18, -11, -1, -7, 4, 19, 11, -15, -9, 18])
test([-19, 8, 10, -20, -18, -17, -16, -15, -15, -11, -6, -5, -3, -2, -1, 1, 8, 8, 8, 9, 10, 12, 12, 14, 15, 16, 18, 19])
print("Specialized tests passed!")

for i in range(1000):
    unsorted = [random.randint(-20, 20) for __ in range(i)]
    test(unsorted)
print("All tests passed!")