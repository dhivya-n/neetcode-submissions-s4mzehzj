class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            ele = ((n >> i) & 1)
            if ele:
                res += (1 << (31 - i) )
        return res
        