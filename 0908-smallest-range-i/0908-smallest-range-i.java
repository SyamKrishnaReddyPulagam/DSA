class Solution {
    public int smallestRangeI(int[] nums, int k) {
        int max_1=nums[0];
        int min_1=nums[0];
        for(int i=0;i<nums.length;i++){
            max_1=Math.max(max_1,nums[i]);
            min_1=Math.min(min_1,nums[i]);
        }
        return Math.max(0, max_1-min_1 - 2*k);
    }
}