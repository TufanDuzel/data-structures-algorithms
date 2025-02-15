'''
Stack()

push()
pop()
showLastItem()
size()
isEmpty()

'''

class Stack():
    def __init__(self):
        self.elements = []
    def push(self, element):
        self.elements.append(element)
    def pop(self):
        self.elements.pop()
    def showLastItem(self):
        return self.elements[len(self.elements) - 1]
    def size(self):
        return len(self.elements)
    def isEmpty(self):
        return self.elements == []
    
myStack = Stack()

print(myStack.isEmpty())

myStack.push(10)
myStack.push(20)
myStack.push(30)
print(myStack.showLastItem())

myStack.pop()
print(myStack.showLastItem())

print(myStack.size())

myStack.push("a")
print(myStack.showLastItem())