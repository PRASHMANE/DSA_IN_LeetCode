class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        ans = -1
        n = len(colors)

        for i in range(n):
            for j in range(i,n):
                if colors[i] != colors[j]:
                    ans = max(ans,abs(i-j))
        return ans

        