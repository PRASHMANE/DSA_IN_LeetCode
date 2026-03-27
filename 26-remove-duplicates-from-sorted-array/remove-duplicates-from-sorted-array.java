class Solution {
    public int removeDuplicates(int[] nums) {
        Set<Integer> set = new LinkedHashSet<>();
        for(int i=0 ; i < nums.length ; i++){
            set.add(nums[i]);
        }

        int ind = 0;

        for(int i : set){
            nums[ind++] = i;
        }

        return ind;
        
    }
}