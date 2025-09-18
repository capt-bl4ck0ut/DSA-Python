import sys

def find_subarray(arr, s):
    n = len(arr)
    left = 0
    current_sum = 0
    for right in range(n):
        current_sum += arr[right]
        while current_sum > s and left <= right:
            current_sum -= arr[left]
            left += 1
        if current_sum == s:
            return arr[left:right+1]
    return None

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
    s = data[1+n]

    res = find_subarray(arr, s)
    if res is None:
        print(-1)
    else:
        print(" ".join(map(str, res)), end=" ")

if __name__ == "__main__":
    main()
