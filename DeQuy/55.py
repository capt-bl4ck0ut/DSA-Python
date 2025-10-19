import sys

def fibonaci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonaci(n - 1) + fibonaci(n - 2)

def main():
    data = sys.stdin.read().strip()
    if not data:
        return
    n = int(data)
    print(fibonaci(n))

if __name__ == "__main__":
    main()
