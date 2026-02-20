class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        n = len(mat)
        m = len(mat[0])

        if r * c != n * m:
            return mat
        
        ans = [[0]*c for _ in range(r)]

        st = []
        for i in range(n):
            for j in range(m):
                st.append(mat[i][j])

        track = 0
        for i in range(r):
            for j in range(c):
                ans[i][j] = st[track]
                track += 1

        return ans