class Solution:
    def jump(self, nums: List[int]) -> int:
        def func(arr):
            z=float("inf")
            for i in arr:
                if i>0:
                    z=min(z,i)
            return z
        n=len(nums)
        if n==1:
            return 0
        if n==2:
            return 1
        dp=[0]*n
        if nums[-2]>=1:
            dp[-2]=1
        for i in range(n-3,-1,-1):
            if nums[i]>=n-1-i:
                dp[i]=1
            elif nums[i]==0:
                continue
            else:
                z=func(dp[i+1:i+nums[i]+1])
                dp[i]=z+1
        return dp[0]