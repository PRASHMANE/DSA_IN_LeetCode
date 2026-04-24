class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:

        count = Counter(moves)
        if count.get("R",0) == 0 and count.get("L",0)==0:
            return len(moves)
        elif count.get("R",0) > count.get("L",0):
            val = "R"
        else:
            val = "L"
        
        temp = ""

        for i in moves:
            if i == "_":
                temp+=val
            else:
                temp+=i
        
        
        count1= Counter(temp)

        return abs(count1.get("L",0)-count1.get("R",0))


        