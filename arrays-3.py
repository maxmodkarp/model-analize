def sorted_squared(nums):
    squared_nums = [0] * len(nums)
    
    left, right, index = 0, len(nums) - 1, len(nums) - 1
    
    while left <= right:
        left_square = nums[left] ** 2
        right_square = nums[right] ** 2
        
        if left_square > right_square:
            squared_nums[index] = left_square
            left += 1
        else:
            squared_nums[index] = right_square
            right -= 1
        index -= 1
    
    return squared_nums

nums1 = [-4, -1, 0, 3, 10]
print(sorted_squared(nums1))  

nums2 = [-7, -3, 2, 3, 11]
print(sorted_squared(nums2))  
