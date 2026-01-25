class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        def find_max(a):
            max1=a[0]
            max2=0

            for i in range(1,len(a)):
                if a[i] > max1 :
                    max2=max1
                    max1=a[i]
                else:
                    if a[i] > max2:
                        max2=a[i]
            return max1,max2

        max1,max2 = find_max(nums)
    
        if max2*2 <= max1:
            for i in range(len(nums)):
                if max1 == nums[i]:
                    return i
        return -1 



        
        