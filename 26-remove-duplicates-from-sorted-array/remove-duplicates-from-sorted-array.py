class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        uni = set()
        for i in nums:
            uni.add(i)
        uni = sorted(list(uni))
        ind=0
        for i in uni:
            nums[ind] = i
            ind+=1
        return ind