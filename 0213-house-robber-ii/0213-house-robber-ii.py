class Solution:
    def rob(self, nums: List[int]) -> int:
        def robbing(nums: List[int]) -> int:
            n=len(nums)
            if n==1:
                return nums[0]
            if n==2:
                return max(nums[0],nums[1])
            dp=[0]*n
            dp[0],dp[1]=nums[0],nums[1]
            dp[2]=dp[0]+nums[2]
            for i in range(3,n):
                dp[i]=max(dp[:i-1])+nums[i]
            return max(dp[-1],dp[-2])
        n=len(nums)
        if n==1:
            return nums[0]
        if n==2:
            return max(nums[0],nums[1])
        z1=robbing(nums[1:])
        z2=robbing(nums[:-1])
        return max(z1,z2)