class Solution:
    def maxSubArray(self, nums):
        s = 0 
        maximum = -10001
        for i in range(len(nums)):
            s += nums[i]
            if s > maximum: 
                maximum = s
            if s < 0:
                s = 0
        return maximum