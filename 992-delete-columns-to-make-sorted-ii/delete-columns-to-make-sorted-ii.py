class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n=len(strs)
        m=len(strs[0])

        deleted=0
        sorted_rows=[False]*(n-1)

        for col in range(m):
            for row in range(n-1):
                if not sorted_rows[row] and strs[row][col]>strs[row+1][col]:
                    deleted+=1
                    break
            else:
                for row in range(n-1):
                    if strs[row][col]<strs[row+1][col]:
                        sorted_rows[row]=True
        return deleted
        