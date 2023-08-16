class Solution(object):
    def findMin(self, nums):
        a,b=0,len(nums)-1
        while a<b:
            c=(a+b)//2
            if nums[c]>nums[b]:
                a=c+1
            else:
                b=c
        return nums[a]