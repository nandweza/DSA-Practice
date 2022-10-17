from array import *

# 1. Create an array and traverse.
myArray = [1, 2, 3, 4, 5, 6]

for i in myArray:
    print(i)

# 2. Access individual elements thru indexes.
print('access any element:')
print(myArray[4])
# 3. Append any value to the array using append() method.
print('append any value to the array:')
myArray.append(8)
print(myArray)

# 4. Insert value in an array using insert() method.
print('Insert value:')
myArray.insert(6, 7)
print(myArray)

# 5. Extend python array using extend() method.
print('Extend array:')
myArray2 = [10, 11, 12, 13]
myArray.extend(myArray2)
print(myArray)

# 6. Add items from list into array using fromlist() mtd.
#print('********************************************************************')
#myList = [20, 21, 22, 23]
#myArray.fromlist(myList)
#print(myArray)

# 7. Remove any array element using remove() mtd.
print('Remove an element:')
myArray.remove(2)
print(myArray)

# 8. Remove last array element using pop() mtd.
print('Remove last element:')
myArray.pop()
print(myArray)

# 9. Fetch any element thru its index using index() mtd.
print('Fetch element thru index:')
print(myArray.index(5))

# 10.Reverse a python array using reverse() mtd.
print('reversed array:')
myArray.reverse()
print(myArray)

# 11.Get array buffer information thru buffer_info() mtd.
# 12.Check for number of occurrences of an element using count() mtd.
print('Count occurences of an element:')
print(myArray.count(3))

# 13.Convert array to string using tostring() mtd.

# 14.Convert array to a python list with same elements using tolist() mtd.

# 15.Append a string to char array using fromstring() mtd.
# 16.Slice elements from an array.
print('slice:')
print(myArray[1:4])