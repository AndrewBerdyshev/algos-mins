import random

def swap(A, i, j):
    A[i], A[j] = A[j], A[i]

def partition_lomuto(A, low, high):
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

def quicksort_lomuto(A, low, high):
    if low < high:
        l, h = partition_lomuto(A, low, high)
        quicksort_lomuto(A, low, l-1)
        quicksort_lomuto(A, h+1, high)
    return A

def partition_hoare(A, low, high):
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

def quicksort_hoare(A, low, high):
    if low < high:
        i, j = partition_hoare(A, low, high)
        if i < high:
            quicksort_hoare(A, i, high)
        if low < j:
            quicksort_hoare(A, low, j)
    return A