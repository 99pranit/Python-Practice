def top_k_freq(nums , k):
    freq = [[] for i in range(len(nums) + 1)]
    dic ={}

    for num in nums:
        dic[num] = 1 + dic.get(num,0)

    for key,val in dic.items():
        freq[val].append(key)

    res = []

    for i in range(len(freq) - 1 , 0 , -1):
        for n in freq[i]:
            res.append(n)
            k -= 1
            if not k:
                return res

print(top_k_freq([1,1,2,2,3,3,3,4] , 3))
