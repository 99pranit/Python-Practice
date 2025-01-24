'''
You are given an integer array heights where heights[i] represents the height of the h ith bar.
'''

def maxArea(heights):
    n = len(heights) - 1
    left , right = 0 , n
    amount = float('-inf')
    current = 0

    while left<right:
        current = min(heights[left] , heights[right]) * n
        amount = max(current , amount)
        if heights[left] > heights[right]:
            right -= 1
            n -= 1
        else:
            left += 1
            n -= 1
    return amount

print(maxArea([1,7,2,5,4,7,3,6]))