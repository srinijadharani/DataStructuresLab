class Queue(object):
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def enqueue(self, item):
        self.items.insert(0, item)
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
    def display(self):
        print(self.items)
qu = Queue()
print("Is the queue empty?", qu.isEmpty())
qu.enqueue(3)
qu.enqueue("Hey")
qu.enqueue(9)
qu.enqueue(10)
qu.enqueue("DSP")
qu.enqueue(87)
print("The queue is after Enqueue: ")
qu.display()
print("Is the queue empty?", qu.isEmpty())
print("Dequeue element:", qu.dequeue())
print("The queue is after Dequeue: ")
qu.display()
print("Size of the queue is:", qu.size())