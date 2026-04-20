class Solution:
   def threeSum(self, nums: List[int]):
        nums.sort()
        result = []
        n = len(nums)
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            num1 = nums[i]
            j = i + 1
            k = len(nums)-1
            while(j<k):
                #target - num1
                if(nums[j] + nums[k] + num1 > 0):
                    k=k-1
                elif(nums[j] + nums[k] + num1 < 0):
                    j = j+1
                elif(nums[j] + nums[k] + num1 == 0):
                    result.append([nums[i], nums[j], nums[k]])
                    j+=1
                    k-=1
                    while nums[j] == nums[j-1] and j<k:
                        j+=1
                    while nums[k] == nums[k+1] and j<k:
                        k-=1    
        return result