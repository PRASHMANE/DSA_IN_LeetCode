class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        ones = s.count('1')
        zeros = len(s) - ones

        # (ones - 1) ones at front, zeros in middle, 1 at end
        return '1' * (ones - 1) + '0' * zeros + '1'
