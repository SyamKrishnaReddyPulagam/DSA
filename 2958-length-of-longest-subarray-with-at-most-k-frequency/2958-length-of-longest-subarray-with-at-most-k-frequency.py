class Solution(object):
    def maxSubarrayLength(self, nums, k):
        dicti,ans={},0
        left,right,n=0,0,len(nums)
        if k>=n:
            return n
        while right<n:
            if nums[right] not in dicti:
                dicti[nums[right]]=1
            else:
                dicti[nums[right]]+=1
            while dicti[nums[right]]>k:
                ans=max(ans,right-left)
                dicti[nums[left]]-=1
                left+=1
            right+=1
        ans=max(ans,right-left)
        return ans