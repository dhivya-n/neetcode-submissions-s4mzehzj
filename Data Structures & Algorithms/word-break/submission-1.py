class Solution:
    def wordBreak(self, s: str, wordDict: List[str], i = 0, lookup = None) -> bool:
        if i == len(s):
            return True
        lookup = {} if lookup is None else lookup

        if i in lookup:
            return lookup[i]
        for word in wordDict:
            if word == s[i:i+len(word)]:
                res = self.wordBreak(s, wordDict, i+len(word), lookup)
                if res:
                    lookup[i] = True
                    return True
        lookup[i] = False
        return False
