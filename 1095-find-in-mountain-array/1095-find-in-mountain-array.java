/**
 * // This is MountainArray's API interface.
 * // You should not implement it, or speculate about its implementation
 * interface MountainArray {
 *     public int get(int index) {}
 *     public int length() {}
 * }
 */
 
class Solution {
    public int findInMountainArray(int target, MountainArray nums) {
        int length=nums.length();
        int i=1;
        int j=length-2;
        int mid=0;
        while(i<=j){
            mid=(i+j)/2;
            int left=nums.get(mid-1);
            int centre=nums.get(mid);
            int right=nums.get(mid+1);
            if(left<centre && centre<right){
                i=mid+1;
            }
            else if(left>centre && centre>right){
                j=mid-1;
            }
            else{
                break;
            }
        }
        int m=0;
        int n=mid;
        while(m<=n){
            int k=(m+n)/2;
            if(nums.get(k)==target){
                return k;
            }
            else if(nums.get(k)<target){
                m=k+1;
            }
            else{
                n=k-1;
            }
        }
        int a=mid;
        int b=length-1;
        while(a<=b){
            int c=(a+b)/2;
            if(nums.get(c)==target){
                return c;
            }
            else if(nums.get(c)<target){
                b=c-1;
            }
            else{
                a=c+1;
            }
        }
        return -1;
    }
}