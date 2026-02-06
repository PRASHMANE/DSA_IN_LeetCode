class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        n=len(nums)
        ans=[0]*n
        nums.sort()
        left=0
        right=n-1
        for i in nums:
            if i % 2 == 0:
                ans[left]=i
                left+=1
            else:
                ans[right]=i
                right-=1
        return ans
        