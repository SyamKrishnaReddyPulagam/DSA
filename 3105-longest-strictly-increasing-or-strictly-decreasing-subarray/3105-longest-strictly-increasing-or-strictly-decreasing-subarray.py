class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        inc,dec=0,0
        i,n,prev1,prev2=1,len(nums),0,0
        while i<n:
            if nums[i]<=nums[i-1]:
                inc=max(inc,i-prev1)
                prev1=i
            if nums[i]>=nums[i-1]:
                dec=max(dec,i-prev2)
                prev2=i
            i+=1
        inc=max(inc,i-prev1)
        dec=max(dec,i-prev2)
        return max(inc,dec)