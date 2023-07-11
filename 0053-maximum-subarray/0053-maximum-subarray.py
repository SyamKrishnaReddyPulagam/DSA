class Solution(object):
    def maxSubArray(self, nums):
        ans,sums=nums[0],0
        a=0
        b=float('-inf')
        for i in range(len(nums)):
            b=max(b,nums[i])
            a+=nums[i]
            sums+=nums[i]
            ans=max(sums,ans)
            if sums<0:
                sums=0
        return max(ans,b)