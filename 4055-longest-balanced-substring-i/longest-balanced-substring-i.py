class Solution:
    def longestBalanced(self, s: str) -> int:

        n = len(s)
        ans = 0
        for i in range(n):
            cnt = [0]*26
            mx = 0
            distinct = 0
            for j in range(i, n):
                idx = ord(s[j]) - ord('a')
                cnt[idx] += 1
                if cnt[idx] == 1:
                    distinct += 1
                mx = max(mx, cnt[idx])
                if mx * distinct == (j - i + 1):
                    ans = max(ans, j - i + 1)
        return ans