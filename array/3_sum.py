'''
Given an integer array nums, return all the triplets 
[nums[i], nums[j], nums[k]] where nums[i] + nums[j] + nums[k] == 0, 
and the indices i, j and k are all distinct.
'''

def threesum(nums):
    nums.sort()
    ans = []
    for i , a in enumerate(nums):
        if i > 0 and a == nums[i-1]:
            continue
        l , r = i+1 , len(nums) - 1
        while l<r:
            cursum = a + nums[l] + nums[r]
            if cursum == 0:
                ans.append([a , nums[l] , nums[r]])
                l += 1
                while nums[l] == nums[l-1] and l<r:
                    l += 1
            elif cursum < 0:
                l += 1
            else:
                r-=1
    return ans



print(threesum([-1,0,1,2,-1,-4]))