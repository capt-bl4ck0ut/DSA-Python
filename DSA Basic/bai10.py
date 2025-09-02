if __name__ == '__main__':
    m = int(input())
    n = int(input())

    a = [] 
    for i in range(m):
        row = []
        for j in range(n):
            x = int(input())
            row.append(x)
        a.append(row)

    total = 0
    for i in range(m):
        for j in range(n):
            total += a[i][j]
            
    print(total)
