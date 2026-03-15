class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer,Integer> hsh = new HashMap<>();
        for (int i=0 ;i<nums.length;i++){
            int num = nums[i];
            if (hsh.containsKey(target-num)){
                return new int [] {i,hsh.get(target-num)};
            }
            hsh.put(num,i);
        }

        return new int[]{};
        
    }
}