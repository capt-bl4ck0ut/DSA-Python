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

    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" ")
            current_node = current_node.next
        print() 

    def insert_value_position(self, position, data):
        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current_node = self.head
        count = 0
        prev_node = None
        while current_node and count < position:
            prev_node = current_node
            current_node = current_node.next
            count += 1
        if count != position:
            print(f"Vị trí {position} vượt quá kích thước danh sách")
            return
        new_node.next = current_node
        prev_node.next = new_node

if __name__ == "__main__":
    n = int(input())
    values = list(map(int, input().strip("[]").split(",")))
    k = int(input())
    x = int(input())

    ds = DSLK()
    for val in values:
        ds.append(val)
    
    ds.insert_value_position(k, x)
    ds.display()
