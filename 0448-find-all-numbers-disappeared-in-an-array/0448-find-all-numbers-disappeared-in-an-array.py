class Solution(object):
    def findDisappearedNumbers(self, nums):
        nums1=[]
        for i in range(1,len(nums)+1):
            nums1.append(i)
        return set(nums1).difference(nums)