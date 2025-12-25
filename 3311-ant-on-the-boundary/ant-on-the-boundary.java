class Solution {
    public int returnToBoundaryCount(int[] nums) {
        int prefix=0,ans=0;
        for(int i:nums){
            prefix+=i;
            if(prefix == 0){
                ans++;
            }

        }
        return ans;
        
    }
}