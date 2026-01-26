class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:

        def count(a,row,col,n,m):
            dire=[(-1,0),(1,0),(0,-1),(0,1)]
            cnt=4
            for dr,dc in dire:
                nr = row+dr
                nc = col+dc
                if 0 <= nr < n and 0 <= nc < m:
                    if a[nr][nc] == 1:
                        cnt-=1
            return cnt

        n = len(grid)
        m = len(grid[0])
        ans=0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    ans+=count(grid,i,j,n,m)
        return ans
        