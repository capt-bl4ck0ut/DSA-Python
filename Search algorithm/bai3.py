def count(a, x):
    count = 0
    for i in range(1, len(a) - 1):
        if a[i] == x:
            count += 1
    return count

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    x = int(input())

    result = count(arr, x)
    print(result)
