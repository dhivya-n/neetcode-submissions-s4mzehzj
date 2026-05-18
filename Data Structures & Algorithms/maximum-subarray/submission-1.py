class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total = nums[0]
        maxTotal = nums[0]
        for i in range(1, len(nums)):
            if total < 0 and total < nums[i]:
                total = nums[i]
            else:
                total += nums[i]
            maxTotal = max(maxTotal, total)
        return maxTotal
        