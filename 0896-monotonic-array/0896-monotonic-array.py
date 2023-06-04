class Solution(object):
    def isMonotonic(self, nums):
        a=1
        b=1
        for i in range(1,len(nums)):
            if nums[i-1]<nums[i]:
                a+=1
            elif nums[i-1]>nums[i]:
                b+=1
            else:
                a+=1
                b+=1
        if a==len(nums) or b==len(nums):
            return True
        return False
        