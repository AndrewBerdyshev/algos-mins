from typing import List

def swap(arr:List[int], a, b):
    c = arr[b]
    arr[b] = arr[a]
    arr[a] = c

def sort_dutch_flag(arr: List[int]):
    zero = 0
    two = len(arr) - 1
    i = 0
    while i <= two:
        if arr[i] == 0:
            swap(arr, i, zero)
            zero += 1
            i += 1
        elif arr[i] == 1:
            i += 1
        else:
            swap(arr, i, two)
            two -= 1

temp = [2,0,2,1,1,0]
sort_dutch_flag(temp)
assert temp == [0,0,1,1,2,2]