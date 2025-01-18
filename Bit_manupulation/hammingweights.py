def hammingWeight(n):
    count_1 = 0
    while n:
        if n%2 != 0:
            count_1 += 1
        n = n>>1
    return count_1

print(hammingWeight(6))