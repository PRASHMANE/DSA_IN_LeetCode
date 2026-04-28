class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        count = Counter(s)
        n = len(s)
        return int((count[letter] / n) * 100)
    