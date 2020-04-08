# Say you have an array for which the ith element is the price of a given stock on day i.
# Design an algorithm to find the maximum profit. You may complete as many transactions as you like

stock = [7, 1, 5, 3, 6, 4]
stock2 = [1, 2, 3, 4, 5]

def maxProfit(prices):
    if len(prices) < 2:
        return 0
    profit = 0
    for i in range(len(prices) - 1):
        if prices[i] < prices[i + 1]:
            profit += prices[i + 1] - prices[i]
    return profit

print(maxProfit(stock2))
