def pattern(n):
    size = 2 * n 
    for i in range(size):
        for j in range(size):
            dist = min(i, j, size - i - 1, size - j - 1)
            print(dist + 1, end=' ')
        print()

pattern(3)
