class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        ans=[]
        c=0
        for i in range(0,len(prices)-1):
            for j in range(i+1,len(prices)):
                if prices[i]>=prices[j]:
                    ans.append(prices[i]-prices[j])
                    c+=1
                    break
                c=0
            if c==0:
                ans.append(prices[i])
                c=0
        ans.append(prices[-1])
        return ans
