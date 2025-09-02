class Stack:
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        return self.stack.pop() 
    def peek(self):
        if self.isEmpty():
            return "Stack is Empty"
        return self.stack[-1]
    def isEmpty(self):
        return self.stack == []

def is_balance(p1, p2): 
    if p1 == "(" and p2 == ")":
        return True
    elif p1 == "{" and p2 == "}":
        return True
    elif p1 == "[" and p2 == "]":
        return True
    else:
        return False

def final(string_parent):
    stack = Stack()
    balanced = True 
    index = 0

    while index < len(string_parent) and balanced:
        parent = string_parent[index]
        if parent in "({[":
            stack.push(parent)
        else:
            if stack.isEmpty():
                balanced = False
            else:
                top = stack.pop()
                if not is_balance(top, parent): 
                    balanced = False
        index += 1
    
    return balanced and stack.isEmpty()

s = input()
print(final(s))
