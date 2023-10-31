def duplicate_zeros(arr):
    n = len(arr)
    i = n - 1 

    while i >= 0:
        if arr[i] == 0:
            for j in range(n - 1, i, -1):
                if j + 1 < n:
                    arr[j + 1] = arr[j]
            if i + 1 < n:
                arr[i + 1] = 0
            i -= 1
        i -= 1

arr1 = [1, 0, 2, 3, 0, 4, 5, 0]
duplicate_zeros(arr1)
print(arr1)  

arr2 = [1, 2, 3]
duplicate_zeros(arr2)
print(arr2) 
