if __name__ == '__main__':
    n = (int)(input())
    a = []
    for i in range(n):
        a.append(int(input()))
    is_incre = True
    is_decre = True
    for i in range(1, n):
        if a[i] > a[i - 1]:
            is_incre = False
        if a[i] < a[i - 1]:
            is_decre = False
    if is_incre or is_decre:
        print("YES")
    else:
        print("NO")