class Solution:
    def maxScore(self, s: str) -> int:
        max_score=0
        l=0
        r=1
        lenth=len(s)
        while r < lenth:
            left=s[:l+1]
            right=s[r:]
            ladd=0
            radd=0
            for i in left:
                if i =='0':
                    ladd+=1
            for i in right:
                if i == '1':
                    radd+=1
            if max_score < ladd+radd:
                max_score=ladd+radd
            l+=1
            r+=1
        return max_score

        