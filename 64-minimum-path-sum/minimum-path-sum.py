class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        n = len(grid)
        m = len(grid[0])

        dp = [[-1]*m for _ in range(n)]

        def solve(i,j):
            if i==0 and j==0:
                return grid[0][0]
            
            if i < 0 or j < 0:
                return float('inf')
            
            if dp[i][j] != -1:
                return dp[i][j]
            
            up = grid[i][j]+solve(i-1,j)
            left = grid[i][j]+solve(i,j-1)

            dp[i][j] = min(up,left)

            return dp[i][j]

        return solve(n-1,m-1)


        