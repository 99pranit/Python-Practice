def count_zero(n , c = 0):
    if n == 0:
        return c
    elif n % 10 == 0:
        c = c + 1
        return count_zero(n // 10 , c)
    else:
        return count_zero( n // 10 , c)

print(count_zero(23040))