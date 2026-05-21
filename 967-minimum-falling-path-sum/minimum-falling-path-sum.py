class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:

        n = len(matrix)
        
        dp = [[0] * n for _ in range(n)]

        for i in range(n):
            dp[0][i] = matrix[0][i]

        for i in range(1,n):
            for j in range(n):

                down = matrix[i][j]+dp[i-1][j]

                if j > 0 :
                    left = matrix[i][j]+dp[i-1][j-1]
                else:

                    left = float("inf")
                
                if j < n-1:
                    right = matrix[i][j]+dp[i-1][j+1]
                else:
                    right = float("inf")
                

                dp[i][j] = min(down,left,right)
            
        return min(dp[-1])
