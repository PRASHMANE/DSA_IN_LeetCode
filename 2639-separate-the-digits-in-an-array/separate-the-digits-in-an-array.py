class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:

        hsh = defaultdict(list)

        for i in range(len(nums)):
            for j in str(nums[i]):
                hsh[i].append(int(j))
        
        ans = []

        for i in hsh:
            ans.extend(hsh[i])
        
        return ans
        