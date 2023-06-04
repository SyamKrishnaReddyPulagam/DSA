class Solution(object):
    def dominantIndex(self, nums):
        nums1=[]
        for i in nums:
            nums1.append(i)
        nums1.sort()
        if nums1[len(nums)-1]>=nums1[len(nums)-2]*2:
            return nums.index(nums1[len(nums)-1])
        return -1