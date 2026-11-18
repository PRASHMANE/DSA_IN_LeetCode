class Solution:
    def numEnclaves(self, grid: list[list[int]]) -> int:
        m,n = len(grid),len(grid[0])
        if not grid:
            return 

        def dfs(r,c):
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == 0:
                return
            grid[r][c] = 0
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

        for i in range(m):
            if grid[i][0] == 1:
                dfs(i,0)
            if grid[i][n-1] == 1:
                dfs(i,n-1)

        for j in range(n):
            if grid[0][j] == 1:
                dfs(0,j)
            if grid[m-1][j] == 1:
                dfs(m-1,j)

        count = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    count+=1
        return count
        

        