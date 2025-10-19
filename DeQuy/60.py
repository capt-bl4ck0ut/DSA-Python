import sys

def tohop(n, k, start, current):
    if len(current) == k:
        print(''.join(map(str, current)), end=' ')
        return
    for i in range(start, n + 1):
        current.append(i)
        tohop(n, k, i + 1, current)
        current.pop()
def main():
    data = sys.stdin.read().strip().split()
    if len(data) != 2:
        return
    n, k = map(int, data)
    tohop(n, k, 1, [])

if __name__ == "__main__":
    main()
