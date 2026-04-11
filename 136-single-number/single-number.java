class Solution {
    public int singleNumber(int[] nums) {
        Map <Integer,Integer> hsh = new HashMap <>();
        for (int i = 0 ; i<nums.length ; i++){
            hsh.put(nums[i],hsh.getOrDefault(nums[i],0)+1);
        }

        for(int i : hsh.keySet()){
            if (hsh.get(i) == 1) return i;
        }

        return -1;
    }
}