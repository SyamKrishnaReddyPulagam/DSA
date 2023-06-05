class Solution(object):
    def sortArrayByParityII(self, nums):
        nums1=[None]*len(nums)
        a=0
        j=1
        while a<len(nums) and j<len(nums):
            for i in range(len(nums)):
                if nums[i]%2==0:
                    nums1[a]=nums[i]
                    a+=2
                else:
                    nums1[j]=nums[i]
                    j+=2
        return nums1