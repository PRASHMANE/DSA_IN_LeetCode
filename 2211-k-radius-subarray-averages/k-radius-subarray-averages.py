class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:

        n = len(nums)
        ans = [-1] * n
        window = 2 * k + 1

        if n < window:
            return ans

        total = sum(nums[:window])
        ans[k] = total // window

        for i in range(window, n):
            total += nums[i]
            total -= nums[i - window]
            ans[i - k] = total // window

        return ans