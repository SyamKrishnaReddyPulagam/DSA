class Solution(object):
    def removeElement(self, nums, val):
        a=0
        for i in range (0,len(nums)):
            if nums[i]!=val:
                nums[a]=nums[i]
                a+=1
            else:
                exit
        return a