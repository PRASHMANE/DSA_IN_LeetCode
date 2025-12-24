class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        cho=0
        temp=money
        for i in prices:
            if i <= temp and temp > -1 and cho < 2:
                cho+=1
                temp -= i
            if cho == 2 and temp > -1:
                return temp
        return money

        