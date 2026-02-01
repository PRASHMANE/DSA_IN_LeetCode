class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        nums.sort()
        count=Counter(nums)
        count=dict(sorted(count.items(),key=lambda x:x[1],reverse=True))

        for i in count:
            if i%2 == 0:
                return i
        return -1
        