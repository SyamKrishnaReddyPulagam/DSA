class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        n=len(nums)
        target=sum(nums)-x
        cursum,l=0,0
        ans=-1
        for r in range(len(nums)):
            cursum+=nums[r]
            
            while l<=r and cursum>target:
                cursum-=nums[l]
                l+=1
            
            if cursum==target:
                ans=max(ans,r-l+1)
        if ans==-1:
            return -1
        return n-ans
        