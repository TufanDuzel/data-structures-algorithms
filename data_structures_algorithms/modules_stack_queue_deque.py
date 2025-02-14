# %%
from queue import LifoQueue

myStack = LifoQueue()

# Adding from top.
myStack.put(1)
myStack.put(10)
myStack.put(100)

# Removing from top.
# LIFO
myStack.get()

# %%
from queue import Queue

myQueue = Queue()

# Adding from left.
myQueue.put(2)
myQueue.put(20)
myQueue.put(200)

# Removing from right.
# FIFO
myQueue.get()

# %%
from collections import deque

myDeque = deque()

# Can be added from both right and left.
myDeque.append(3)
myDeque.append(30)
myDeque.append(300)
myDeque

myDeque.appendleft(3000)
myDeque

# Can be removed from both the right and left.
myDeque.pop()
myDeque

myDeque.popleft()
myDeque