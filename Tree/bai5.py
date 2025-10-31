import sys, re

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    
    def trung(self, out):
        if self.left:
            self.left.trung(out)
        out.append(self.val)
        if self.right:
            self.right.trung(out)

    def insert(self, x):
        if x < self.val:
            if self.left is None:
                self.left = Node(x)
            else:
                self.left.insert(x)
        else:
            if self.right is None:
                self.right = Node(x)
            else:
                self.right.insert(x)
def remove(root, x):
    if root is None:
        return 0
    root.left = remove(root.left, x)
    root.right = remove(root.right, x)
    if root.val == x:
        return None
    return root

def read_input():
    data = sys.stdin.read()
    nums = list(map(int, re.findall(r"-?\d+", data)))
    if not nums:
        return [], None
    if len(nums) >= 2 and nums[0] == len(nums) - 2:
        n = nums[0]
        arr = nums[1:1+n]
        x = nums[1+n]
        return arr, x
    else:
        arr = nums[:-1]
        x = nums[-1]
        return arr, x

def main():
    arr, x = read_input()
    if not arr:
        print("NULL")
        return

    # Xây BST
    root = Node(arr[0])
    for v in arr[1:]:
        root.insert(v)

    root = remove(root, x)

    if root is None:
        print("NULL")
    else:
        out = []
        root.trung(out)
        if out:
            print(" ".join(map(str, out)))
        else:
            print("NULL")

if __name__ == "__main__":
    main()