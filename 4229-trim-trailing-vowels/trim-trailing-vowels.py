class Solution:
    def trimTrailingVowels(self, s: str) -> str:
        vo={'a','e','i','o','u'}
        i=len(s)-1

        while i>=0 and s[i] in vo:
            i-=1
        return s[:i+1]