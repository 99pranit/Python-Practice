'''
You are given an integer array piles where piles[i] is the number 
of bananas in the ith pile. You are also given an integer h, 
which represents the number of hours you have to eat all the bananas.
'''
import math
def minSpeed(piles , hour):
    l , r = 1 , max(piles)

    while l<r:
        mid = (l+r) // 2
        s = 0
        for p in piles:
            s = s + math.ceil(p/mid)

        if s <= hour:
            ans = mid
            r = mid - 1
        else:
            l = mid + 1
        
    return ans

print(minSpeed([1,4,3,2] , 9))