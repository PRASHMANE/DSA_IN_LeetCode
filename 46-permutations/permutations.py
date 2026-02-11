class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        
        ans=[]
        ans.append(nums[:])
        n=len(nums)

        while True:

            ind=-1

            for i in range(n-2,-1,-1):
                if nums[i] < nums[i+1]:
                    ind=i
                    break
            
            if ind == -1:
                break
            
            for i in range(n-1,ind,-1):
                if nums[ind] < nums[i]:
                    nums[ind],nums[i]=nums[i],nums[ind]
                    break

            nums[ind+1:]=reversed(nums[ind+1:])

            ans.append(nums[:])
        
        #ans.sort()
        
        return ans
