class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()

        n = len(nums)

        ans = set()

        for i in range(n):
            if(i>0 and nums[i] == nums[i-1]):
                continue
            left = i+1
            right = n -1

            while left < right:
                sum = nums[i]+nums[left]+nums[right]
                if sum == 0:
                    temp = (nums[i],nums[left],nums[right])
                    ans.add(temp)

                    left+=1
                    right-=1
                elif sum < 0:
                    left+=1
                else:
                    right-=1

        return list(ans)

            
