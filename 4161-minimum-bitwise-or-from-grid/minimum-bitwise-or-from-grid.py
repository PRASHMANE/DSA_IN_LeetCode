class Solution:
    def minimumOR(self, grid: List[List[int]]) -> int:
        ans=0
        for i in range(30,-1,-1):
            mask=ans| ((1<<i)-1)
            possible = True
            for row in grid:
                row_ok=False
                for val in row:
                    if (val|mask)==mask:
                        row_ok=True
                        break
                if not row_ok:
                    possible=False
                    break
            if not possible:
                ans |= (1<<i)
        return ans