class Solution:
    def numSteps(self, s: str) -> int:
        count=0
        val=int(s,2)

        while val != 1:
            if val % 2 != 0:
                count+=1
                val+=1
            else:
                count+=1
                val=val//2
        return count
        