if __name__ == '__main__':
    n = (int)(input())
    a = []
    for i in range(n):
        a.append((int)(input()))
    Sum = 0
    for i in range(n):
        Sum += a[i]
    print(Sum)