def count_numbers_with_even_digits(nums):
    def count_digits(number):
        return len(str(number))

    count = 0
    for num in nums:
        if count_digits(num) % 2 == 0:
            count += 1

    return count

nums1 = [12, 345, 2, 6, 7896]
print(count_numbers_with_even_digits(nums1))  

nums2 = [555, 901, 482, 1771]
print(count_numbers_with_even_digits(nums2))  
