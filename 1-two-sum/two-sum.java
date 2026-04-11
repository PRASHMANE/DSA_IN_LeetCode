class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map <Integer,Integer> hsh = new HashMap<>();
        int val;

        for (int i = 0 ; i < nums.length ; i++){
            val = nums[i];
            if(hsh.containsKey(target-val)){
                return new int[]{i,hsh.get(target-val)};
            }
            hsh.put(val,i);
        }
        return new int[]{-1,-1};
    }
}