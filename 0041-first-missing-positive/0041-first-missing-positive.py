class Solution(object):
    def firstMissingPositive(self, nums):
        x=1
        y=0
        nums= list(set(nums))
        nums.sort()
        print(nums)
        for i in range(len(nums)):
            if nums[i]<1:
                i+=1
                y+=1
            elif nums[i]!=x:
                print(x)
                return x
            else:
                x+=1
        if y!=0:
            return len(nums)+1-y
        return len(nums)+1