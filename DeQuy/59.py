import sys

def hoanvi(n, current, used):
    if len(current) == n:
        print(''.join(map(str, current)), end=' ')
        return
    for i in range(1, n + 1):
        if not used[i]:
            used[i] = True
            current.append(i)
            hoanvi(n, current, used)
            current.pop()
            used[i] = False

def main():
    data = sys.stdin.read().strip()
    if not data:
        return
    n = int(data)
    used = [False] * (n + 1)
    hoanvi(n, [], used)

if __name__ == "__main__":
    main()
