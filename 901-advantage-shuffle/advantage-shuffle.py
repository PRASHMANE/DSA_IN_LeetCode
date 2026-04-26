class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums1)

        nums1.sort()

        num_2 = sorted([(val,i) for i , val in enumerate(nums2)],reverse=True)

        left = 0
        right = n-1
        ans=[0]*n
        for val , ind in num_2:
            if nums1[right] > val:
                ans[ind] = nums1[right]
                right-=1
            else:
                ans[ind] = nums1[left]
                left+=1
        return ans
