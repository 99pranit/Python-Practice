def maxSum(nums):
    def sumdigit(n):
        s = 0
        while n:
            s += n%10
            n = n//10
        return s
    
    d = {}
    for num in nums:
        n1 = sumdigit(num)
        if n1 not in d:
            d[n1] = []
        d[n1].append(num)
    
    maxsum = -1
    for key,value in d.items():
        if len(value) > 1:
            value.sort(reverse = True)
            maxsum = max(maxsum,value[0]+value[1])

    return maxsum


print(maxSum([18,43,36,13,7]))
