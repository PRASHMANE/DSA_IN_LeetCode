class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        arr = [row[y:y+k] for row in grid[x:x+k]][::-1]
        row=0
        for i in range(x,x+k):
            col=0
            for j in range(y,y+k):
                grid[i][j] = arr[row][col]
                col+=1
            row+=1

        return grid

        