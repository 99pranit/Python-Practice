def reverseBits(n):
    bi = ''
    for i in range(32):
        if n & (1<<i):
            bi += '1'
        else:
            bi += '0'

    res = 0
    for i , bit in enumerate(bi[::-1]):
        res = res|int(bit)* (1<<i)
    return res

print(reverseBits(4))