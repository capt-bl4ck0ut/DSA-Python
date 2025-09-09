class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class DSLK:
    def __init__(self):
        self.head = None
    
    # Thêm từng phần tử
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node:
            last_node = last_node.next
        last_node.next = new_node
    
    def display(self):
        current_node = self.head
        while current_node.next:
            print(current_node.data, end=" ")
            current_node = current_node.next
        print()
    
    # Chèn 1 phần tử vào đau danh sách
    def insert_firstnode(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    # Chèn 1 phần tử sau 1 phần tử đã biết 
    def insert_after(self, pre_node, data):
        current_node = self.head
        while current_node:
            if current_node == pre_node.data:
                new_node = Node(data)
                new_node.next = current_node.next
                current_node.next = new_node
                return
            current_node = current_node.next
            print(f"[+] Node với giá trị {pre_node} không tồn tại trong danh sách liên kết")

    # Chèn 1 phân tử đã biết cụ thể
    def insert_node_postion(self, position, data):
            new_node = Node(data)
            if position == 0:
                self.head = new_node
                return
            current_node = self.head
            prev_node = None
            count = 0
            while current_node and count < position:
                prev_node = current_node
                current_node = current_node.next
                count += 1
            
            if count != position:
                print(f"[-] Vượt quá {position} trong danh sách liên kết")
                return
            new_node.next = current_node
            prev_node.next = new_node
    
    # Xóa 1 node bởi 1 giá trị, node cần xóa là node đầu tiên và node cần xóa không phải là node đầu tiên
    def delete_node(self, key):
        current_node = self.head
        if current_node and current_node.data == key:
            current_node = current_node.next
            return
        pre_node = None
        while current_node and current_node.data != key:
            pre_node = current_node
            current_node = current_node.next
        
        if current_node is None:
            print(f"[+] Node với giá trị {key} không tìm thấy trong danh sách")
            return
        pre_node.next = current_node.next
        current_node = None
    
    # Xóa 1 node đã biết vị trí cụ thể
    def delete_at_position(self, postion):
        if self.head is None:
            print(f"[+] Danh sách trống")
            return
        current_node = self.head
        if postion == 0:
            current_node = current_node.next
            current_node = None
            return
        count = 0
        prev_node = None
        while current_node and count != postion:
            prev_node = current_node
            current_node = current_node.next
        if current_node is None:
            print(f"[+] Vị trí {postion} không tìm thấy trong danh sách")
            return
        prev_node = current_node.next
        current_node = None
        

