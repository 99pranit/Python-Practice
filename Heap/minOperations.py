'''
You are given a 0-indexed integer array nums, and an integer k.

In one operation, you will:

Take the two smallest integers x and y in nums.
Remove x and y from nums.
Add min(x, y) * 2 + max(x, y) anywhere in the array.
Note that you can only apply the described operation if nums contains at least two elements.

Return the minimum number of operations needed so that all elements of the array are greater than or equal to k.
'''
import heapq
def minOperations(nums,k):
    heapq.heapify(nums)
    c = 0
    while len(nums) > 1:
        if nums[0] >= k:
            return c

        x = heapq.heappop(nums)
        y = heapq.heappop(nums)
        n = x * 2 + y
        c += 1

        heapq.heappush(nums,n)

    return c

print(minOperations([2,11,10,1,3],10))