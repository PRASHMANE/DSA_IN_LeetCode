class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        visited=[[0]*m for i in range(n)]


        def dfs(visited,grid,row,col,n,m):
            stack=[]
            stack.append([row,col])
            while stack:
                p=stack.pop()
                r=p[0]
                c=p[1]
                for i in range(r-1,r+2):
                    for j in range(c-1,c+2):
                        if 0<=i<n and 0<=j<m:
                            if abs(i-r) != abs(j-c) and grid[i][j]==1 and visited[i][j]==0:
                                visited[i][j]=1
                                stack.append([i,j])
    

        # find the edge element
        for i in range(n):
            for j in range(m):
                if i==0 or i==n-1:
                    if grid[i][j]==1 and visited[i][j]!=1:
                        visited[i][j]=1
                        dfs(visited,grid,i,j,n,m)
                else:
                    if j==0 or j==m-1:
                        if grid[i][j]==1 and visited[i][j]!=1:
                            visited[i][j]=1
                            dfs(visited,grid,i,j,n,m)
        count=0
        for i in range(n):
            for j in range(m):
                if grid[i][j]==1 and visited[i][j]!=1:
                    count+=1
        return count
        