class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        while l < r:
            m = math.floor((l+r)/2)
            if m == l:
                return min(nums[r], nums[l])
            if nums[l] > nums[m]:
                r = m
            elif nums[m] > nums[r]:
                l = m
            else:
                return nums[l]
        return min(nums[l], nums[r])
        