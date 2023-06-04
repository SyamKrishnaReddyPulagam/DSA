class Solution(object):
    def sortArrayByParity(self, nums):
        size = len(nums)
        res = [None] * size
        start = 0
        end = size - 1
        for val in nums:
            if val % 2 == 1:
                res[end] = val
                end = end -1
            else:
                res[start] = val
                start = start + 1
        return res