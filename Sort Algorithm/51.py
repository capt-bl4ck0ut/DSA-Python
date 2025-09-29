import sys

def sort_custom(arr):
    positives = sorted([x for x in arr if x > 0])     
    negatives = sorted([x for x in arr if x < 0], reverse=True)  
    
    res = []
    pi, ni = 0, 0 
    for x in arr:
        if x > 0:
            res.append(positives[pi])
            pi += 1
        elif x < 0:
            res.append(negatives[ni])
            ni += 1
        else:
            res.append(0)
    return res

def main():
    data = list(map(int, sys.stdin.read().strip().split()))
    n = data[0]
    arr = data[1:1+n]
    result = sort_custom(arr)
    print(" ".join(map(str, result)) + " ")

if __name__ == "__main__":
    main()
