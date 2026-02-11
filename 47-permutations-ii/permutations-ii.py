class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        nums.sort()                     # 1️⃣ start from smallest permutation
        ans = [nums[:]]                 # 2️⃣ store copy
        n = len(nums)
        temp = nums[:]

        while True:
            ind = -1

            # find pivot
            for i in range(n-2, -1, -1):
                if nums[i] < nums[i+1]:
                    ind = i
                    break

            if ind == -1:
                break

            # find next greater element
            for i in range(n-1, ind, -1):
                if nums[i] > nums[ind]:
                    nums[i], nums[ind] = nums[ind], nums[i]
                    break

            # reverse suffix
            nums[ind+1:] = reversed(nums[ind+1:])
            ans.append(nums[:])         # 3️⃣ append copy

        return ans