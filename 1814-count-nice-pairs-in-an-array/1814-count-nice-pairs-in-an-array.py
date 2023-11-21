class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        mod=(10**9)+7
        def reversed(num):
            return int(str(num)[::-1])
        n=len(nums)
        dicti={}
        ans=0
        for i in range(n):
            nums[i]=nums[i]-reversed(nums[i])
            if nums[i] in dicti:
                ans+=dicti[nums[i]]
                dicti[nums[i]]+=1
            else:
                dicti[nums[i]]=1
        return ans%mod