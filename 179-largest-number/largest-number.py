class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = list(map(str, nums))
        
        # custom comparator
        def compare(a, b):
            if a + b > b + a:
                return -1
            elif a + b < b + a:
                return 1
            else:
                return 0
        
        # sort using comparator
        nums.sort(key=cmp_to_key(compare))
        
        # edge case: when all are zeros
        if nums[0] == "0":
            return "0"
        
        return "".join(nums)