class Solution:
    def countSubstrings(self, s: str) -> int:
        
        n = len(s)
        count = 0

        def expand(l, r):
            nonlocal count
            while l >= 0 and r < n and s[l] == s[r]:
                count += 1
                l -= 1
                r += 1

        for i in range(n):
            expand(i, i)     # odd-length palindromes
            expand(i, i + 1) # even-length palindromes

        return count