class Solution {
    public int[] twoSum(int[] nums, int target) {
        int [] result = new int[2];
        for(int i = 0; i < nums.length; ++i){
            for(int j = 0; j < nums.length; ++j){
                if(j != i && (nums[i] + nums[j] == target)){
                    System.out.print(i);
                    result[1] = i;
                    result[0] = j; 
                }
            }
        }
        return result;    
    }
}
