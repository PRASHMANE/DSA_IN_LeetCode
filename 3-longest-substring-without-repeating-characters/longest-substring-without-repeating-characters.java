class Solution {
    public int lengthOfLongestSubstring(String s) {

        Map<Character,Integer> hsh = new HashMap<>();
        int max_val = 0;

        int left = 0;

        for (int right = 0 ; right < s.length();right++){
            char ch = s.charAt(right);
            hsh.put(ch,hsh.getOrDefault(ch,0)+1);

            while (hsh.get(ch) > 1){
                char ch1 = s.charAt(left);
                hsh.put(ch1,hsh.get(ch1) - 1);
                
                if (hsh.get(ch1) == 0){
                    hsh.remove(ch1);
                }
                //hsh.put(s[left],get(l) - 1);
                left++;
            }

            max_val = Math.max(max_val,right-left+1);
        }

    return max_val;
        
    }
}