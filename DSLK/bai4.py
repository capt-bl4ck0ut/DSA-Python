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
    def display_at_postion(self, postion):
        current_node = self.head
        count = 0
        while current_node:
            if count == postion:
                return current_node.data
            current_node = current_node.next
            count += 1
        return None
if __name__ == "__main__":
    n = int(input())
    values = list(map(int, input().strip("[]").split(",")))
    k = int(input())

    dslk = DSLK()
    for i in values:
        dslk.append(i)
    result = dslk.display_at_postion(k)
    if result is not None:
        print(result)
    else:
        print("[+] Vị trí không hợp lệ")

        