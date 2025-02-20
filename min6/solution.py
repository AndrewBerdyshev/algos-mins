def merge(left, right, res):
    lsize, rsize = len(left), len(right)
    n = len(res)
    assert n == lsize + rsize
    i, j, k = 0, 0, 0
    while k < n and i < lsize and j < rsize:
        if left[i] < right[j]:
            res[k] = left[i]
            k+=1
            i+=1
        else:
            res[k] = right[j]
            k+=1
            j+=1

    while i < lsize:
        res[k] = left[i]
        k+=1
        i+=1
    while j < rsize:
        res[k] = right[j]
        k+=1
        j+=1

def merge_sort(array):
    if len(array) <= 1:
        return
    middle = len(array) // 2
    left = array[:middle]
    right = array[middle:]
    
    merge_sort(left)
    merge_sort(right)
    
    buffer = [0]*len(array)
    merge(left, right, buffer)
    
    for i in range(len(array)):
        array[i] = buffer[i]


lololo = [1, 2, 3, 7, 6, 5, 3, 4]
merge_sort(lololo)
print(lololo)
