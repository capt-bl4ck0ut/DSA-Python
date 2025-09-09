def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

if __name__ == "__main__":
    arr = [2, 5, 8, 9]
    x = 9
    result = linear_search(arr,x)
    if result == -1:
        print(f"[+] Không tìm thấy giá trị", x)
    else:
        print("Giá trị", x, "được tìm thấy tại vị trí", result)