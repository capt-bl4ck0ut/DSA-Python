import sys

def game(n):
    if n == 1:
        return 1
    else:
        return 1 + game(n-(n+1)//2)

def main():
    data = sys.stdin.read().strip()
    if not data:
        return
    n = int(data)
    print(game(n))

if __name__ == "__main__":
    main()
