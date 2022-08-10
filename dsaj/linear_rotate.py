def count_rotations_linear(nums):
    position = 1                 # What is the intial value of position?
    
    while position < len(nums):                     # When should the loop be terminated?
        
        # Success criteria: check whether the number at the current position is smaller than the one before it
        if position > 0 and nums[position] < nums[position - 1]:   # How to perform the check?
            return position
        
        # Move to the next position
        position += 1
    
    return 0                     # What if none of the positions passed the check 

x = [1, 2, 3, 4, 5, -1, 0]
print(count_rotations_linear(x))

#sorted rotated list
a = [4, 5, 6, 1, 2, 3]
print(count_rotations_linear(a))

#An empty list
c = []
print(count_rotations_linear(c))

#List with one elements
d = [2]
print(count_rotations_linear(d))

#List with the same elements
e = [2, 2, 2]
print(count_rotations_linear(e))

#List with repeated elements
f = [4, 4, 5, 6, 6, 6, 2, 3]
print(count_rotations_linear(f))