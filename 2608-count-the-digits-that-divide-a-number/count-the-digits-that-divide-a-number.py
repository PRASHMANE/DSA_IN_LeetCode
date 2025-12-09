class Solution:
    def countDigits(self, num: int) -> int:
        cnt=0
        a=num
        while a > 0:
            val=a%10
            if val != 0 and num % val == 0:
                cnt+=1
            
            a=a//10
        return cnt
        