combination =[]
def dice(n , c = []):
    if not n:
        combination.append(c[:])
        return
    else:
        for i in range (1,7):
            if i <= n:
                c.append(i)
                dice(n-i , c)
                c.pop()
dice(12)
print(combination)