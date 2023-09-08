class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        else:
            for i in range(len(nums)-1):
                for i in range(len(nums)-1):
                    nums[i]=nums[i]+nums[i+1]
                    if nums[i]>9:
                        nums[i]=nums[i]-10
        return nums[0]