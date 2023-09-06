class Solution(object):
    def rotate(self, nums, k):
        """
        #using slicling
        k=k%len(nums)
        nums[:]=nums[-k:]+nums[:-k]
        return nums
        """
        
        #using an extra array and placing elements with modified indices
        x=[0]*len(nums)
        k=k%len(nums)
        for i in range(len(nums)):
            x[(i+k)%len(nums)]=nums[i]
        nums[:]=x[:]
        return nums
        
        """
        #making inplace change in nums array for each rotation
        #giving time limit exceed error so above methods are best in case
        k=k%len(nums)
        for i in range(k):
            nums[:]=nums[-1:]+nums[:-1]
        return nums
        """