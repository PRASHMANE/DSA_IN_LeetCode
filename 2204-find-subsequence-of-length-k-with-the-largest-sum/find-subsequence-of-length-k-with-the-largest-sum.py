class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        
        # store value + index
        arr = []

        for i, num in enumerate(nums):
            arr.append((num, i))

        # sort by value descending
        arr.sort(reverse=True)

        # take top k
        arr = arr[:k]

        # restore original order
        arr.sort(key=lambda x: x[1])

        ans = []

        for val, idx in arr:
            ans.append(val)

        return ans