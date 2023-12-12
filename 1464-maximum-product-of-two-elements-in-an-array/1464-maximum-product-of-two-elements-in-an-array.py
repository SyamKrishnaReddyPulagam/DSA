class Solution(object):
    def maxProduct(self, nums):
        first,sec=max(nums[0],nums[1]),min(nums[0],nums[1])
        n=len(nums)
        for i in range(2,n):
            if nums[i]>=first:
                first,sec=nums[i],first
            elif nums[i]<first and nums[i]>sec:
                sec=nums[i]
        return (first-1)*(sec-1)