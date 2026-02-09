class Solution:
    def totalFruit(self, fruits: List[int]) -> int:

        n=len(fruits)
        left=0
        hsh={}
        maxlen=0

        for right in range(n):
            hsh[fruits[right]]=hsh.get(fruits[right],0)+1

            while len(hsh) > 2:
                hsh[fruits[left]]-=1
                if hsh[fruits[left]]==0:
                    del hsh[fruits[left]]
                left+=1
            
            maxlen=max(maxlen,right-left+1)
        return maxlen

        