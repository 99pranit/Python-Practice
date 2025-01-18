def countBits(n):
    if not n:
        return [0]
    res = [0] * (n+1) 
    for i in range(n+1):
        res[i] = res[i>>1] + (i&1)
    return res


print(countBits(4))