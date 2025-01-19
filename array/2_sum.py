def two_sum(a , target):
    prev_sum = {}
    for i in range(0 , len(a)):
        diff = target - a[i]
        if diff in prev_sum:
            return [prev_sum[diff] , i]
        else:
            prev_sum[a[i]] = i

a = [1 , 2 , 3 , 4 , 5]
target = 5
print(two_sum(a , target))