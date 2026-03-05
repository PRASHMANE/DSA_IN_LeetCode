class Solution:
    def minOperations(self, s: str) -> int:
        n=len(s)
        zero_start = ""
        for i in range(n):
            if i % 2 == 0:
                zero_start+="0"
            else:
                zero_start+="1"
        
        one_start=""
        for i in range(n):
            if i % 2 == 0:
                one_start+="1"
            else:
                one_start+="0"
        
        min_val=float("inf")

        count=0
        for i , j in zip(s,zero_start):
            if i != j:
                count+=1
        
        min_val=min(min_val,count)

        count = 0
        for i , j in zip(s,one_start):
            if i != j:
                count+=1
        
        return min(min_val,count)