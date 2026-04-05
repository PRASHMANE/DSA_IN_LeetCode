class Solution:
    def judgeCircle(self, moves: str) -> bool:
        hsh={
            "R" : 0,
            "L" : 0,
            "U" : 0,
            "D" : 0
        }

        for i in moves:
            hsh[i]+=1
        
        if abs(hsh["R"] - hsh["L"]) != 0:
            return False
        else:
            if abs(hsh["U"]-hsh["D"]) != 0:
                return False
        return True
        