def badpairs(nums):
    n = len(nums) 
    total_pairs = n * (n - 1) // 2
    freq = {}
    goodpairs = 0
    for key , value in enumerate(nums):
        i = value - key

        if i in freq:
            goodpairs += freq[i]
            freq[i] += 1
        else:
            freq[i] = 1
        
    return total_pairs - goodpairs

print(badpairs([4,1,3,3]))