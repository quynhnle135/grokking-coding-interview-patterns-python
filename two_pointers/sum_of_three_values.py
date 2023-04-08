def sum_of_three(nums, target):
    nums.sort()

    for i in range(0, len(nums) - 2):
        low = i + 1
        high = len(nums) - 1

        while low < high:
            triplet = nums[i] + nums[low] + nums[high]
            if triplet == target:
                return True
            elif triplet < target:
                low += 1
            else:
                high -= 1

    return False


nums = [5, 4, 8, 9, 2]
target = 17
print(sum_of_three(nums, target))