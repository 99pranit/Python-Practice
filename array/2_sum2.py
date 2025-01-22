"""
Return the indices (1-indexed) of two numbers, [index1, index2], 
such that they add up to a given target number target and index1 < index2.
Note that index1 and index2 cannot be equal, therefore you may not use
the same element twice.

Your solution must use O(1) additional space.
"""

def twosum(nums , target):
    l , r = 0 , len(nums) - 1
    while l<r:
        cursum = nums[l] + nums[r]
        if target is cursum:
            return [l+1 , r+1]
        elif cursum < target:
            l += 1
        else:
            r -= 1

print(twosum([1,2,3,4] , 3))