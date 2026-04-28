class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        stack = []
        hsh={}

        for i in nums2:
            while stack and  i > stack[-1]:
                hsh[stack.pop()] = i
            stack.append(i)
        
        while stack:
            hsh[stack.pop()] = -1
        
        return [hsh[i] for i in nums1]