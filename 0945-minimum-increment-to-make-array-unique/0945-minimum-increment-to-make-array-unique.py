class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        dicti=defaultdict(int)
        for i in nums:
            if i in dicti:
                dicti[i]+=1
            else:
                dicti[i]=1
        temp=set(sorted(nums))
        ans=0
        for i in range(min(temp),max(temp)+len(nums)):
            if dicti[i]>1:
                extra=dicti[i]-1
                dicti[i+1]+=extra
                ans+=extra
        return ans