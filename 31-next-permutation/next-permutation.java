class Solution {

    public void reverse(int start,int end,int[] arr){
        while (start < end){
            int temp = arr[start];
            arr[start] = arr[end];
            arr[end] = temp;

            start++;
            end--;
        }
    }


    public void nextPermutation(int[] nums) {

        int n = nums.length;
        int i = n-2;

        while(i>=0 && nums[i]>=nums[i+1]){
            i--;
        }

        if(i >= 0){
            int j = n-1;
            while(nums[j] <= nums[i]){
                j--;
            }

            int temp = nums[i];
            nums[i]=nums[j];
            nums[j]=temp;
        }

        
        reverse(i+1,n-1,nums);
        
    }
    
}