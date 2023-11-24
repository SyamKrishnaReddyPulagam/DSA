class Solution {
    public boolean canJump(int[] nums) {
        int n=nums.length-1;
        int z=n;
        for(int i=n;i>-1;i--){
            if(i+nums[i]>=z){
                z=i;
            }
        }
        if(z==0){
            return true;
        }
        return false;
    }
}