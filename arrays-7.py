def check_if_exist(arr):
    seen = set()

    for num in arr:
        if num * 2 in seen or (num % 2 == 0 and num // 2 in seen):
            return True
        seen.add(num)

    return False

arr1 = [10, 2, 5, 3]
print(check_if_exist(arr1)) 

arr2 = [3, 1, 7, 11]
print(check_if_exist(arr2))  
