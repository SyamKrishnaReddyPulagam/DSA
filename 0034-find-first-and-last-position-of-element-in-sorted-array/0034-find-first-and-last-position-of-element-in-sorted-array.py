class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def firstele(nums,k):
            i,j=0,len(nums)-1
            while i<=j:
                mid=(i+j)//2
                if nums[mid]==k:
                    if mid==0 or nums[mid-1]!=k:
                        return mid
                    else:
                        j=mid-1
                elif nums[mid]>k:
                    j=mid-1
                else:
                    i=mid+1
            return -1
        m=firstele(nums,target)
        while m<len(nums)-1 and nums[m+1]==target:
            m+=1
        return firstele(nums,target),m