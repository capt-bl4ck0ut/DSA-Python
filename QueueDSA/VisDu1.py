"""
- Triển khai 1 lớp hàng đợi
"""
class Queue:
    def __init__(self):
        self.queue = []
    def Enqueue(self, value):
        self.queue.append(value)
    def Dequeue(self):
        if self.isEmpty():
            return "Queue is Empty"
        return self.queue.pop(0)
    def peek(self):
        if self.isEmpty():
            return "Queue is Empty"
        return self.queue[0]
    def isEmpty(self):
        return self.queue == 0
    def size(self):
        return len(self.queue)

myQueue = Queue()
myQueue.Enqueue("A")
myQueue.Enqueue("B")
myQueue.Enqueue("C")

print("Queue: ", myQueue.queue)
print("Peek: ", myQueue.peek())
print("Dequeue: ", myQueue.Dequeue())
print("After Enqueue: ", myQueue.queue)
print("IsEmpty: ", myQueue.isEmpty())
print("Size: ", myQueue.size())