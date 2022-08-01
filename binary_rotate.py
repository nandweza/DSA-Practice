def count_rotations_binary(nums):
    lo = 0
    hi = len(nums) - 1
    
    while lo <= hi:
        mid = (lo + hi) // 2
        mid_number = nums[mid]
        
        # Uncomment the next line for logging the values and fixing errors.
        # print("lo:", lo, ", hi:", hi, ", mid:", mid, ", mid_number:", mid_number)
        
        if mid > 0 and nums[mid] < nums[mid - 1]:
            # The middle position is the answer
            return mid
        
        elif mid > lo:
            # Answer lies in the left half
            hi = mid - 1  
        
        else:
            # Answer lies in the right half
            lo = mid + 1
    
    return 0

x = [1, 2, 3, 4, 5, -1, 0]
print(count_rotations_binary(x))