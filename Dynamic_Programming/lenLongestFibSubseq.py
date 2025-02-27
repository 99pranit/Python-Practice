'''
Given a strictly increasing array arr of positive integers forming a sequence, 
return the length of the longest Fibonacci-like subsequence of arr. 
If one does not exist, return 0.
'''
def lenFibseq(arr):
    index = {x : i for i , x in enumerate(arr)}
    dp = {}
    maxlen = 0

    for j in range(len(arr)):
        for i in range(j):
            x = arr[j] - arr[i]

            if x in index and index[x] < i:
                k = index[x]
                dp[i , j]  = dp.get((k , i) , 2) + 1
                maxlen = max(maxlen , dp[i , j])

    return maxlen if maxlen > 2 else 0


print(lenFibseq([1,2,3,4,5,6,7,8]))