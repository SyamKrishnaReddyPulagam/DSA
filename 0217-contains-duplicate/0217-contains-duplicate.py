class Solution(object):
    def containsDuplicate(self, nums):
        nums1=set(nums)
        x=len(nums)
        y=len(nums1)
        if x==y:
            return False
        else:
            return True