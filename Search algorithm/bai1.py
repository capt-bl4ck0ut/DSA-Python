def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    arr = arr[:n]
    x = int(input())
    result = linear_search(arr, x)
    print(result)
