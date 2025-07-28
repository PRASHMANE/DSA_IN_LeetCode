class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        n=len(image)
        m=len(image[0])
        visit=[[0]*m for i in range(n)]
        fix_col=image[sr][sc]
        def dfs(visited,image,row,col,fix_col,color,n,m):
            visited[row][col]=1
            image[row][col]=color
            stack=[]
            stack.append([row,col])
            while stack:
                p=stack.pop()
                r=p[0]
                c=p[1]
                for i in range(r-1,r+2):
                    for j in range(c-1,c+2):
                        if 0<=i<n and 0<=j<m:
                            if abs(i-r) != abs(j-c) and image[i][j] == fix_col and visited[i][j]!=1:
                                visited[i][j]=1
                                image[i][j]=color
                                stack.append([i,j])
        dfs(visit,image,sr,sc,fix_col,color,n,m)
        return image


        
        