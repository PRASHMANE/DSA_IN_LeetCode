class Solution:
    def totalFruit(self, fruits: List[int]) -> int:

        left=0
        right=0
        n= len(fruits)
        hsh={}
        maxlen=0

        while right < n:
            hsh[fruits[right]]=hsh.get(fruits[right],0)+1

            if len(hsh) > 2:
                hsh[fruits[left]]-=1
                if hsh[fruits[left]] == 0:
                    del hsh[fruits[left]]
                left+=1
            if len(hsh) <= 2:
                maxlen=max(maxlen,right-left+1)
            right+=1
        return maxlen

        