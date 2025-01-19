'''
Given two integers a and b, return the sum of the two integers 
without using the + and - operators.
'''
def sum_int(a , b):
    MAX = 0x7FFFFFFF
    MASK = 0xFFFFFFFF
    while b:
        carry = (a&b) << 1
        a = (a ^ b) & MASK
        b = carry & MASK
    return a if a <= MAX else ~(a ^ MASK)

print(sum_int(-1,-4))