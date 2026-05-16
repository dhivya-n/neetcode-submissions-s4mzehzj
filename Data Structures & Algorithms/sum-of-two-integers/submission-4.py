class Solution:
    def getSum(self, a: int, b: int) -> int:
        result = 0
        carry = 0
        mask = 0xffffffff
        a = a & mask
        b = b & mask

        for i in range(32):
            a_d = (a >> i) & 1
            b_d = (b >> i) & 1
            result += ( a_d ^ b_d ^ carry ) << i
            if carry:
                carry = carry & (a_d | b_d)
            else:
                carry = a_d & b_d
        return result if result < 0x7fffffff else  ~ ( result ^ mask)
        
        