class Solution:
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        return self.stack.pop()
    def peek(self):
        if self.isEmpty:
            print("Stack Is Empty")
        return self.stack[-1]
    def isEmpty(self):
        return self.stack == []

def convert(input_str):
    stack = Solution()
    for i in input_str:
        stack.push(i)
    rever_string = ""
    while not stack.isEmpty():
        rever_string += stack.pop()
    return rever_string
n = input()
print(convert(n))
    