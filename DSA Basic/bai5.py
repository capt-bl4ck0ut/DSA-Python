import math

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

if __name__ == '__main__':
    n = int(input())
    a = []
    for i in range(n):
        a.append(int(input()))
    
    for i in a:
        if is_prime(i):
            print(i, end=' ') 
