from collections import deque

def maxSlidingWindow(nums, k):
    if not nums:
        return []

    max_values = []
    window = deque()

    for i in range(len(nums)):
        while window and window[0] < i - k + 1:
            window.popleft()

        while window and nums[window[-1]] <= nums[i]:
            window.pop()

        window.append(i)

        if i >= k - 1:
            max_values.append(nums[window[0]])

    return max_values

print(maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))  
print(maxSlidingWindow([1], 1))  
