class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        ans=0
        n=len(nums)
        i,j=0,n-1
        while i<=j:
            ans=max(ans,nums[i]+nums[j])
            i,j=i+1,j-1
        return ans