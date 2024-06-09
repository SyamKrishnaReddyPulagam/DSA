class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        pre,ans=0,0
        dicti=defaultdict(int)
        dicti[0]=1
        for i in nums:
            pre+=i
            rem=pre%k
            ans+=dicti[rem]
            dicti[rem]+=1
        return ans