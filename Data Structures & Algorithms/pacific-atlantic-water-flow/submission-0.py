from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
      m = len(heights)
      n = len(heights[0])
      pacificReachable = set()
      atlanticReachable = set()
      
      def dfs(i, j, prev):
         if i < 0 or j < 0 or i == m or j == n or heights[i][j] < prev or (i,j) in visited:
            return
         visited.add((i,j))
         dfs(i+1, j, heights[i][j])
         dfs(i, j+1, heights[i][j])
         dfs(i-1, j, heights[i][j])
         dfs(i, j-1, heights[i][j])

      visited = set()
      for j in range(n):
         dfs(0, j, heights[0][j])
      for i in range(m):
         dfs(i, 0, heights[i][0])
      atlanticReachable = visited

      visited = set()
      for j in range(n):
         dfs(m-1, j, heights[m-1][j])
      for i in range(m):
         dfs(i, n-1, heights[i][n-1])
      pacificReachable = visited

      result = []
      for cell in atlanticReachable:
         if cell in pacificReachable:
            result.append(list(cell))

      return result