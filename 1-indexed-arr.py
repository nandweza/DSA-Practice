#!/usr/bin/python3
"""indexing the array to start at index 1 instead of index 0."""

arr = ['a', 'b', 'c', 'd', 'e', 'f']

for i, v in enumerate(arr, 1):
    print(i, v)