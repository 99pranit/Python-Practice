def findMin(nums):
    s , f = 0 ,1
    n = len(nums)

    while f != n:
        if nums[s] > nums[f]:
            return nums[f]
        s += 1
        f += 1
    return nums[0]