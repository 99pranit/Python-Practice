def maxProfit(prices):
    l = 0 
    maxprofit = float('-inf')
    for i in range(len(prices)):
        maxprofit = max(maxprofit , prices[i] - prices[l])
        if prices[l] > prices[i]:
            l = i

    return maxprofit

print(maxProfit([10,1,5,6,7,1]))