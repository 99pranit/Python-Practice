"""
Given an integer array nums, return an array output where output[i] 
is the product of all the elements of nums except nums[i].
"""
def product_except_itself(nums):
    ans = [1] * len(nums)
    prefix = 1
    for i in range(len(nums)):
        ans[i] = prefix
        prefix *= nums[i]

    postfix = 1
    for j in range(len(nums) - 1 , -1 , -1):
        ans[j] *= postfix
        postfix *= nums[j]

    return ans

print(product_except_itself([1,2,4,6]))