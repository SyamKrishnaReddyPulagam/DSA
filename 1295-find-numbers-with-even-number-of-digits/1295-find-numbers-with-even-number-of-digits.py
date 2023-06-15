class Solution(object):
    def findNumbers(self, nums):
        c=0
        for i in range(len(nums)):
            nums[i]=str(nums[i])
        for j in nums:
            if len(j)%2==0:
                c+=1
        return c