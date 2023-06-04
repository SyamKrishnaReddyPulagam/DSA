class Solution {
    public boolean isMonotonic(int[] nums) {
        int a=1;
        int b=1;
        for(int i=1;i<nums.length;i++){
            if (nums[i-1]<nums[i]){
                a+=1;
            }
            else if (nums[i-1]>nums[i]){
                b+=1;
            }
            else{
                a+=1;
                b+=1;
            }
        }
        if(a==nums.length || b==nums.length){
            return true;
        }
        return false;
    }
}