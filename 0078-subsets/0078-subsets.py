class Solution(object):
    def subsets(self, nums):
        result = [[]]
        for n in nums:
            for i in range(len(result)):
                result.append(result[i]+[n])
        return result