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

if __name__ == "__main__":
    n = int(input())
    dslk = DSLK()
    
    for i in range(n, 0, -1):
        dslk.append(i)
    for i in range(2, n + 1):
        dslk.append(i)
    
    dslk.display()
