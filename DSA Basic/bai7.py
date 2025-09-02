if __name__ == '__main__':
    n = int(input())
    a = []
    for i in range(n):
        a.append(int(input()))
    for i in sorted(set(a)):
            print(f"{i} - {a.count(i)};", end=' ')