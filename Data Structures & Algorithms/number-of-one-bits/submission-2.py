class Solution:
    def hammingWeight(self, n: int) -> int:
        # Way 1 - & with that digit
        # res = 0
        # for i in range(32):
        #     if (1 << i) & n:
        #         res += 1
        # return res

        # Way - 2 Move each bit and check the most significant bit alone
        # res = 0
        # while n > 0:
        #     if n & 1:
        #         res += 1
        #     n>>=1
        # return res

        # Way - 3 - use the buildin function
        # return bin(n).count('1')

        # way - 4 Negatiting till the latest one
        res = 0
        while n > 0:
            n = n & n-1
            res+=1
        return res
