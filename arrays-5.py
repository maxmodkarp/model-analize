def merge_sorted_arrays(nums1, m, nums2, n):
    i = m - 1 
    j = n - 1  
    k = m + n - 1 

    while i >= 0 and j >= 0:
        if nums1[i] >= nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1

    while j >= 0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1

nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
merge_sorted_arrays(nums1, m, nums2, n)
print(nums1)  

nums3 = [1]
m = 1
nums4 = []
n = 0
merge_sorted_arrays(nums3, m, nums4, n)
print(nums3)  

nums5 = [0]
m = 0
nums6 = [1]
n = 1
merge_sorted_arrays(nums5, m, nums6, n)
print(nums5) 
