class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # logic, fast and slow pointer
        l = 0
        r = 1
        maxV = 0
        while (r < len(prices)):
            profit = prices[r] - prices[l] 
            if (profit < 0):
                l = r
            elif (profit > maxV):
                maxV = profit
            r += 1
        return maxV