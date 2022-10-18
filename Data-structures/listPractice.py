#List operations and functions
#concatenation
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)
print(len(c))
print(max(c))
print(min(c))
print(sum(c))

# * operator
a = [0, 1]
a = a * 4
print(a)

myList = []
fullList = list()
while(True):
    inp = input("Enter a word: ")
    if inp == 'done': break
    if inp[0] == 'a':
        myList.append(inp)
    else:
        fullList.append(inp)
    print(fullList)
    print(myList)

    finalList = [myList, sorted(fullList)]
    print(sorted(finalList))