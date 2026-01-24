class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        row=[""]*numRows
        curr=0
        direction=-1

        for ch in s:
            row[curr] += ch
            if curr == 0 or curr == numRows-1:
                direction*=-1
            curr+=direction

        return "".join(row)