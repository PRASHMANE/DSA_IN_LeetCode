class Solution {
    public boolean judgeCircle(String moves) {
        int upper = 0;
        int lower = 0;
        int right = 0;
        int left = 0;

        for (char ch : moves.toCharArray()){
            if (ch == 'U')upper++;
            else if(ch == 'D')lower++;
            else if(ch == 'L')left++;
            else{
                right++;
            }
        }

        if(Math.abs(upper-lower) != 0 || Math.abs(right-left) != 0){
            return false;
        }

        return true;
        
    }
}