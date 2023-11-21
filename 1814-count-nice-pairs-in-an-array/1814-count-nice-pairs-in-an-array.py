class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        mod=(10**9)+7
        def reversed(num):
            return int(str(num)[::-1])
        n=len(nums)
        for i in range(n):
            nums[i]=nums[i]-reversed(nums[i])
        dicti={}
        ans=0
        for i in nums:
            if i in dicti:
                ans+=dicti[i]
                dicti[i]+=1
            else:
                dicti[i]=1
        return ans%mod