class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        max_t=0
        max_f=0
        n=len(answerKey)
        left=0
        count=0

        for right in range(n):
            if answerKey[right] == "F":
                count+=1
            
            while count > k:
                if answerKey[left] == "F":
                    count-=1
                left+=1
            
            max_t=max(max_t,right-left+1)
        
        left=0
        count=0

        for right in range(n):
            if answerKey[right] == "T":
                count+=1
            
            while count > k:
                if answerKey[left] == "T":
                    count-=1
                left+=1
            
            max_f=max(max_f,right-left+1)
        
        return max(max_t,max_f)
