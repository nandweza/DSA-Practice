"""
Linked lists in python are an ordered collection of objects.
"""

#implementing linkedlist using deque object.

from collections import deque

#creating a linkedlist and populating it at creation.
myList = deque(['a', 'b', 'c', 'd'])

print(myList)

#add element at the end of the linkedlist

myList.append('e')
print(myList)

#remove element at the end of the linkedlist

myList.pop()
print(myList)

#add element from the beginning of the linkedlist

myList.appendleft('f')
print(myList)

#remove elem from the beginning of the linkedlist
myList.popleft()
print(myList)

#Implementing a queue using deque (FIFO)

myQueue = deque([])

myQueue.append(3)
myQueue.append(2)
myQueue.append(4)

print(myQueue)

myQueue.popleft()
print(myQueue)

#Implementing a stack using deque (LIFO)

myStack = deque()

myStack.append('Allan')
myStack.append('Mary')
myStack.append('Eva')

print(myStack)

myStack.pop()
print(myStack)