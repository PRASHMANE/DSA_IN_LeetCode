class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        n = len(matrix)
        m = len(matrix[0])
        count=0
        ans=[]
        for i in range(n):
            for j in range(m):
                ans.append(matrix[i][j])
        ans.sort()
        return ans[k-1]