class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        n=len(nums)
        if len(nums)==1:
            return nums[0]
        else:
            while n!=1:
                for i in range(len(nums)-1):
                    nums[i]=(nums[i]+nums[i+1])%10
                n-=1
        return nums[0]