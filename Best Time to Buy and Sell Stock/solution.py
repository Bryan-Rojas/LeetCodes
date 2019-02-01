def maxProfit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    if not prices or len(prices) is 1:
        return 0

    profit = 0

    for i in range(1, len(prices)):
        if prices[i] > prices[i-1]:
            profit += prices[i] - prices[i-1]

    return profit

input1 = [7, 1, 5, 3, 6, 4]
input2 = [1, 2, 3, 4, 5]
input3 = [7, 6, 4, 3, 1]

print(maxProfit(input1))
print(maxProfit(input2))
print(maxProfit(input3))