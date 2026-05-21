class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:

        n = len(matrix)
        m = len(matrix[0])

        ans = float("inf")

        dp = [[None] * m for i in range(n)]
        

        def solve(i,j):

            if j < 0 or j > m-1:
                return float("inf")
            
            if i == n-1:
                return matrix[i][j]
            
            if dp[i][j] != None:
                return dp[i][j]
            
            down = matrix[i][j]+solve(i+1,j)
            left = matrix[i][j]+solve(i+1,j-1)
            right = matrix[i][j]+solve(i+1,j+1)

            dp[i][j] = min(down,left,right)

            return dp[i][j]

        for i in range(m):
            ans = min(ans,solve(0,i))
        
        return ans
            
            

        