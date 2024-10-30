pattern =[]
def permutation(s, c=""):
    if not s:
        pattern.append(c)
    else:
        for i in range(0 , len(s)):
            c1 = c + s[i]
            s1 = s[:i] + s[i+1:]
            permutation(s1, c1)

        
s = "abc"
permutation(s)
print(pattern)
