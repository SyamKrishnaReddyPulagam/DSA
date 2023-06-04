class Solution(object):
    def sortArrayByParity(self, nums):
        return [i for i in nums if not i % 2] + [i for i in nums if i % 2]