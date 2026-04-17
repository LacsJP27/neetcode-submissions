class Solution {
    public int[] productExceptSelf(int[] nums) {
      //Create a result array
      // iterate through nums and multiply all th enumbers
      // to the left of the curr index of nums and store in same index in result
      // then go backwards through the nums and multiply everything on the right of the index
        // by what's at the same index in the result
        // return result
    
        int[] res = new int[nums.length];
        int sum = 1;
        for(int i = 0; i < nums.length; ++i) {
            if(i == 0){
                res[i] = sum;
            } else {
                res[i] = nums[i - 1] * sum;
                sum = nums[i - 1] * sum;
            }
        }

        for(int i = nums.length - 1; i >= 0; --i) {
            if(i == nums.length - 1) {
                sum = 1;
            } else {
                sum = nums[i + 1] * sum;
                res[i] = res[i] * sum;
                
            }
        }
        return res;
      
    }
}  
