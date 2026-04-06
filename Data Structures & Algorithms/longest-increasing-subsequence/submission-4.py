class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        import sys
        sys.setrecursionlimit(2000)
        def lcs(s, i = 0, lastIndex = None, lookup = None):
            if i == len(s):
                return 0
    
            lookup = {} if lookup is None else lookup

            if (i, lastIndex) in lookup:
                return lookup[(i, lastIndex)]

            #delete current element
            res = lcs(s, i+1, lastIndex, lookup)

            #select current element
            if lastIndex == None or s[i] > s[lastIndex]:
                res = max(res, 1+lcs(s, i+1, i, lookup))
            
            lookup[(i, lastIndex)] = res
            return res
        return lcs(nums)