class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        
        n = len(matrix)

        # Check each row
        for row in matrix:
            if len(set(row)) != n:
                return False

        # Check each column
        for col in zip(*matrix):
            if len(set(col)) != n:
                return False

        return True