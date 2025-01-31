def longest_substring_repeating_k(s , k):
    if not s:
        return 0
    
    l ,r = 0,0
    freq = {}
    maxlen = 0
    maxf = 0
    for r in range(len(s)):
        freq[s[r]] = 1 + freq.get(s[r],0)
        maxf = max(maxf , freq[s[r]])

        while ((r-l) + 1) - maxf > k:
            freq[s[l]] -= 1
            l += 1
        maxlen = max(maxlen , r - l + 1)

    return maxlen

print(longest_substring_repeating_k('AAABABB' , 1))
        
