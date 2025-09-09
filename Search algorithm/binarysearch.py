def binarysearch(arr, x):
    low = 0
    hight = len(arr) - 1
    mid = 0

    # Duyệt qua danh sách mảng để tìm kiếm phần tử
    while low <= hight:
        mid = (low + hight) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            low = mid -1
        else:
            return mid
    return -1

arr = [1,2,3,4,5]
x = 3
result = binarysearch(arr, x)
if result != -1:
    print(f"[+] Phần tử được tìm thấy vị trí", str(result))
else:
    print(f"[-] Phần tử không được tìm thấy")