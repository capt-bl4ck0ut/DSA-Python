class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class DSLK:
    def __init__(self):
        self.head = None
    
    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" ")
            current_node = current_node.next
        print()
    
    def change_value(self, value1, value2):
        current_node = self.head
        while current_node:
            if current_node.data == value1:
                current_node.data = value2
            current_node = current_node.next

if __name__ == "__main__":
    dslk = DSLK()
    n = int(input())
    values = list(map(int, input().strip("[]").split(",")))
    a = int(input())
    b = int(input())
    for i in values:
        dslk.append(i)
    dslk.change_value(a, b)
    dslk.display()


