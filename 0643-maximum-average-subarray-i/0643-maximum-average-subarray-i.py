class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        temp=sum(nums[:k])
        ans=temp
        for i in range(len(nums)-k):
            temp=temp-nums[i]+nums[i+k]
            ans=max(ans,temp)
        return ans/k