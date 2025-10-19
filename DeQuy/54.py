import sys

def UCLN(a, b):
    if b == 0:
        return a
    else:
        return UCLN(b, a%b)
    
def main():
    data = sys.stdin.read().strip().split()
    if len(data) != 2:
        return
    a, b = map(int, data)
    print(UCLN(a, b))

if __name__ == "__main__":
    main()

