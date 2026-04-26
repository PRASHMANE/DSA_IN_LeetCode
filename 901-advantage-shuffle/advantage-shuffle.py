class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums1)
        nums1.sort()

        nums_2 = sorted([(val,i) for i , val in enumerate(nums2)],reverse=True)

        res = [0]*n

        left = 0
        right = n-1

        for val , ind in nums_2:
            if nums1[right] > val:
                res[ind] = nums1[right]
                right-=1
            else:
                res[ind] = nums1[left]
                left+=1
        return res