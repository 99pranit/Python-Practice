def reverse(n , s = 0):
    if n == 0:
        return s
    else:
        s = s * 10 + n % 10
        return reverse(n // 10 , s)
    
print(reverse(1234))