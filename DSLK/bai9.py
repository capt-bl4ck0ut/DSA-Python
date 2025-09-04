class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = new_node
        else:
            tmp = self.head
            while tmp.next != self.head:
                tmp = tmp.next
            tmp.next = new_node
            new_node.next = self.head
    
    def get_node_at(self, index):
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
    
    def print(self, start_index, count):
        start_node = self.get_node_at(start_index)
        temp = start_node
        for _ in range(count):
            print(temp.data, end=" ")
            temp = temp.next

if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    k = int(input())
    
    dslkvong = CircularLinkedList()
    for num in arr:
        dslkvong.append(num)

    dslkvong.print(k, n)


