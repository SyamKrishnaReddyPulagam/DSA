class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        n=len(nums)
        nums.sort()
        i,j,mod=0,n-1,10**9+7
        ans=0
        while i<=j:
            if nums[i]+nums[j]>target:
                j-=1
            else:
                ans+=pow(2,j-i,mod)
                i+=1
        return ans%mod