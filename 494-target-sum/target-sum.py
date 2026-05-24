class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        total = sum(nums)

        if target+total < 0 or (target+total) % 2:
            return 0
        
        k = (total+target) // 2
        n = len(nums)

        dp = [[-1]*(k+1) for _ in range(n)]

        def solve(i,t):
            if i == 0:
                if t == 0 and nums[0] == 0:
                    return 2
                if t == 0 or nums[0] == t:
                    return 1
                return 0
            if dp[i][t] != -1:
                return dp[i][t]

            not_take = solve(i-1,t)
            take = 0
            if nums[i] <= t:
                take = solve(i-1,t-nums[i])
            
            dp[i][t]= take+not_take
            return dp[i][t]
        return solve(n-1,k)

        return k
        