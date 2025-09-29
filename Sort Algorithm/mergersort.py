import sys

def megersort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    sortLeft = megersort(left)
    sortRight = megersort(right)
    
    return meger(sortLeft, sortRight)

def meger(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def main():
    data = list(map(int, sys.stdin.read().strip().split()))
    if len(data) < 2:
        return
    n = data[0]           
    arr = data[1:1+n]      
    if len(arr) != n:
        return
    sorted_arr = megersort(arr)
    print(" ".join(map(str, sorted_arr)))

if __name__ == "__main__":
    main()
