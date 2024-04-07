class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        inc=0
        i,n,prev=1,len(nums),0
        while i<n:
            if nums[i]<=nums[i-1]:
                inc=max(inc,i-prev)
                prev=i
            i+=1
        inc=max(inc,i-prev)
        dec=0
        i,n,prev=1,len(nums),0
        while i<n:
            if nums[i]>=nums[i-1]:
                dec=max(dec,i-prev)
                prev=i
            i+=1
        dec=max(dec,i-prev)
        return max(inc,dec)