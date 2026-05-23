class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        INF = float("inf")
        n = len(coins)

        dp = [[0]* (amount+1) for _ in range(n)]

        def solve(i,t):
            if i == 0:
                if t % coins[0] == 0:
                    return t // coins[0]
                return INF
            if dp[i][t] != 0:
                return dp[i][t]

            not_take = solve(i-1,t)
            take = INF
            if coins[i] <= t:
                take = 1 + solve(i,t-coins[i])
            
            dp[i][t]= min(not_take,take)
            return dp[i][t]
        
        ans =  solve(n-1,amount)

        if ans == INF:
            return -1
        return ans

        