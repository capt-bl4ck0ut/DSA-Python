import math
import sys

def is_square(n):
    if n < 0:
        return False
    r = int(math.sqrt(n))
    return r * r == n

def partition(arr, low, high):
    pivot = arr[(low + high) // 2]
    i, j = low, high
    while i <= j:
        while arr[i] < pivot:
            i += 1
        while arr[j] > pivot:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
    return i, j

def quick_sort(arr, low, high):
    if low < high:
        i, j = partition(arr, low, high)
        if low < j:
            quick_sort(arr, low, j)
        if i < high:
            quick_sort(arr, i, high)

def print_array(arr):
    if not arr:
        print("NULL")
        return
    print(arr[0], end=" ")
    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1]:
            print(arr[i], end=" ")

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    if data[0].isdigit() and len(data) - 1 == int(data[0]):
        arr = list(map(int, data[1:]))
    else:
        arr = list(map(int, data))

    b = [x for x in arr if is_square(x)]
    if not b:
        print("NULL")
        return

    quick_sort(b, 0, len(b) - 1)
    print_array(b)

if __name__ == "__main__":
    main()
