def find_min(nums):
    minimum = nums[0]
    for i in range(len(nums)):
        if nums[i] < minimum:
           minimum = nums[i]
    return minimum
print(find_min([3,2,5,7]))