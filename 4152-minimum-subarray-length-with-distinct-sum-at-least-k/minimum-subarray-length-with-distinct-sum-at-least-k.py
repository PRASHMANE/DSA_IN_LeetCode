class Solution:
    def minLength(self, nums: List[int], k: int) -> int:

        from collections import defaultdict

        freq = defaultdict(int)
        distinct_sum = 0
        left = 0
        res = float('inf')

        for right in range(len(nums)):
            # add nums[right]
            if freq[nums[right]] == 0:
                distinct_sum += nums[right]
            freq[nums[right]] += 1

            # try shrinking from left while sum >= k
            while distinct_sum >= k:
                res = min(res, right - left + 1)
                # remove nums[left]
                freq[nums[left]] -= 1
                if freq[nums[left]] == 0:
                    distinct_sum -= nums[left]
                left += 1

        return res if res != float('inf') else -1