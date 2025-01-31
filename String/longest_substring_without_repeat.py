def longest_substring_without_repeat(s):
    if not s:
        return 0
    
    l , r = 0 , 1
    current = 1
    maxlen = 0
    n = len(s)
    while current != n:
        if s[current] not in s[l:r]:
            maxlen = max(maxlen , len(s[l:r]))
        else:
            while s[current] in s[l:r] and l < r:
                l += 1
        r += 1
        current += 1

    return maxlen + 1

print(longest_substring_without_repeat('pwwkew'))