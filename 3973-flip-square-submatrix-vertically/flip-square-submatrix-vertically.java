class Solution {
    public int[][] reverseSubmatrix(int[][] grid, int x, int y, int k) {

        int[][] arr = new int[k][k];
        int row = 0;
        for (int i = x ; i < x+k ;i++){
            int col =0;
            for (int j = y ; j< y+k ; j++){
                arr[row][col]=grid[i][j];
                col++;
            }
            row++;
        }

        row = k-1;
        for (int i = x ; i < x+k ;i++){
            int col =0;
            for (int j = y ; j< y+k ; j++){
                grid[i][j]=arr[row][col];
                col++;
            }
            row--;
        }

        return grid;

        
    }
}