class Solution:
    def numEnclaves(self, grid: list[list[int]]) -> int:
        m,n = len(grid),len(grid[0])
        if not grid:
            return 

        que = deque()

        for i in range(m):
            if grid[i][0] == 1:
                que.append((i,0))
                grid[i][0] = 0
            if grid[i][n-1] == 1:
                que.append((i,n-1))
                grid[i][n-1] = 0

        for j in range(n):
            if grid[0][j] == 1:
                que.append((0,j))
                grid[0][j] = 0
            if grid[m-1][j] == 1:
                que.append((m-1,j))
                grid[m-1][j] = 0
        
        dir = [(1,0),(-1,0),(0,1),(0,-1)]
        
        while que:
            r,c = que.popleft()
            for dr,dc in dir:
                nr,nc=r+dr,c+dc

                if 0 <= nr < m and 0 <= nc < n and grid[nr][nc] == 1:
                    grid[nr][nc] = 0
                    que.append((nr,nc))
        
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    count+=1
        return count