class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        mod=(10**9)+7
        def reversed(num):
            return int(str(num)[::-1])
        n=len(nums)
        for i in range(n):
            nums[i]=nums[i]-reversed(nums[i])
        dicti=Counter(nums)
        ans=0
        for i in dicti.values():
            ans+=((i)*(i-1))//2
        return ans%mod