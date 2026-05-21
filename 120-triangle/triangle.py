class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
    
        n = len(triangle)
        m = len(triangle[0])

        dp = [[None]* (i+1) for i in range(n)]

        if n == 1 and m == 1:
            return triangle[0][0]
        
        def solve(r,c):

            if r == n-1 :
                return triangle[r][c]
            
            if dp[r][c] is not None:
                return dp[r][c]
            
            row = triangle[r][c]+solve(r+1,c)
            col = triangle[r][c]+solve(r+1,c+1)

            dp[r][c] = min(row,col)
            

            return dp[r][c]
        
        return solve(0,0)


        
        