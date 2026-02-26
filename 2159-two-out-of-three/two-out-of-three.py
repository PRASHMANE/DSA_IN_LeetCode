class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        ans=[]
        hsh1={}
        hsh2={}
        hsh3={}
        uni=set()

        for i in nums1:
            hsh1[i]=1
            uni.add(i)
        
        for i in nums2:
            hsh2[i]=1
            uni.add(i)
        
        for i in nums3:
            hsh3[i]=1
            uni.add(i)
        
        for i in uni:
            if hsh1.get(i,0)+hsh2.get(i,0)+hsh3.get(i,0) >= 2:
                ans.append(i)
        return ans
        

        