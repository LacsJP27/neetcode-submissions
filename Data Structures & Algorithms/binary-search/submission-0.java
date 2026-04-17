class Solution {
    public int search(int[] nums, int target) {
          return binarySearch(0, nums.length - 1, target, nums);
    }

    public int binarySearch(int left, int right, int target, int[] nums){
        if (left > right) return -1;
        int mid = left + (right - left) / 2;
        if(nums[mid] == target) return mid;
        return (target > nums[mid]) ? binarySearch(mid + 1, right, target, nums) :
            binarySearch(left, mid - 1, target, nums);
    }
}
