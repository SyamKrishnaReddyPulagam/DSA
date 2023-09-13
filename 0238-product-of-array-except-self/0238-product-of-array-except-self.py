class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        x=1
        y=0
        for i in nums:
            if i==0:
                y+=1
                continue
            x*=i
        if y==0:
            for i in range(len(nums)):
                if nums[i]==0:
                    continue
                nums[i]=x//nums[i]
        else:
            if y==len(nums):
                return nums
            if y>1:
                return [0]*len(nums)
            for i in range(len(nums)):
                if nums[i]==0:
                    nums[i]=x
                else:
                    nums[i]=0
            
        return nums