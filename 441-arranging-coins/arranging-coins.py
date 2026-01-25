class Solution:
    def arrangeCoins(self, n: int) -> int:
        count=0
        temp=1
        while True:
            if temp <= n:
                count+=1
                n-=temp
            else:
                break
            temp+=1
        return count

            
            
        