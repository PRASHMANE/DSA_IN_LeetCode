class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        ans = set()

        n = len(nums)

        for i in range(n):
            seen = set()

            for j in range(i+1,n):
                three = -(nums[i]+nums[j])

                if three in seen:
                    temp = [nums[i],nums[j],three]
                    temp.sort()
                    ans.add(tuple(temp))
                
                seen.add(nums[j])
        return list(ans)
        