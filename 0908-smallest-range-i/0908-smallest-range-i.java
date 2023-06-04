class Solution {
    public int smallestRangeI(int[] nums, int k) {
        if (nums.length==0 || nums.length==1){
            return 0;
        }
        Arrays.sort(nums);
        return Math.max(0, nums[nums.length-1] - nums[0] - 2*k);
    }
}