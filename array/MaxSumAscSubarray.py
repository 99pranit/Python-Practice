'''
Given an array of positive integers nums, return the 
maximum possible sum of an ascending subarray in nums.
'''
def MaxSum(nums):
    s , f = 0 , 1
    n = len(nums)
    su = nums[0]
    maxsum = max(nums)

    while f<n:
        if nums[s] < nums[f]:
            su += nums[f]
            maxsum = max(maxsum , su)
            s , f = f , f+1
        else:
            s , f = f , f + 1
            su = nums[s]

    return maxsum


print(MaxSum([10,20,30,5,10,50]))