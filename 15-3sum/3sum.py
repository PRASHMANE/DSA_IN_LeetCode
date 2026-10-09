class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        ans = []

        for i in range(n-2):
            
            if i>0 and nums[i-1] == nums[i]:
                continue
            
            left = i+1
            right = n-1

            while left < right:
                sum = nums[left]+nums[right]+nums[i]

                if sum == 0:
                    ans.append([nums[i],nums[left],nums[right]])
                    left+=1
                    right-=1

                    while left<right and nums[left] == nums[left-1]:
                        left+=1
                    while left<right and nums[right] == nums[right+1]:
                        right-=1
                elif sum < 0:
                    left+=1
                else:
                    right-=1
        return ans