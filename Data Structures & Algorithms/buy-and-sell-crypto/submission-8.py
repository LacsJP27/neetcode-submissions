class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        l, r = 0, 1

        while r < len(prices):
            currProfit = prices[r] - prices[l]
            maxProfit = max(maxProfit, currProfit)

            if prices[r] <= prices[l]:
                l = r
            r += 1
            
        return maxProfit