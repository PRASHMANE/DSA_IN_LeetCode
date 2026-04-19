class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        ans=set()
        n = len(grid)*len(grid[0])
        
        for i in grid:
            for j in i:
                if j in ans:
                    rep = j
                ans.add(j)
        total = n*(n+1)//2
        sum_val = sum(list(ans))
        miss = total - sum_val

        return [rep,miss]

        