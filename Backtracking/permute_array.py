pattern = []
def permute(n , c):
    if not n:
        pattern.append(c)
        return
    else:
        for i in range(len(n)):
            c1 = c + [n[i]]
            n1 = n[:i] + n[i+1:]
            permute(n1,c1)
    
permute([1,2,3],[])
print(pattern)