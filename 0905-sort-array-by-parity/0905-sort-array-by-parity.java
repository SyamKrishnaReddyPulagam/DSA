class Solution {
    public int[] sortArrayByParity(int[] nums) {
        int size = nums.length;
        int[] newArray = new int[size];
        for (int i = 0; i < size; i++) {
            newArray[i] = 0;
        }
        int start=0;
        int end=size-1;
        for(int i=0;i<size;i++){
            if(nums[i]%2==0){
                newArray[start]=nums[i];
                start+=1;
            }
            else{
                newArray[end]=nums[i];
                end-=1;
            }
        }
        return newArray;
    }
}
