"""
You are given list of numbers, obtained by rotating a sorted list an unknown number of times.
Write a function to determine the minimum number of times the original sorted list was rotated
to obtain the given list. Your function should have the worst-case complexity of O(log N),
where N is the length of the list. You can assume that all the numbers in the list are unique.

Example: The list [5, 6, 9, 0, 2, 3, 4] was obtained by rotating the sorted list [0, 2, 3, 4, 5, 6, 9]
3 times.

We define "rotating a list" as removing the last element of the list and adding it before the first
element. E.g. rotating the list [3, 2, 4, 1] produces [1, 3, 2, 4].

"Sorted list" refers to a list where the elements are arranged in the increasing order e.g.
[1, 3, 5, 7].
"""

def count_rotations(nums):
    n = len(nums)
    for i in range(0, n):
        #find the smallest element in the list
        if (nums[i] < nums[i - 1]):
            return i
    return 0


#sorted rotated list
a = [4, 5, 6, 1, 2, 3]
print(count_rotations(a))

#Sorted rotated list
b = [5, 6, 1, 2, 3, 4]
print(count_rotations(b))

#An empty list
c = []
print(count_rotations(c))

#List with one elements
d = [2]
print(count_rotations(d))

#List with the same elements
e = [2, 2, 2]
print(count_rotations(e))

#List with repeated elements
f = [4, 4, 5, 6, 6, 6, 2, 3]
print(count_rotations(f))