class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        n = len(coins)

        dp = [[None] * (amount+1) for _ in range(n)]

        def solve(i ,t):
            if i == 0:
                if t % coins[0] == 0:
                    return 1
                return 0
            if dp[i][t] != None:
                return dp[i][t]
            not_take = solve(i-1,t)
            take =  0
            if coins[i] <= t:
                take = solve(i,t-coins[i])
            dp[i][t]=take+not_take
            return dp[i][t]
        return solve(n-1,amount)
        