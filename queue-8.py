def maxSumAfterKOperations(nums, k):
    n = len(nums)
    dp = [0] * n
    for i in range(n):
        dp[i] = nums[i]
    max_sum = max(dp)

    for i in range(1, k + 1):
        temp = [0] * n
        max_val = float('-inf')

        for j in range(n):
            dp[j] = max(dp[j], temp[j] + nums[j])
            max_val = max(max_val, dp[j])
            if j >= k:
                temp[j - k] = max(0, max_val)

        max_sum = max(max_sum, max(dp))

    return max_sum

nums1 = [10, 2, -10, 5, 20]
k1 = 2
print(maxSumAfterKOperations(nums1, k1)) 

nums2 = [-1, -2, -3]
k2 = 1
print(maxSumAfterKOperations(nums2, k2)) 

nums3 = [10, -2, -10, -5, 20]
k3 = 2
print(maxSumAfterKOperations(nums3, k3)) 
