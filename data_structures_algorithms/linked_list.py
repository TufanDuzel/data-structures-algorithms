# Node -> LinkedList

# Singly LinkedList
#%%
class Node():
    def __init__(self, value):
        self.value = value
        self.nextNode = None
        
firstNode = Node(10)
secondNode = Node(20)
thirdNode = Node(30)

firstNode.nextNode = secondNode
secondNode.nextNode = thirdNode

print(firstNode.nextNode.nextNode.value)

# Doubly LinkedList
#%%
class Node():
    def __init__(self, value):
        self.value = value
        self.nextNode = None
        self.prevNode = None
        
firstNode = Node(1)
secondNode = Node(2)
thirdNode = Node(3)

firstNode.nextNode = secondNode

secondNode.prevNode = firstNode
secondNode.nextNode = thirdNode

thirdNode.prevNode = secondNode

print(firstNode.nextNode.nextNode.value)
print(thirdNode.prevNode.value)
