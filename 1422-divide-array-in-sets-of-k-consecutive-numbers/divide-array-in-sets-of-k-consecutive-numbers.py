from collections import Counter
class Solution:
    def isPossibleDivide(self,nums, k):
        if len(nums) % k != 0:
            return False

        freq = Counter(nums)
        for num in sorted(freq):
            count = freq[num]
            if count > 0:
                for i in range(num, num + k):
                    if freq[i] < count:
                        return False
                    freq[i] -= count
        return True
