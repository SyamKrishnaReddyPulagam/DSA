class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans,temp=float("-inf"),1
        for i in nums:
            temp*=i
            ans=max(ans,temp)
            if temp==0:
                temp=1
        temp=1
        for i in range(len(nums)-1,-1,-1):
            temp*=nums[i]
            ans=max(ans,temp)
            if temp==0:
                temp=1
            
        return ans