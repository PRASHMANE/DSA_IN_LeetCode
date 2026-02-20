class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0

        total = 0
        cur = 0

        # Loop from the 3rd element
        for i in range(2, len(nums)):
            # Check if the current triple continues the arithmetic pattern
            if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
                cur += 1  # extend arithmetic slices
                total += cur
            else:
                cur = 0  # reset

        return total