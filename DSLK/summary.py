class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class DSLK:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
    
    def print(self, data):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" ")
            current_node = current_node.next
        print()
    
    ## Chèn Phần từ vào đâu danh sách
    def insertFirts(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    ## Chèn phần tử sau phần tử đã biết cụ thể 
    def insertNode(self, prev_node, data):
        new_node = Node(data)
        current_node = self.head
        while current_node:
            if current_node.data == prev_node.data:
                new_node = Node(data)


