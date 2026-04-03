class Solution:
    # def rob(self, nums: List[int], i = 0, hasZeroRobbed = False, lookup = None) -> int:
    #     if i >= len(nums):
    #         return 0
    #     if i == len(nums)-1:
    #         #You can only rob is zero not robbed
    #         if hasZeroRobbed:
    #             return 0
    #         else:
    #             return nums[i]
    #     lookup = {} if lookup is None else lookup 

    #     if (i, hasZeroRobbed) in lookup:
    #         return lookup[(i, hasZeroRobbed)]
    #     rob = 0
    #     if i == 0:
    #         rob = nums[i] + self.rob(nums,i+2, True, lookup)
    #     else:
    #         rob = nums[i] + self.rob(nums,i+2, hasZeroRobbed, lookup)

    #     lookup[(i, hasZeroRobbed)] = max(rob, self.rob(nums,i+1, hasZeroRobbed, lookup))
    #     return lookup[(i, hasZeroRobbed)]

    # Bottomup
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]

        #Robzero
        rob1, rob2, rob = nums[0], max(nums[0], nums[1]), 0
        for i in range(2, n-1):
            rob = max(nums[i]+rob1, rob2)
            rob1 = rob2
            rob2 = rob
        result = max(rob2, rob1)

        #Don'tRobzero
        rob1, rob2, rob = 0, nums[1], 0
        for i in range(2, n):
            rob = max(nums[i]+rob1, rob2)
            rob1 = rob2
            rob2 = rob
        result = max(result, rob2, rob1)
        return result


        