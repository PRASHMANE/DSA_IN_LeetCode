class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        left = 0
        right = 0
        res = 0

        while left < len(nums1) and right < len(nums2):
            if nums1[left] <= nums2[right]:
                res = max(res, right - left)
                right += 1
            else:
                left += 1

        return res