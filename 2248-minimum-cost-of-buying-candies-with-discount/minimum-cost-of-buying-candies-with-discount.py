class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        cost.sort(reverse = True)
        n = len(cost)
        right = n-1
        left = 0
        ans = 0

        if n == 1:
            return cost[0]

        while left < n:
            flage = True

            for i in range(2):
                if left < n:
                    ans+=cost[left]
                    left+=1
                else:
                    flage = False
                    break
            
            if flage:
                left+=1
        
        return ans