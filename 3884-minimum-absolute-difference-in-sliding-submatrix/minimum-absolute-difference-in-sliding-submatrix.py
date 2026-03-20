#python3
class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        ans = [[0] * (n - k + 1) for _ in range(m - k + 1)]
        vals = [0] * (k * k)
        for i in range(m - k + 1):
            for j in range(n - k + 1):
                idx = 0
                for r in range(k):
                    for c in range(k):
                        vals[idx] = grid[i + r][j + c]
                        idx += 1
                vals.sort()
                min_diff = float('inf')
                for x in range(1, len(vals)):
                    if vals[x] != vals[x - 1]:
                        diff = vals[x] - vals[x - 1]
                        if diff < min_diff:
                            min_diff = diff
                ans[i][j] = 0 if min_diff == float('inf') else min_diff
        return ans