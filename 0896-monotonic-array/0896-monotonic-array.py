class Solution(object):
    def isMonotonic(self, nums):
        if nums==sorted(nums) or nums==sorted(nums)[::-1]:
            return True
        return False