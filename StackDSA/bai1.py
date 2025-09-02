class Stack():
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def is_empty(self):
        return self.items == []
def rever(s):
    stack = Stack()
    for char in s:
        stack.push(char)
    rever_string = ""
    while not stack.is_empty():
        rever_string += stack.pop()
    return rever_string
s = input()
print(rever(s))