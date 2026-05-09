class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unichar = {}
        n = len(s)
        if n <= 1:
            return n

        result, l, r = 1, 0, 1
        unichar[s[0]] = 0
        while r < n: 
            
            if s[r] in unichar and unichar[s[r]] >= l:
                l = unichar[s[r]] + 1
            unichar[s[r]] = r
            result = max(result, (r-l)+1) 
            r = r + 1
        return result
        