class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer,Integer> hsh = new HashMap<>();
        for(int i = 0; i<nums.length;i++){
            int val = target-nums[i];
            if (hsh.containsKey(val)){
                return new int[] {hsh.get(val),i};
            }
            hsh.put(nums[i],i);
        }
        return new int[] {0,0};
    }
}