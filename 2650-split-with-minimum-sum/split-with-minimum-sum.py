class Solution:
    def splitNum(self, num: int) -> int:
        digits = sorted(map(int, str(num)))
        num1 = num2 = 0

        for i, d in enumerate(digits):
            if i % 2 == 0:
                num1 = num1 * 10 + d
            else:
                num2 = num2 * 10 + d

        return num1 + num2

        