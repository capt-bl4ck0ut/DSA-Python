import sys
import re

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, x):
        if x < self.data:
            if self.left is None:
                self.left = Node(x)
            else:
                self.left.insert(x)
        else:  
            if self.right is None:
                self.right = Node(x)
            else:
                self.right.insert(x)

    def inorder(self, out):
        if self.left:
            self.left.inorder(out)
        out.append(self.data)
        if self.right:
            self.right.inorder(out)

def main():
    data = sys.stdin.read()
    nums = list(map(int, re.findall(r"-?\d+", data)))
    if not nums:
        return
    if "[" in data or "]" in data:
        arr = nums
    else:
        n = nums[0]
        arr = nums[1:1+n]
    if not arr:
        return
    root = Node(arr[0])
    for x in arr[1:]:
        root.insert(x)
    res = []
    root.inorder(res)
    sys.stdout.write(" ".join(map(str, res)) + " ")

if __name__ == "__main__":
    main()
