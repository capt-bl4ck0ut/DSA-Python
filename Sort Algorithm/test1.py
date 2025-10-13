import sys

def mergersort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    sortLeft = mergersort(left)
    sortRight = mergersort(right)

    return merger(sortLeft, sortRight)

def merger(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(i)
            i += 1
        else:
            result.append(j)
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
