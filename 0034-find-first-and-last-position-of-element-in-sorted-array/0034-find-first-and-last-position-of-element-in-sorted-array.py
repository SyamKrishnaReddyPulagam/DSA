class Solution(object):
    def searchRange(self, nums, target):
        if target not in nums: 
            return [-1,-1]
        else : 
            return [nums.index(target),nums.index(target) + nums.count(target) - 1]