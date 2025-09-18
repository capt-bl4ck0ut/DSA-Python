import sys

def bubble_sort(nums):
    swap = True
    while swap:
        swap = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i], nums[i + 1] = nums[i + 1], nums[i]
                swap = True

def main():
    data = list(map(int, sys.stdin.read().strip().split()))
    if len(data) < 2:
        return
    n = data[0]          
    arr = data[1:1+n]       
    if len(arr) != n:
        return
    bubble_sort(arr)
    for num in arr:
        print(num, end=" ")

if __name__ == "__main__":
    main()
