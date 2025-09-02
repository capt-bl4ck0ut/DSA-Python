if __name__ == '__main__':
    n = int(input())
    a = []
    for _ in range(n):
        a.append(int(input()))
    m = int(input())
    b = []
    for _ in range(m):
        b.append(int(input()))

    c = a + b
    c.sort()

    for x in c:
        print(x, end=' ')
