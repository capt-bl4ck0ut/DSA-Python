import sys

def find_index(arr, x):
    left, right = 0, len(arr) - 1
    result = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == x:
            result = mid       
            right = mid - 1  
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return result

def main():
    data = list(map(int, sys.stdin.read().strip().split()))
    if len(data) < 3:
        print(-1)
        return
    n = data[0]
    arr = data[1:1+n]
    if len(arr) != n:
        print(-1)
        return
    x = data[1+n]

    print(find_index(arr, x))

if __name__ == "__main__":
    main()
