int searchInsert(int* nums, int numsSize, int target)
{
    int start=0;
    int end=numsSize-1;
    int ind=-1;
    while (start<=end){
        int mid= start+(end-start)/2;
        if (nums[mid]>target){
            end=mid-1;
        }
        else if (nums[mid]<target){
            ind=mid;
            start=mid+1;
        }
        else{
            return mid;
        }
    }
    return ind+1;
}