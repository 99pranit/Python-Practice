def daily_temperature(temperatures):
    res = [0 for _ in range(len(temperatures))]
    stack = []

    for i , temp in enumerate(temperatures):
        while stack and stack[-1][0] < temp:
            stackT , stackI = stack.pop()
            res[stackI] = i - stackI
        stack.append((temp,i))

    return res

print(daily_temperature([30,38,30,36,35,40,28]))