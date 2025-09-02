class Solution:
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        return self.stack.pop()
    def is_empty(self):
        return self.stack == []
    def peek(self):
        if not self.is_empty():
            return self.stack[-1] 
def encode(s):
    if not s:
        return ""
    stack = Solution()
    result = ""
    count = 0
    #aaaabbaaac
    for char in s:
        if stack.is_empty() or char != stack.peek():
            if not stack.is_empty():
                result += stack.pop() + str(count)
            stack.push(char)
            count = 1
        else:
            count += 1
    if not stack.is_empty():
        result += stack.pop() + str(count)
    return result
s = input()
print(encode(s))