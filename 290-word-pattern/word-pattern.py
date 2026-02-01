class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        return [pattern.index(c) for c in pattern] == [words.index(c) for c in words]