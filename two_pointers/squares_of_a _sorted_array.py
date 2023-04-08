def squares_of_array(nums):
    l = 0
    r = len(nums) - 1
    result = [0] * len(nums)
    index = len(nums) - 1
    while l <= r:
        l_squared = nums[l] ** 2
        r_squared = nums[r] ** 2
        if l_squared > r_squared:
            result[index] = l_squared
            l += 1
            index -= 1
        else:
            result[index] = r_squared
            r -= 1
            index -= 1
    return result


nums1 = [1, 2, 3]
print(squares_of_array(nums1))

nums2 = [-5, -4, 0, 1, 2, 3]
print(squares_of_array(nums2))