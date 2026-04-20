class Solution:
   def threeSum(self, nums: List[int]):
        counter = {}
        n = len(nums)
        for num in nums:
            counter[num] = counter.get(num, 0) + 1
        
        result = set()
        for i in range(n-2):
            counter[nums[i]]-=1
            for j in range(i + 1, n-1):
                counter[nums[j]]-=1
                expected = - (nums[i] + nums[j])
                if expected in counter and counter[expected] > 0:
                    result.add(tuple(sorted([nums[i], nums[j],expected])))
                counter[nums[j]]+=1
            counter[nums[i]]+=1
        return [list(x) for x in result]