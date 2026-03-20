class Solution {
    public int majorityElement(int[] nums) {

        int n = nums.length;
        Map<Integer,Integer> hsh = new HashMap<>();
        for (int i=0 ; i<n ; i++){
            hsh.put(nums[i],hsh.getOrDefault(nums[i],0)+1);
        }

        for (Map.Entry<Integer,Integer> ent : hsh.entrySet()){
            if(ent.getValue() > n/2 ){
                return ent.getKey();
            }
        }
        return 0;
        
    }
}