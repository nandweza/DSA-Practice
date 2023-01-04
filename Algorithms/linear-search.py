#!/usr/bin/python3
"""
In Computer science, linear search or sequential search algorithm is a method
of finding an element within a list, the search is done sequentially until the
desired match is found, else the whole list is searched upto the last element. 
"""

"""
Example 1
Given an array arr[] of N elements, the task is to write
a function to search a given element x in arr[].
"""

def search_elem(n, x):
    """
    a function to search a given elem x in arr[]
    """
    for i in range(0, len(n) - 1):
        if (n[i] == x):
            return i
    return -1

arr = [1, 2, 3, 4, 5, 6]
a = 4

print(search_elem(arr, a))