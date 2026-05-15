class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n+1)
        if n == 0:
            return [0]
        dp[1] = 1
        offset = 0
        for i in range(2, n+1):
            offset = i if i & (i-1) == 0 else offset
            dp[i] = 1 + dp[i-offset]
        return dp