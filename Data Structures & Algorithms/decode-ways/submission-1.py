class Solution:
    def numDecodings(self, s: str) -> int:
        def decodeString(s, i , prev , lookup ):
            previous = int(prev) if prev != '' else ''
            if previous == 0:
                return 0
            if i == len(s):
                return 1 if previous == '' else 0
            if (i, previous) in lookup:
                return lookup[(i, previous)]
            res = 0
            if previous!= '':
                if (previous == 2 and 0<= int(s[i])<=6) or previous == 1:
                    res+=decodeString(s, i+1, '', lookup)
            elif previous == '' and s[i] != '0':
                res+=decodeString(s, i+1, s[i], lookup)
                res+=decodeString(s, i+1, '', lookup)
            lookup[(i, previous)] = res
            return res
        lookup = {}
        return decodeString(s, 0, '', lookup)
        