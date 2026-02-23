class Solution:
    def checkRecord(self, s: str) -> bool:

        count = Counter(s)

        if count["A"] < 2:
            
            if "LLL" in s:
                return False
        else:
            return False


        return True
        