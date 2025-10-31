import sys
import re

# --- Cấu trúc node của BST ---
class Node:
    __slots__ = ("val", "left", "right")
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def insert_bst(root, x):
    if root is None:
        return Node(x)
    if x < root.val:
        root.left = insert_bst(root.left, x)
    else:  # x >= root.val
        root.right = insert_bst(root.right, x)
    return root

def check_avl(node):
    if node is None:
        return True, 0
    okL, hL = check_avl(node.left)
    if not okL:
        return False, 0
    okR, hR = check_avl(node.right)
    if not okR:
        return False, 0
    if abs(hL - hR) > 1:
        return False, 0
    return True, max(hL, hR) + 1

def main():
    data = sys.stdin.read()
    nums = list(map(int, re.findall(r"-?\d+", data)))
    if not nums:
        print("true")  
        return
    if "[" in data or "]" in data:
        arr = nums
    else:
        n = nums[0]
        arr = nums[1:1+n]

    root = None
    for x in arr:
        root = insert_bst(root, x)

    is_avl, _ = check_avl(root)
    print("true" if is_avl else "false")

if __name__ == "__main__":
    main()
