import sys

def min_initial_people(arr, k):
    arr.sort()
    count = 1  
    for i in range(1, len(arr)):
        if arr[i] - arr[i-1] > k:
            count += 1
    return count

def main():
    data = list(map(int, sys.stdin.read().strip().split()))
    n = data[0]
    arr = data[1:1+n]
    k = data[1+n]
    print(min_initial_people(arr, k))

if __name__ == "__main__":
    main()
