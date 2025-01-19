def missing_number(nums):
    res = len(nums)
    for i in range(len(nums)):
        res = res ^ i ^nums[i]

    return res

print(missing_number([0,1,3,4]))