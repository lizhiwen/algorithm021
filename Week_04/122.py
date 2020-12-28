class Solution:
    def maxProfit(self, prices):
        size = len(prices)

        ans = 0
        for i in range(1, size):
            ans += max(0, prices[i]-prices[i-1])
        return ans