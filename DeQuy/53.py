import sys

def power(a, b):
    if b == 0:
        return 1
    else:
        return a * power(a, b - 1)

def main():
    data = sys.stdin.read().strip().split()
    if len(data) != 2:
        return
    a, b = map(int, data)
    print(power(a, b))

if __name__ == "__main__":
    main()
