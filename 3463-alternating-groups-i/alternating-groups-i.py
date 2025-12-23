class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        n=len(colors)
        count=0
        for i in range(n):
            if colors[(i+1)%n] != colors[i] and colors[(i-1+n)%n] != colors[i]:
                count+=1
        return count 
        