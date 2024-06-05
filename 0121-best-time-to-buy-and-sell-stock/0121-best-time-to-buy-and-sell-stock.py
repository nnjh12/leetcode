class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # set min buying price to the value greater than first price 
        minBuyingPrice = prices[0]+1
        maxProfit = 0
        tempProfit = 0
       
        for price in prices:
            # if price is smaller than min buying price
            if price < minBuyingPrice:
                # set min buying price to price
                minBuyingPrice = price
                
                # if maxProft is greater than cur tempProfit
                if maxProfit > tempProfit:
                    # move max profit so far to tempProfit. 
                    tempProfit = maxProfit
            
            # calculate the profit
            profit = price - minBuyingPrice
            # if profit is greater than max profit so far
            if profit > maxProfit:
                # update max profit
                maxProfit = profit

        if maxProfit > tempProfit:
            return maxProfit
        else:
            return tempProfit      

    """
    Attempt1: Recursion. Not very efficient

    def maxProfit(self, prices: List[int]) -> int:
        # Base case: when there is only one price
        if len(prices) < 2:
            return 0
        # Base case: when there is only two prices
        elif len(prices) == 2:
            profit = prices[1] - prices[0]
            if profit > 0:
                return profit
            else:
                return 0

        # Find the max profit between buying stock at first index vs not-buying stock at first index
        profit = max(max(prices[1:]) - prices[0], self.maxProfit(prices[1:]))
        return profit
    """