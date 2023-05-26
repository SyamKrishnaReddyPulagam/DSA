class Solution(object):
    def moveZeroes(self, nums):
        j=0
        for i in nums:
            if i!=0:
                nums[j]=i
                j+=1
        while(j<len(nums)):
            nums[j]=0
            j+=1
        return nums