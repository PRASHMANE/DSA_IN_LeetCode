class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        
        row=len(mat)
        col=len(mat[0])

        left = 0
        right = col - 1

        while left <= right :

            mid = (left+right)//2

            max_row=0
            for r in range(row):
                if mat[r][mid] > mat[max_row][mid]:
                    max_row = r
            
            left_val = mat[max_row][mid-1] if mid-1 >= 0 else -1
            right_val = mat[max_row][mid+1] if mid+1 < col else -1

            if mat[max_row][mid] > left_val and mat[max_row][mid] > right_val:
                return [max_row,mid]
            elif right_val > mat[max_row][mid]:
                left = mid+1
            else:
                right=mid-1

        return [-1,-1] 