class Solution:
    def countLargestGroup(self, n: int) -> int:
        cnt = Counter()
        
        # Count how many numbers have each digit-sum
        for i in range(1, n + 1):
            s = 0
            temp = i
            while temp > 0:
                s += temp % 10
                temp //= 10
            cnt[s] += 1
        
        # Find the largest group size
        max_size = max(cnt.values())
        # Count how many digit sums have that largest size
        return sum(1 for v in cnt.values() if v == max_size)