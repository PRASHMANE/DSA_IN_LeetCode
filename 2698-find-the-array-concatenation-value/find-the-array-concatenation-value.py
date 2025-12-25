class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        l=0
        r=len(nums)-1
        ans=0
        while l <= r:
            if l==r:
                ans+=nums[l]
            else:
                con = int(str(nums[l])+str(nums[r]))
                ans+=con
            l+=1
            r-=1
        return ans
        