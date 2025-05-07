class Solution:
    def maxProduct(self, n: int) -> int:
        dig1,dig2=nlargest(2,list(map(int,str(n))))
        return dig1*dig2