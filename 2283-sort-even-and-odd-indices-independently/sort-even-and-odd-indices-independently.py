class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        odd=[]
        even=[]
        for i in range(len(nums)):
            if i % 2 == 0:
                even.append(nums[i])
            else:
                odd.append(nums[i])
        odd.sort(reverse=True)
        even.sort()
        ans=[]
        for i,j in zip(even,odd):
            ans.append(i)
            ans.append(j)
        lo=len(odd)
        le=len(even)
        if lo > le:
            for i in odd[le:]:
                ans.append(i)
        else:
            for i in even[lo:]:
                ans.append(i)
        return ans
        