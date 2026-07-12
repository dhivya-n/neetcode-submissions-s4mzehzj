class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        island = 0
        m, n = len(grid), len(grid[0])
        def dfs(i, j):
            if (i, j) in visited or i < 0 or j < 0 or i == m or j == n or grid[i][j] == '0':
                return
            visited.add((i,j))
            dfs(i-1, j)
            dfs(i, j-1)
            dfs(i+1, j)
            dfs(i, j+1)
            
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and  (i, j) not in visited :
                    island+=1
                    dfs(i,j)
        return island
        