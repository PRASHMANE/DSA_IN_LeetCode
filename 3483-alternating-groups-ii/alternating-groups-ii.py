class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:

        maxlen=1
        ans=0
        n=len(colors)

        for i in range(1,n+(k-1)):
            if colors[i%n] != colors[(i-1+n)%n] :
                maxlen+=1
            else:
                maxlen = 1
            if maxlen >= k:
                ans += 1
        return ans
        