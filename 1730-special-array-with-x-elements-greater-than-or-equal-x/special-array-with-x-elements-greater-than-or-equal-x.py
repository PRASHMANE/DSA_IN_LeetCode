class Solution:
    def specialArray(self, nums: List[int]) -> int:
        n = len(nums)
        # Try x from 1 to n
        for x in range(1, n + 1):
            # Count how many numbers >= x
            count = sum(num >= x for num in nums)
            if count == x:
                return x
        return -1