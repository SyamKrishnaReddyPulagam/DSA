class Solution {
    public int maxArea(int[] height) {
        int n=height.length;
        int i=0;
        int j=n-1;
        int ans=0;
        int temp=0;
        if(n==2){
            return Math.min(height[0],height[1]);
        }
        while(i<j){
            temp=(Math.min(height[i],height[j]))*(j-i);
            ans=Math.max(ans,temp);
            if(height[i]>=height[j]){
                j--;
            }
            else{
                i++;
            }
        }
        return ans;
    }
}