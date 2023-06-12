class Solution(object):
    def summaryRanges(self, nums):
        ret=[]
        save=""
        for i in range(len(nums)):
            if i<=len(nums)-2 and nums[i+1]==nums[i]+1:
                if save=="": save=str(nums[i])+"->"
            else:
                ret.append(save+str(nums[i]))
                save=""
        return ret