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
        curent_node = self.head
        while curent_node:
            print(curent_node.data, end=" ")
            curent_node = curent_node.next
        print()
    
    def delete(self, value):
        curent_node = self.head
        prev_node = None
        while curent_node and curent_node.data == value:
            self.head = curent_node.next
            curent_node = self.head
        while curent_node:
            if curent_node.data > value:
               prev_node.next = curent_node.next
               curent_node = curent_node.next
            else:
                prev_node = curent_node
                curent_node = curent_node.next
                
if __name__ == "__main__":
    dslk = DSLK()
    n = int(input())
    values = list(map(int, input().strip("[]").split(",")))
    k = int(input())
    for i in values:
        dslk.append(i)
    dslk.delete(k)
    dslk.display()


