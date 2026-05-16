class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        n = len(cost)

        dp = [-1] * n

        def cost1(ind):
            if ind >= n:
                return 0

            if dp[ind] != -1:
                return dp[ind]

            fl = cost1(ind+1)+cost[ind]
            fr = cost1(ind+2)+cost[ind]

            dp[ind] = min(fl,fr)

            return dp[ind]
        
        return min(cost1(0),cost1(1))