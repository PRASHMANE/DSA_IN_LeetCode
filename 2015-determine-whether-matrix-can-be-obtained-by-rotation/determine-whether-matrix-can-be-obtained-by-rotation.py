class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:

        def rotate(mat):
            n = len(mat)

            com = [[0]*n for _ in range(n)]

            for i in range(n):
                for j in range(n):
                    com[j][n-1-i] = mat[i][j]
            
            return com
        
        def compare(mat,target):
            n=len(mat)
            for i in range(n):
                for j in range(n):
                    if mat[i][j] != target[i][j]:
                        return False
            
            return True
            
        
        for _ in range(4):
            ans = compare(mat,target)
            if ans :
                return True
            mat = rotate(mat)
        
        return False
            
                

        