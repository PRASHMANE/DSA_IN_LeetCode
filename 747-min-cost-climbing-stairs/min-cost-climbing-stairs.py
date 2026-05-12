class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        n = len(cost)

        if n <= 2:
            return min(cost)

        dp=[-1]*n

        def fun(ind):

            if ind == 0:
                return cost[ind]
            if ind < 0:
                return 0
            
            if dp[ind] != -1:
                return dp[ind]
            
            case1 = fun(ind-1)
            case2 = fun(ind-2)

            dp[ind] = min(case1,case2)+cost[ind]

            return dp[ind]
        
        fun(n-1)
        return min(dp[-1],dp[-2])
    