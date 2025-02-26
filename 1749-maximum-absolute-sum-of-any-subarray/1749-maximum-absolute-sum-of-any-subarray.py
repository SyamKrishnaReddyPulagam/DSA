class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        dp1,ans1=0,0
        for i in nums:
            dp1=max(dp1+i,i)
            ans1=max(ans1,dp1)
        dp2,ans2=float("inf"),float("inf")
        for i in nums:
            dp2=min(dp2+i,i)
            ans2=min(ans2,dp2)
        return max(ans1,abs(ans2))