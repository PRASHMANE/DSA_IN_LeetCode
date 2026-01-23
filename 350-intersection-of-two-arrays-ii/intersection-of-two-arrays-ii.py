class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        nu1=Counter(nums1)
        nu2=Counter(nums2)

        count=nu1 & nu2

        res=[]

        for i in count:
            res.extend([i]*count[i])
        return res

        