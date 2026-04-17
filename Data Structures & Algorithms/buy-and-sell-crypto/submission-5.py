class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # max profit var
        # two pointers
        left = 0
        right = 0
        maxProfit = 0

        while right < len(prices):
            if prices[right] < prices[left]:
                left = right
            curProfit = prices[right] - prices[left]
            maxProfit = max(maxProfit, curProfit)
            right += 1
        
        return maxProfit