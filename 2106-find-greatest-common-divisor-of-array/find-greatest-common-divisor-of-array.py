class Solution:
    def findGCD(self, nums: list[int]) -> int:

        def gcd(a,b):
            while b != 0:
                a,b = b,a%b
            return a
        
        a = min(nums)
        b = max(nums)

        return gcd(a,b)
        