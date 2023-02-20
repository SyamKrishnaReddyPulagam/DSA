class Solution(object):
    def searchInsert(self, nums, target):
        start=0
        end=len(nums)-1
        ind=-1
        while start<=end:
            mid=start+(end-start)/2
            if nums[mid]>target:
                end=mid-1
            elif nums[mid]<target:
                ind=mid
                start=mid+1
            else:
                return mid
        return ind+1
        