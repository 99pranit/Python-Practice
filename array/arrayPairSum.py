'''
Given an integer array nums of 2n integers, group these 
integers into n pairs (a1, b1), (a2, b2), ..., (an, bn) 
such that the sum of min(ai, bi) for all i is maximized. 
Return the maximized sum.
'''

def arrayPairSum(nums):
    return sum(sorted(nums)[::2])

print(arrayPairSum([1,4,3,2]))