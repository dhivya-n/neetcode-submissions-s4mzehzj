class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        res = min(nums[l], nums[r])
        while l < r:
            m = math.floor((l+r)/2)
            if nums[l] > nums[m]:
                r = m-1
                res = min(res, nums[m])
            elif nums[m] > nums[r]:
                l = m+1
                res = min(res, nums[r])
            else:
                # print("here", r, l, m)
                return min(nums[l], res)
        return res
        