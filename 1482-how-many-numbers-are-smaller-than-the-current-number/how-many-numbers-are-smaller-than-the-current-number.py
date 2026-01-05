class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans=[]
        count=0
        for i in range(len(nums)):
            for j in range (len(nums)):
                if i!=j:
                    if nums[i] > nums[j]:
                        count+=1
            ans.append(count)
            count=0
        return ans
        