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
        for val in self.queue:
            print(val, end=' ')  

def isPrimary(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True  

def super_primary(n):
    while n > 0:
        if not isPrimary(n):
            return False
        n //= 10 
    return True

def super_is_primary(n):
    q = Queue()
    for i in range(2, n + 1):
        if super_primary(i):
            q.Enqueue(i)
    q.display()

n = int(input())
super_is_primary(n)
