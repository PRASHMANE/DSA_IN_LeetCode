class Solution {
    public boolean compare(int[][] mat,int[][] target){

        int n = mat.length;
        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                if(mat[i][j] != target[i][j]){
                    return false;
                }
            }
        }
        return true;

    }

    public int[][] routate(int[][] mat){
        int n = mat.length;
        int[][] com = new int[n][n];
        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                com[j][n-1-i] = mat[i][j];
            }
        }
        return com;
    }
    public boolean findRotation(int[][] mat, int[][] target) {

        for(int i=0 ;i<4;i++){
            boolean ans = compare(mat,target);
            if (ans == true){
                return true;
            }
            mat = routate(mat);
        }

        return false;   
    }
}