class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()             # sort scores
        ans = float("inf")      # start with a very large value
        
        # slide a window of length k
        for i in range(len(nums) - k + 1):
            diff = nums[i + k - 1] - nums[i]
            ans = min(ans, diff)
        
        return ans