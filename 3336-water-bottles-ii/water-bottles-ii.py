class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        full = numBottles
        empty = 0
        cost = numExchange
        ans = 0

        while full > 0:
            # drink all full bottles
            ans += full
            empty += full
            full = 0

            # exchange if possible
            if empty >= cost:
                empty -= cost
                full += 1
                cost += 1

        return ans
