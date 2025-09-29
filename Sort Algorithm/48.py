import sys

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

def count_fre(arr):
    if not arr:
        return "" 
    quick_sort(arr)  
    parts = []
    count = 1
    for i in range(1, len(arr)):
        if arr[i] == arr[i - 1]:
            count += 1
        else:
            parts.append(f"{arr[i - 1]} {count}")
            count = 1
    parts.append(f"{arr[-1]} {count}")  
    return "; ".join(parts) + "; "

def main():
    data = list(map(int, sys.stdin.read().strip().split()))
    if not data:
        return
    n = data[0]
    arr = data[1:1 + n]
    print(count_fre(arr))

if __name__ == "__main__":
    main()
