def singleNumber(nums):
    res = 0
    for num in nums:
        res = res ^ num
    return res

print(singleNumber([2,3,2]))