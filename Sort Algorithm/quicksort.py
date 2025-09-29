import sys

def partion(arr, low, hight):
    pivot = arr[hight]
    i = low - 1

    for j in range(low, hight):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[hight] = arr[hight], arr[i + 1]
    return i + 1

def quick_sort(arr, low = 0, hight = None):
    if hight is None:
        hight = len(arr) - 1
    
    if low < hight:
        pivot_index = partion(arr, low, hight)
        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, hight)

def main():
    data = list(map(int, sys.stdin.read().strip().split()))
    if len(data) < 2:
        return
    n = data[0]
    arr = data[1:1+n]
    if len(arr) != n:
        return
    quick_sort(arr, 0, n-1)
    print(" ".join(map(str, arr)))

if __name__ == "__main__":
    main()
