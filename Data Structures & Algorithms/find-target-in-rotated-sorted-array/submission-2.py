class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l , r = 0, len(nums)-1
        if r == 0:
            return 0 if nums[r] == target else -1
        while l < r:
            if nums[l] == target:
                return l
            if nums[r] == target:
                return r
            m = (l + r ) // 2
            if nums[m] == target:
                return m

            if l == m:
                break
            if nums[l] < nums[r]:
                if target < nums[m]:
                    r = m
                else:
                    l = m+1
            if nums[l] < nums[m]:
                if target > nums[l] and target < nums[m]:
                    r = m
                else:
                    l = m+1
            else:
                if target < nums[m]:
                    r = m
                else:
                    l = m+1
        return -1