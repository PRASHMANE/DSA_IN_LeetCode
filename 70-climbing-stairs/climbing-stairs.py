class Solution:
    def climbStairs(self, n: int) -> int:

        if n<=1:
            return n

        
        dp = [-1] * (n+1)

        def climb(i):
            if i <= 1:
                return 1
            
            if dp[i] != -1:
                return dp[i]

            dp[i] = climb(i-1)+climb(i-2)

            return dp[i]
        climb(n)
        return dp[n]
        