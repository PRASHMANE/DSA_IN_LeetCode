class Solution:
    def reverseWords(self, s: str) -> str:
        st=s.split(" ")
        for i in range(len(st)):
            st[i]=st[i][::-1]
        
        st = " ".join(st)
        return st
        