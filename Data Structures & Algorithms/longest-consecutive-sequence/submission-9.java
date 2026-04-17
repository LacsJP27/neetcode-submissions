class Solution {
    public int longestConsecutive(int[] nums) {

        //sort array
        //start at the first number 
        // add one to first number
        // check if the next number is equalt to that
        // if not start at the number agin and repeat
        // keep track of a max consequetive numbers
        Arrays.sort(nums);
        System.out.println(Arrays.toString(nums));
        if(nums.length == 1) return 1;
        if(nums.length == 0) return 0;

        int nextNum = nums[0] + 1;
        int result = 0;
        int count = 1;
        for(int i = 1; i < nums.length; ++i) {
            if(nums[i] == nextNum - 1){
                result = Math.max(result, count);
                continue;
            }
            if(nums[i] == nextNum) {
                ++count;
                ++nextNum;
                result = Math.max(result, count);
            } else {
                count = 1;
                if(i == nums.length - 1) break;
                nextNum = nums[i] + 1;
            }
        }
        System.out.println(result);
        return result;
    }
}
