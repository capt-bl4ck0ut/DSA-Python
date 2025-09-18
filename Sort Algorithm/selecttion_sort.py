import sys
def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        arr[i], arr[min_index] = arr[min_index] , arr[i]

def main():
    data = list(map(int, sys.stdin.read().strip().split()))
    if len(data) < 2:
        return
    n = data[0]           
    arr = data[1:1+n]      
    if len(arr) != n:
        return
    selection_sort(arr)
if __name__ == "__main__":
    main()