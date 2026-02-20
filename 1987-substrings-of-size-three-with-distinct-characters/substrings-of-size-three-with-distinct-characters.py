class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        n=len(s)
        count=0

        for i in range(n):
            for j in range(i,n):
                if j-i+1 == 3:
                    if len(set(s[i:j+1])) == 3:
                        count +=1
                elif j-i+1 > 3:
                    break
        return count
