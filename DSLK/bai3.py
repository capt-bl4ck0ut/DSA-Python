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

    def delete_at_postion(self, postion):
        if self.head is None:
            print(f"[+] Danh Sách Trống")
            return
        current_node = self.head
        if postion == 0:
            self.head = current_node.next
            return 
        prev_node = None
        count = 0
        while current_node and count != postion:
            prev_node = current_node
            current_node = current_node.next
            count += 1
        if count != postion:
            print(f"[+] Vị trí {postion} vượt quá kích thước của mảng")
            return
        prev_node.next = current_node.next
        current_node = None
if __name__ == "__main__":
    n = int(input())
    values = list(map(int, input().strip("[]").split(",")))
    k = int(input())

    dslk = DSLK()
    for i in values:
        dslk.append(i)
    dslk.delete_at_postion(k)
    dslk.display()