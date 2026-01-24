class Solution:
    def countSegments(self, s: str) -> int:

        s1=s.split(" ")
        count=0
        for i in s1:
            if i != " " and i != "":
                count+=1
        return count

    
            