class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = set()
        col = set()

        n =len(matrix)
        m = len(matrix[0])

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    row.add(i)
                    col.add(j)
        
        for i in list(row):
            for j in range(m):
                matrix[i][j] = 0

        for i in range(n):
            for j in list(col):
                matrix[i][j] = 0

        return matrix 
