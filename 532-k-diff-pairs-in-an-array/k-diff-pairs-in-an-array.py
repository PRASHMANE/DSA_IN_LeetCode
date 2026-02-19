class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k < 0:  # no pairs possible when k is negative
            return 0

        freq = {}
        # Build frequency map
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        count = 0
        for num in freq:
            if k == 0:
                # need at least two of same number for a 0-diff pair
                if freq[num] > 1:
                    count += 1
            else:
                # check if num + k exists for unique pair
                if (num + k) in freq:
                    count += 1

        return count