class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [[1]]

        for _ in range(rowIndex+1):
            dummy_row = [0] + res[-1] + [0]
            row = []

            for i in range(len(res[-1]) + 1):
                row.append(dummy_row[i] + dummy_row[i+1])
            res.append(row)
        
        return res[rowIndex]
