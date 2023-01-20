"""
Implementing your own Linked List.
"""

#creating a linked list

#The class below stores the head(starting point of the linkedlist)

class LinkedList:
    def __init__(self):
        self.head = None

#another class to store nodes

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None