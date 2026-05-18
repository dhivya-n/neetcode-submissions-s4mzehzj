class Solution:
    def canJump(self, nums: List[int], index = 0, lookup = None) -> bool:
        import sys
        sys.setrecursionlimit(2000)
        if index >= len(nums)-1:
            return True
        lookup = {} if lookup is None else lookup

        if index in lookup:
            return lookup[index]
        
        possibleJump = nums[index]
        for i in range(index+1, index + possibleJump+1):
            jump = self.canJump(nums, i, lookup)
            if jump == True:
                return True
        lookup[index] = False
        return lookup[index]
