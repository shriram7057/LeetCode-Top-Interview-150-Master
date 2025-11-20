class Solution(object):
    def maxProfit(self, k, prices):
        n = len(prices)
        if n == 0 or k == 0:
            return 0

        if k >= n // 2:
            profit = 0
            for i in range(1, n):
                if prices[i] > prices[i - 1]:
                    profit += prices[i] - prices[i - 1]
            return profit

        dp = [[0] * n for _ in range(k + 1)]

        for t in range(1, k + 1):
            best = -prices[0]
            for i in range(1, n):
                dp[t][i] = max(dp[t][i - 1], prices[i] + best)
                best = max(best, dp[t - 1][i] - prices[i])

        return dp[k][n - 1]
