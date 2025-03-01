from lomuteandhoar import *

def partition_lomuto_branchfree(A, first, last):
    assert first < last

    if last + 1 - first < 2:
        return first

    if first >= len(A) or last >= len(A) or first < 0 or last < 0:
      return first

    if A[first] > A[last]:
        swap(A, first, last)

    pivot_pos = first
    pivot = A[first]

    first += 1
    while first <= last and A[first] < pivot:
        first += 1

    for read in range(first + 1, last):
        x = A[read]
        smaller = -(x < pivot)
        delta = smaller & (read - first)
        A[first + delta] = A[first]
        A[read - delta] = x
        first -= smaller

    first -= 1
    A[pivot_pos] = A[first]
    A[first] = pivot

    return first

def quicksort_lomuto_branchfree(A, low, high):
    if low < high:
        pivot = partition_lomuto_branchfree(A, low, high)
        quicksort_lomuto_branchfree(A, pivot+1, high)
        quicksort_lomuto_branchfree(A, low, pivot)
    return A

def quicksort(A, delegat):
    return delegat(A, 0, len(A)-1)

def test(unsorted, delegat):
    python_sorted = sorted(unsorted.copy())
    my_sorted = quicksort(unsorted.copy(), delegat)
    assert python_sorted == my_sorted, f"Given {unsorted}\nExpected {python_sorted} but got {my_sorted}"

def thousandTest(delegat):
    for i in range(0, 1000):
        unsorted = [random.randint(-20, 20) for __ in range(i)]
        test(unsorted, delegat)

# thousandTest(quicksort_lomuto_branchfree)
# print("All tests passed!")

import time
def measure(delegat, args):
    start = time.time()
    delegat(*args)
    end = time.time()
    return end - start

import format_table
format_table.format_table(["thousandTest"], ["lomuto", "hoare", "lomuto branchfree"], 
                          [[measure(thousandTest, [quicksort_lomuto]), measure(thousandTest, [quicksort_hoare]), measure(thousandTest, [quicksort_lomuto_branchfree])]])