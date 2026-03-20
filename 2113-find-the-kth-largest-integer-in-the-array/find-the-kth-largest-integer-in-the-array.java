class Solution {
    public String kthLargestNumber(String[] nums, int k) {
        Arrays.sort(nums, (a, b) -> {
            // 2 --> Sort based on lengths first
            if (a.length() != b.length()) {
                // 1 --> Larger length == Larger number (since no leading zeros)
                return Integer.compare(a.length(), b.length());
            }
            // 3 --> If lengths are equal, compare the string values (lexicographically)
            return a.compareTo(b); 
        });
        
        // 4 --> Return the kth largest element (at index n-k in ascending sort)
        return nums[nums.length - k];
    }
}