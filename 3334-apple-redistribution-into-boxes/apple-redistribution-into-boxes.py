class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        ans=0
        maxlen=1
        val = 0

        capacity.sort(reverse=True)
        tota_appel=sum(apple)

        for i in capacity:
            val+=i
            if val >= tota_appel:
                ans+=1
                return ans
            else:
                ans+=1


        