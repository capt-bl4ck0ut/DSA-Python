import sys, re

def first_index(a, x):
    left, right = 0, len(a) - 1
    ans = -1
    while left <= right:
        mid = (left + right) // 2
        if a[mid] == x:
            ans = mid
            right = mid - 1  
        elif a[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return ans

def main():
    data = sys.stdin.read()
    nums = list(map(int, re.findall(r'-?\d+', data)))
    if not nums:
        print(-1)
        return
    if len(nums) >= 2 and nums[0] == len(nums) - 2:
        n = nums[0]
        arr = nums[1:1+n]
        x = nums[1+n]
    else:
        arr = nums[:-1]
        x = nums[-1]

    print(first_index(arr, x))

if __name__ == "__main__":
    main()
