class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices)<1: 
            return 0
        profit=0
        minprice=prices[0]
        for i in range(1,len(prices)):
            minprice=min(minprice, prices[i])
            profit=max(profit,prices[i]-minprice)
        return profit
            