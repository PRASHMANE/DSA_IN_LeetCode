class Solution:
    def countPrimes(self, n: int) -> int:
        if n > 2:
            is_prime = [True] * (n)
            is_prime[0] = False
            is_prime[1] = False
            count=1
        else:
            return 0

        p = 2
        while p*p <= n:
            if is_prime:
                for mul in range(p*p,n,p):
                    is_prime[mul]=False
                p+=1
        return sum(is_prime)
        