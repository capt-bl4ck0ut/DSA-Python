def search_min(a):
    min_val = a[0]
    min_index = 0
    for i in range(1, len(a)):
        if a[i] < min_index:
            min_val = a[i]
            min_index = i
    return min_index 

def search_max(a):
    max_val = a[0]
    max_index = 0
    for i in range(1, len(a)):
        if a[i] >= max_index:
            max_val = a[i]
            max_index = i
    return max_index
def swap(a):
    min_value = search_min(a)
    max_value = search_max(a)
    a[min_value], a[max_value] = a[max_value], a[min_value]
    return a

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    result = swap(arr)
    for x in result:
        print(x, end=" ")

