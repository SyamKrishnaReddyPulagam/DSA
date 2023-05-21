class Solution(object):
    def majorityElement(self, nums):
        for i in set(nums):
            if nums.count(i)>(len(nums)/2):
                return(i) 
        