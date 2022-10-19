#tuples are immmutable

# creating a tuple

newTuple = ('a', 'b', 'c', 'd', 'e', 1)
myTuple = tuple('allan')
print(newTuple)
print(myTuple)

# tuple concatenation
print(newTuple + myTuple)

# * operation
print(myTuple * 3)

#returns true if element exist
print('l' in myTuple)

#count the times an element exists
print(myTuple.count('l'))

#returns index of element
print(myTuple.index('n'))

#returns number of elements
print(len(myTuple))

#returns max and min respectively
print(max(myTuple))
print(min(myTuple))

#converts list to tuple
myList = ['l', 'i', 'f', 'e']
print(tuple(myList))