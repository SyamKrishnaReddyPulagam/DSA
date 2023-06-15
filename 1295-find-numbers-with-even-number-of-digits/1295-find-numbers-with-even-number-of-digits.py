class Solution(object):
    def findNumbers(self, nums):
        return sum((len(str(i))) % 2 == 0 for i in nums)