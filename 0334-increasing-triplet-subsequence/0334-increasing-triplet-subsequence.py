class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        x=sorted(nums)
        if x[::-1]==nums:
            return False
        leftmin=[0]*len(nums)
        leftmin[0]=nums[0]
        for i in range(1,len(nums)):
            leftmin[i]=min(leftmin[i-1],nums[i])
        rightmin=[0]*len(nums)
        rightmin[-1]=nums[-1]
        for i in range(len(nums)-2,-1,-1):
            rightmin[i]=max(rightmin[i+1],nums[i])
        for i in range(len(nums)):
            if leftmin[i]<nums[i] and rightmin[i]>nums[i]:
                return True
        return False