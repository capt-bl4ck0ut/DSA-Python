class Solution:
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        return self.stack.pop()
    def is_empty(self):
        return self.stack == []

def conver_bin(dec_num):
    if dec_num == 0:
        return 0
    s = Solution()
    while dec_num > 0:
        remainder = dec_num % 2
        s.push(remainder)
        dec_num = dec_num // 2
    bin = ""
    while not s.is_empty():
        bin += str(s.pop())
    return bin
command = int(input())
print(conver_bin(command))