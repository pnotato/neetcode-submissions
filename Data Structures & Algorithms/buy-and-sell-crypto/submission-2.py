class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1 # left is buy, right is sell
        maxP = 0

        while r < len(prices):
            # profitable?
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r
            r += 1

        return maxP

        # buy, sell = float('inf'), None
        # for i in prices:
        #     if i < buy or buy == float('inf'):
        #         buy = i
        #     elif not sell or i > sell:
        #         sell = i
        # return 0 if (sell == None) else sell - buy

