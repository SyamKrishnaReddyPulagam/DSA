class Solution:
    def countPairs(self, nums: List[int]) -> int:
        hashset=collections.Counter() 
        ans=0
        m=10**9+7
        for i in nums:
            for j in range(22):
                k=(1 << j)-i
                if k in hashset:
                    ans+=hashset[k]
            hashset[i]+=1
        return ans%m