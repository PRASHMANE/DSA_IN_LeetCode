class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        hsh2={}

        for i in range(len(nums2)):
            found=False
            for j in range(i,len(nums2)):
                if nums2[i] < nums2[j]:
                    found=True
                    hsh2[nums2[i]] = nums2[j]
                    break
            if not found:
                hsh2[nums2[i]] = -1

        ans=[]

        for i in nums1:
            ans.append(hsh2[i])
        
        return ans