class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n=len(nums)
        start,end=0,n-1
        while start<end:
            mid=(start+end)//2
            if nums[mid]>nums[end]:
                start=mid+1
            else:
                end=mid
        if start!=0:
            if target<nums[0] and target>=nums[start]:
                i,j=start,n-1
            else:
                i,j=0,start
        else:
            i,j=0,n-1
        while i<=j:
            k=(i+j)//2
            if nums[k]>target:
                j=k-1
            elif nums[k]<target:
                i=k+1
            else:
                return k
        return -1