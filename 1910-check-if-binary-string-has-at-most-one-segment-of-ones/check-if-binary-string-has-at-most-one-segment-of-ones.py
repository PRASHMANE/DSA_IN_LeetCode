class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        return ((n := len(s)) - 1 - s[::-1].index("1") < (s.index("0") if "0" in s else n))