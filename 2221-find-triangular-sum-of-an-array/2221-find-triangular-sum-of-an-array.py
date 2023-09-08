class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        x=0
        if len(nums)==1:
            return nums[0]
        else:
            while len(nums)!=1:
                y=[]
                for i in range(len(nums)-1):
                    x=nums[i+1]+nums[i]
                    if x>9:
                        x=x-10
                    y.append(x)
                nums=y
        return nums[0]