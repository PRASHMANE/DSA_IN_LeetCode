from collections import Counter
class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        l=len(s)
        n=l-1
        count= Counter(s)
        one = count["1"]
        ans=""
        if l <= 1:
            return s
        if one == 1:
            for i in range(l):
                if i != l-1:
                    ans+="0"
                else:
                    ans+="1"
            return ans 
        
        for i in range(l):
            if one > 1 :
                ans+="1"
                one-=1
            else:
                if i != l-1:
                    ans+="0"
                else:
                    ans+="1"
        return ans


        