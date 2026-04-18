class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = Counter(nums)

        n = len(nums)
        ans = []

        for i in count.keys():
            if count[i] > n // 3:
                ans.append(i)
        
        return ans