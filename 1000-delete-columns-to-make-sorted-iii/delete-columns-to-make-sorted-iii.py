class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs[0])
        m = len(strs)

        dp = [1]*n

        for i in range(n):
            for j in range(i):
                if all(strs[r][j] <= strs[r][i] for r in range(m)):
                    dp[i] = max(dp[i],dp[j]+1)
        return n-max(dp)
