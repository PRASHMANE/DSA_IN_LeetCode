class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        max_count=0
        ind=0
        n = len(mat)
        m = len(mat[0])
        for i in range(n):
            count=0
            for j in range(m):
                if mat[i][j] == 1:
                    count+=1
            if count > max_count:
                max_count=count
                ind=i
        return [ind,max_count]