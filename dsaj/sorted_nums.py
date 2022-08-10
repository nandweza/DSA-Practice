# arr = [] -> array of integers, sorted in ascending order.
#finding the startint and ending position of a given number.

def sort_arr(arr, target):
    position = 0

    while position < len(arr):
        if position == target:
            return position
        position += 1
    return -1

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
c = 6
print(sort_arr(a, c))