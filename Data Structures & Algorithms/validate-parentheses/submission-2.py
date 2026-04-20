class Solution:
    def isValid(self, s: str) -> bool:
        open_b = ['(', '{', '[']
        result = []
        for char in s:
            if char in open_b:
                result.append(char)
            else:
                if len(result) == 0:
                    return False
                ele = result.pop()
                if ( ele == '[' and char == ']' ) or ( ele == '{' and char == '}' ) or ( ele == '(' and char == ')' ):
                    continue
                else:
                    return False
        return True if len(result) == 0 else False