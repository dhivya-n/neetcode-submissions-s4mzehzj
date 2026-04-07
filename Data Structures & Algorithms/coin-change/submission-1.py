class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        lookup = {}
        import sys
        sys.setrecursionlimit(20000)
        def canMake(amount):
            if amount == 0:
                return 0
            if amount < 0:
                return -1
            if amount in lookup:
                return lookup[amount]

            result = float("inf")
            for coin in coins:
                current = canMake(amount - coin)
                if current != -1:
                    result = min(result, 1+current)
            lookup[amount] = -1 if result == float("inf") else result
            return lookup[amount]
        return canMake(amount)