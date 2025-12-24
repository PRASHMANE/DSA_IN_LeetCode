class Solution {
    public int minimumBoxes(int[] apple, int[] capacity) {
        int ans=0;
        int val= 0,sum=0;
        for(int i : apple){
            sum+=i;
        }
        
        Arrays.sort(capacity);

        for (int i= capacity.length-1;i>=0;i--){
            val+=capacity[i];
            if(val>=sum){
                ans++;
                return ans;
            }else ans++;
        }
        return ans;
    }
}