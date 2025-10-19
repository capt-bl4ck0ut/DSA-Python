import sys

def nhiphan(n, prefix = ""):
    if len(prefix) == n:
        print(prefix, end=' ')
        return
    nhiphan(n, prefix + '0')
    nhiphan(n, prefix + '1')

def main():
    data = sys.stdin.read().strip()
    if not data:
        return
    n = int(data)
    nhiphan(n)

if __name__ == "__main__":
    main()
