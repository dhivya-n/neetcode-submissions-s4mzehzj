class Solution:
    #Recursion
    # def rob(self, nums: List[int], i = 0) -> int:
    #     if i >= len(nums):
    #         return 0
    #     return max((nums[i]+self.rob(nums, i+2)),self.rob(nums, i+1))

    # #TopDown
    # def rob(self, nums: List[int], i = 0, lookup = None) -> int:
    #     if i >= len(nums):
    #         return 0
    #     lookup = {} if lookup is None else lookup
    #     if i in lookup:
    #          return lookup[i]
    #     lookup[i] = max((nums[i]+self.rob(nums, i+2, lookup)),self.rob(nums, i+1, lookup))
    #     return lookup[i]

    # Bottomup
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[n-1]

        lookup = [0 for i in range(n)]

        lookup[0] = nums[0]
        lookup[1] = max(nums[1], nums[0])

        for i in range(2, n):
            lookup[i] = max(nums[i]+lookup[i-2], lookup[i-1])

        return max(lookup[n-1], lookup[n-2])
    # Bottomup - optimised
    # def rob(self, nums: List[int]) -> int:
    #     if len(nums) == 1:
    #         return nums[0]

    #     first_house = nums[0]
    #     second_house = nums[1]
    #     curr = 0

    #     for i in range(2, len(nums)):
    #         curr = max((nums[i] + first_house), second_house)
    #         first_house = second_house
    #         second_house = curr
    #     return max(second_house, first_house)