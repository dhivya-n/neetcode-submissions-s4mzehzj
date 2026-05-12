class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        return self.lcs(text1, text2)

    def lcs(self, s1, s2, i = 0, j = 0, lookup = None):
        if i >= len(s1) or j >= len(s2):
            return 0
        lookup = {} if lookup is None else lookup

        if (i,j) in lookup:
            return lookup[(i,j)]
        if s1[i] == s2[j]:
            lookup[(i,j)] = 1+self.lcs(s1, s2, i+1, j+1, lookup)
        else:
            lookup[(i,j)] = max(self.lcs(s1, s2, i, j+1, lookup), self.lcs(s1, s2, i+1, j, lookup))
        return lookup[(i,j)]

        