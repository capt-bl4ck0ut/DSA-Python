import sys

def search(arr):
    s = set(arr)
    x = 0
    while True:
        if x not in s:
            return x
        x += 1

def main():
    data = list(map(int, sys.stdin.read().strip().split()))
    if len(data) < 2:
        return
    n = data[0]
    arr = data[1:1+n]
    if len(arr) != n:
        return
    print(search(arr))

if __name__ == "__main__":
    main()