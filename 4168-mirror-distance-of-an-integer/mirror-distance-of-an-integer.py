class Solution:
    def mirrorDistance(self, n: int) -> int:
        temp = n
        mirror = 0

        while temp > 0:
            dig = temp % 10
            mirror = mirror * 10 + dig
            temp = temp // 10
        return abs(mirror - n)
