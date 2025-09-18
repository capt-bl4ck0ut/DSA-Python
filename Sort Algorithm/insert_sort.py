import sys
def insert_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def main():
    data = list(map(int, sys.stdin.read().strip().split()))
    if len(data) < 2:
        return
    n = data[0]          
    arr = data[1:1+n]       
    if len(arr) != n:
        return
    insert_sort(arr)
    for num in arr:
        print(num, end=" ")

if __name__ == "__main__":
    main()


