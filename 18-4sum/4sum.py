class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        nums.sort()

        ans = set()

        for i in range(n):
            for j in range(i+1,n):
                left=j+1
                right=n-1
                while left < right:
                    sum = nums[i]+nums[j]+nums[left]+nums[right]
                    if sum == target:
                        temp = (nums[i],nums[j],nums[left],nums[right])
                        ans.add(temp)
                        left+=1
                        right-=1
                    elif sum < target:
                        left+=1
                    else:
                        right-=1
        return list(ans)

        