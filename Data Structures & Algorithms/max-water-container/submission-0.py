class Solution:
    def maxArea(self, heights: List[int]) -> int:
       n = len(heights)
       water = 0
       for i in range(n):
        for j in range(i+1, n):
            water = max(water, min(heights[i], heights[j])*(j-i))
       return water