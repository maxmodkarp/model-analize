def valid_mountain_array(arr):
    n = len(arr)
    
    if n < 3:
        return False  
    
    i = 0
    
    while i < n - 1 and arr[i] < arr[i + 1]:
        i += 1
    
    if i == 0 or i == n - 1:
        return False 
    
    while i < n - 1 and arr[i] > arr[i + 1]:
        i += 1
    
    return i == n - 1

arr1 = [2, 1]
print(valid_mountain_array(arr1))  

arr2 = [3, 5, 5]
print(valid_mountain_array(arr2))  

arr3 = [0, 3, 2, 1]
print(valid_mountain_array(arr3))  
