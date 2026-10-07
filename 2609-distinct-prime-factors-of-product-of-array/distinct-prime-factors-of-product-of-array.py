from math import prod

class Solution:
    def distinctPrimeFactors(self, nums: list[int]) -> int:
        def spf(n):
            fact = set()
            p = 2
            while p*p <= n:
                while n%p == 0:
                    fact.add(p)
                    n//=p
                p+=1
            if n > 1:
                fact.add(n)
            return len(fact)
        

        n = prod(nums)
        return spf(n)
        