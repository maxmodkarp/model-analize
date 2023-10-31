def sort_array_by_parity(nums):
    even = [x for x in nums if x % 2 == 0] 
    odd = [x for x in nums if x % 2 != 0]  

    return even + odd  

arr1 = [3, 1, 2, 4]
print(sort_array_by_parity(arr1)) 

arr2 = [0]
print(sort_array_by_parity(arr2))  
