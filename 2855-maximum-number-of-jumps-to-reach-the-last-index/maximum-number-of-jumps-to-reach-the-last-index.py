class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        
        n = len(nums)
        dp = [-2] * n   # -2 = not visited

        def dfs(i):
            if i == n - 1:
                return 0

            if dp[i] != -2:
                return dp[i]

            max_jumps = -1

            for j in range(i + 1, n):
                if abs(nums[i] - nums[j]) <= target:
                    result = dfs(j)
                    if result != -1:
                        max_jumps = max(max_jumps, 1 + result)

            dp[i] = max_jumps
            return dp[i]

        return dfs(0)