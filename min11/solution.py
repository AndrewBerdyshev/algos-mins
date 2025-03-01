import random

def swap(A, i, j):
    A[i], A[j] = A[j], A[i]

def partition_lomute(A, low, high):
    pivot = A[random.randint(low, high)]
    i = low
    j = low
    k = high
    while j <= k:
        if A[j] < pivot:
            swap(A, i, j)
            i += 1
            j += 1
        elif A[j] == pivot:
            j += 1
        else:
            swap(A, j, k)
            k -= 1
    
    return i, k

def quicksort_lomute(A, low, high):
    if low < high:
        l, h = partition_lomute(A, low, high)
        quicksort_lomute(A, low, l-1)
        quicksort_lomute(A, h+1, high)
    return A

def partition_hoar(A, low, high):
    pivot = A[random.randint(low, high)]
    i, j = low, high
    while i <= j:
        while A[i] < pivot:
            i += 1
        while A[j] > pivot:
            j -= 1
        if i <= j:
            swap(A, i, j)
            i += 1
            j -= 1
    return i, j

def quicksort_hoar(A, low, high):
    if low < high:
        i, j = partition_hoar(A, low, high)
        if i < high:
            quicksort_hoar(A, i, high)
        if low < j:
            quicksort_hoar(A, low, j)
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

thousandTest(quicksort_lomute)
thousandTest(quicksort_hoar)
print("All tests passed!")