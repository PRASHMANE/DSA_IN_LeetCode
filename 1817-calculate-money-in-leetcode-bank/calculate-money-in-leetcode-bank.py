class Solution:
    def totalMoney(self, n: int) -> int:
        amount=0
        weekstart=1
        dayofweek=0

        for _ in range(n):
            amount+=weekstart+dayofweek
            dayofweek+=1

            if dayofweek == 7:
                dayofweek=0
                weekstart+=1
        return amount
        