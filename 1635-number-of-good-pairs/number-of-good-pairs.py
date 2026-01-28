class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        good_pairs = 0
        count = {}
        for x in nums:
            good_pairs += count.get(x, 0)
            count[x] = count.get(x, 0) + 1
        return good_pairs