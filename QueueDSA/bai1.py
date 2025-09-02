class Queue:
    def __init__(self):
        self.queue = []
    def Enqueue(self, value):
        self.queue.append(value)
    def Dequeue(self):
        if self.isEmpty():
            return None
        return self.queue.pop(0)
    def isEmpty(self):
        return len(self.queue) == 0
    def display(self):
        print(' '.join(map(str, self.queue)), end=' ')

def swap(n, k, values):
    queue = Queue()
    for value in values:
        queue.Enqueue(value)
    for _ in range(k):
        front = queue.Dequeue()
        queue.Enqueue(front)
    queue.display()
    
n = int(input())                       
values = list(map(int, input().split())) 
k = int(input())                         
swap(n, k, values)
