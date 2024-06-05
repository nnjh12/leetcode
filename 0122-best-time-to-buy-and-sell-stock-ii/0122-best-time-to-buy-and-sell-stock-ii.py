class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        # compare the price of (i-1)th and ith day
        # if the price increse, increase the profit
        for i in range(1, len(prices)):
            diff = prices[i] - prices[i-1]
            if diff > 0 :
                profit += diff

        return profit
        