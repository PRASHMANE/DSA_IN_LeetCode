class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count=Counter(nums)
        n = float("inf")
        maxi=0
        for i in count:
            if count[i] > maxi :
                n = i
                maxi = count[i]
        return n
                