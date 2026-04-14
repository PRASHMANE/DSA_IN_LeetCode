class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        buy =0
        sell = 1
        profit = 0

        while sell < n:
            if prices[sell] > prices[buy]:
                profit = max(profit,prices[sell]-prices[buy])
            else:
                buy=sell
            sell+=1
        
        return profit