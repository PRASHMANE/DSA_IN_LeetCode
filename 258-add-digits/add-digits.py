class Solution:
    def addDigits(self, num: int) -> int:
        count=0
        sr1=str(num)
        if num == 0:
            return 0
        if num >0 and num<10:
            return num
        def add(arr):
            return str(sum(arr))

        while True:
            if int(sr1) == 0:
                return 0
            if int(sr1) >0 and int(sr1)<10:
                return int(sr1)
            new=[]
            if len(sr1)>=2:
                for i in sr1:
                    new.append(int(i))
                sr1=add(new)
                