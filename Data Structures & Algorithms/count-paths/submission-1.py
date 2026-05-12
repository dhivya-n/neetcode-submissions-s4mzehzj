class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        prev_dp = [1] * n
        dp = [0] * n

        for i in range(1, m):
            dp[0] = prev_dp[0]
            for j in range(1, n):
                dp[j] = prev_dp[j] + dp[j-1]
            prev_dp = dp

        return prev_dp[n-1]
