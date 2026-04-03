class Solution:
    def rob(self, nums: List[int], i = 0, hasZeroRobbed = False, lookup = None) -> int:
        if i >= len(nums):
            return 0
        if i == len(nums)-1:
            #You can only rob is zero not robbed
            if hasZeroRobbed:
                return 0
            else:
                return nums[i]
        lookup = {} if lookup is None else lookup 

        if (i, hasZeroRobbed) in lookup:
            return lookup[(i, hasZeroRobbed)]
        rob = 0
        if i == 0:
            rob = nums[i] + self.rob(nums,i+2, True, lookup)
        else:
            rob = nums[i] + self.rob(nums,i+2, hasZeroRobbed, lookup)

        lookup[(i, hasZeroRobbed)] = max(rob, self.rob(nums,i+1, hasZeroRobbed, lookup))
        return lookup[(i, hasZeroRobbed)]
        