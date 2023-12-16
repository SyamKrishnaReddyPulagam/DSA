class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        n=len(nums)
        if k>=n:
            return n
        l,r=0,0
        ans=0
        dicti={}
        while r<n:
            if nums[r] in dicti:
                dicti[nums[r]]+=1
                if dicti[nums[r]]>k:
                    ans=max(ans,r-l)
                    while dicti[nums[r]]>k:
                        dicti[nums[l]]-=1
                        l+=1
            else:
                dicti[nums[r]]=1
            r+=1 
        ans=max(ans,r-l)
        return ans