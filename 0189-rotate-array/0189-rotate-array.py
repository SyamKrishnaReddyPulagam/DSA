class Solution(object):
    def rotate(self, nums, k):
        """
        #using slicling
        k=k%len(nums)
        nums[:]=nums[-k:]+nums[:-k]
        return nums
        """
        x=[0]*len(nums)
        k=k%len(nums)
        for i in range(len(nums)):
            x[(i+k)%len(nums)]=nums[i]
        nums[:]=x[:]
        return nums