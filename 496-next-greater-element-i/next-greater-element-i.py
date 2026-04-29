class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        stack = []
        hsh ={}

        for num in nums2:
            while stack and num > stack[-1]:
                hsh[stack.pop()] = num
            stack.append(num)
        
        while stack:
            hsh[stack.pop()] = -1
        

        return [hsh[val] for val in nums1]