'''
Queue()

enqueue()
dequeue()
size()
isEmpty()

'''

class Queue():
    def __init__(self):
        self.elements = []
    def enqueue(self, element):
        self.elements.insert(0, element)
    def dequeue(self):
        return self.elements.pop()
    def size(self):
        return len(self.elements)
    def isEmpty(self):
        return self.elements == []
    
myQueue = Queue()

print(myQueue.isEmpty())

myQueue.enqueue(10)
myQueue.enqueue(20)
myQueue.enqueue(30)

print(myQueue.dequeue())

print(myQueue.size())