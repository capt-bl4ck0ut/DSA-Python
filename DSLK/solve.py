class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class DSLK:
    def __init__(self):
        self.head = None

    def display(self):
        current_node = self.head
        while current_node:
            print(current_node, end = " ")
            current_node = current_node.next
        print("None")

    # Chèn một phần tử vào cuối danh sách
    def insertNodeLast(self, newnode):
        newnode = Node(newnode)
        if not self.head:
            self.head = newnode
            return   
        last_node = self.head   
        while last_node.next:
            last_node = last_node.next
        last_node.next = newnode

    def insertNodeFirst(self, newnode):
        new_node = Node(newnode)
        new_node.next = self.head
        self.head = new_node
        
    def insert_after_node(self, prev_node, newnode):
        current_node = self.head
        while current_node:
            if current_node.data == prev_node:
                new_node = Node(newnode)
                new_node.next = current_node.next
                current_node.next = new_node
                return
            current_node = current_node.next
            