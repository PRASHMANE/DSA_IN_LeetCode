class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        unique = set()
        n = len(digits)
        for i in range(n):
            # digit for units must be even
            if digits[i] % 2 == 1:
                continue
            for j in range(n):
                if j == i:
                    continue
                for k in range(n):
                    if k == i or k == j:
                        continue
                    # hundreds digit must be non-zero
                    if digits[k] == 0:
                        continue
                    # build the 3-digit number
                    num = digits[k] * 100 + digits[j] * 10 + digits[i]
                    unique.add(num)
        return len(unique)