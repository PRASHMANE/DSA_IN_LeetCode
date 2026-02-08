class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        ans = 0
        mask = 0
        l = 0
        
        for r, num in enumerate(nums):
            # Shrink window until no bit conflict
            while mask & num:
                mask ^= nums[l]
                l += 1
            # Add current to mask
            mask |= num
            # Update result
            ans = max(ans, r - l + 1)
        
        return ans