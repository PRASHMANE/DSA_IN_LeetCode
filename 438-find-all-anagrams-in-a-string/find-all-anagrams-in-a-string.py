class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        right = len(p)-1
        left=0
        n=len(s)

        val="".join(sorted(p))
        ans=[]

        while right < n:

            if "".join(sorted(s[left:right+1])) == val:
                ans.append(left)
            left+=1
            right+=1
        return ans
        