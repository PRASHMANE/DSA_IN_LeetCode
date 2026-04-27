class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        #bills.sort()
        

        count = {}

        for i in bills:
            if i == 5:
                count[5] = count.get(5,0)+1
            elif i == 10:
                if count.get(5,0) > 0:
                    count[10] = count.get(10,0)+1
                    count[5]-=1
                else:
                    return False
            else:
                if count.get(10,0) > 0 and count.get(5,0) > 0:
                    count[10]-=1
                    count[5]-=1
                elif count.get(5,0) >= 3:
                    count[5]-=3
                else:
                    return False
        return True
