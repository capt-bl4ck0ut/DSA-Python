import sys, re

def odd_at_even_index(arr):
    res = []
    for i in range(len(arr)):
        if i % 2 == 0 and arr[i] % 2 == 1:
            res.append(arr[i])
    return res

def main():
    data = sys.stdin.read()
    nums = list(map(int, re.findall(r'-?\d+', data)))
    if not nums:
        print("NULL")
        return
    if len(nums) >= 2 and nums[0] == len(nums) - 1:
        n = nums[0]
        arr = nums[1:1+n]
    else:
        arr = nums

    res = odd_at_even_index(arr)

    if res:
        for x in res:
            sys.stdout.write(str(x) + " ")
    else:
        print("NULL")

if __name__ == "__main__":
    main()
