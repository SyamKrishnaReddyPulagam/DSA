class Solution(object):
    def dominantIndex(self, nums):
        nums1=[]
        for i in nums:
            nums1.append(i)
        nums1.sort()
        x=nums1[len(nums)-1]
        y=nums1[len(nums)-2]
        if x>=y*2:
            return nums.index(x)
        return -1