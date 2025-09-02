class Node:
    def __init__(self, data):
        self.data = data
        self.head = None
    
class DSLK:
    def __init__(self):
        self.head = None
    
    def display(self):
        current = self.head
        while current:
            print(current.data, end = " -> ")
            current = current.next
        print("None")

    # Hàm append 1 node
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node:
            last_node = last_node.next
        last_node.next = new_node

    # Chèn 1 phần tử vào đầu dslk
    def firstNode(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    # Chèn 1 phần tử sau 1 phần tử đã biết cụ thể
    def insert_after_node(self, pre_node, data):
        curent_node = self.head
        while curent_node:
            if curent_node.data == pre_node.data:
                new_node = Node(data)
                new_node.next = curent_node.next
                curent_node.next = new_node
                return
            curent_node = curent_node.next
        print(f"Node với giá trị {pre_node} không tồn tại trong danh sách liên kết.")
    
    # Chèn 1 node vào vị trí cụ thể
    def insert_at_postion(self, postion, data):
        new_node = Node(data)
        # Chèn vào vị trí 0
        if postion == 0:
            new_node.next = self.head
            self.head = new_node
            return
        # Chèn vào vị trí bất kì
        current_node =  self.head
        count = 0
        prev_node = None

        # Duyệt qua danh sách để tìm vị trí cần chèn
        while current_node and count < postion:
            prev_node = current_node
            current_node = current_node.next
            count += 1
        # Nếu vị trí vượt qua kích thước
        if count != postion:
            print(f"Vị trí {postion} vượt quá kích thước của danh sách")
            return
        # Chèn node mới vào vị trí đã tìm thấy
        new_node.next = current_node
        prev_node.next = new_node

    # Xóa bởi 1 giá trị, node cần xóa là node đầu tiên, node cần xóa không phải node đầu tiên
    def delete_node(self, key):
        current_node = self.head
        if current_node and current_node.data == key:
            current_node = current_node.next
            return
        pre_node = None
        while current_node and current_node.data != key:
            pre_node = current_node
            current_node = current_node.next
        # Nếu node cần xóa không tồn tại trong danh sách
        if current_node is None:
            print(f"Node với giá trị {key} không tồn tại trong danh sách liên kết.")
            return
        pre_node.next = current_node.next
        current_node = None
    # Xóa node bởi giá trị ở vị trí cụ thể
    def delete_at_postion(self, postion):
        if self.head is None:
           print("Danh sách trống")
           return
        curent_node = self.head
        if postion == 0:
           self.head = curent_node.next
           curent_node = None
           return
        pre_node = None
        count = 0
        while curent_node and count != postion:
           pre_node = curent_node
           curent_node = curent_node.next
           count += 1
        # Nếu vị trí không tồn tại trong danh sách
        if curent_node is None:
            print(f"Vị trí {postion} vượt quá kích thước danh sách")
            return
        pre_node.next = curent_node.next
        curent_node = None
    # Độ dài của node
    def get_length(self):
        curent_node = self.head
        count = 0
        while curent_node:
            count += 1
            curent_node = curent_node.next
        return count
    # Đệ quy 
    def get_length_recurisive(self, node):
        # Nếu node là None, tức là danh sách rỗng
        if not node:
            return 0
        return 1 + self.get_length_recurisive(node.next)
    # Reverslist
    def reverslist(self):
        # prev bắt đầu là None vì node cuối cùng của danh sách liên kết đảo ngược sẽ trỏ đến None
        prev = None
        current = self.head
        while current:
            next_node = current.next # Lưu trữ node tiếp theo
            current.next = prev # Đảo ngược node
            prev = current # Di chuyển prev lên
            current = next_node # Di chuyển current lên node tiếp theo
        self.head = prev

            