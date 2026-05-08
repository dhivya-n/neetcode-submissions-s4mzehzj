class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        maxFromRight = [ 0 ] * n
        maxFromRight[n-1] = prices[n-1]
        for i in range(n-2, -1, -1):
            maxFromRight[i] = max(maxFromRight[i+1], prices[i])
        maxProf = 0
        for i in range(n-1):
            curr = maxFromRight[i+1] - prices[i] 
            maxProf = max(maxProf, curr)
        return maxProf
