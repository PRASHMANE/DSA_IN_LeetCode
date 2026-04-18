class Solution {
    public List<Integer> majorityElement(int[] nums) {

        int n = nums.length;

        Map<Integer,Integer> hsh = new HashMap<>();

        for(int num : nums){
            hsh.put(num,hsh.getOrDefault(num,0)+1);
        }

        List<Integer> ans = new ArrayList<>();

        for(int key : hsh.keySet()){
            if (hsh.get(key) > n / 3){
                ans.add(key);
            }
        }


        return ans;
        
    }
}