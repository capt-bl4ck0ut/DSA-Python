import sys
import re

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

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

def tree_level(node):
    if node is None:
        return 0
    deg = (1 if node.left is not None else 0) + (1 if node.right is not None else 0)
    return max(deg, tree_level(node.left), tree_level(node.right))


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
        sys.stdout.write("0")
        return

    root = Node(arr[0])
    for x in arr[1:]:
        root.insert(x)

    sys.stdout.write(str(tree_level(root)))

if __name__ == "__main__":
    main()
