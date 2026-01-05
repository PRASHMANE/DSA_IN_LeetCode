class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:

        ans=[]
        nums.sort()
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                break
        val=nums[i]
        ans.append(val)
        n=len(nums)
        total= n*(n+1) / 2 
        rem = total - sum(nums)
        ans.append(int(val+rem))
        return ans
