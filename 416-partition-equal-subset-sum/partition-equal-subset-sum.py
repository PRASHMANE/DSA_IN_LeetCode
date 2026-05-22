class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        total = sum(nums)
        n = len(nums)
        if total%2 != 0:
            return False
        
        total = total // 2

        dp = [[-1] * (total+1) for _ in range(n)]

        def solve(i,t):

            if t == 0:
                return True
            if i == 0:
                return t == nums[i]

            if dp[i][t] != -1:
                return dp[i][t]
            
            not_take = solve(i-1,t)
            take = False

            if nums[i] <= t:
                take = solve(i-1,t-nums[i])
            
            dp[i][t]= take or not_take

            return dp[i][t]
        
        return solve(n-1,total)
        