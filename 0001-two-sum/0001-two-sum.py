class Solution(object):
    def twoSum(self, nums, target):
        for num in range(len(nums)):
            for number in range(num+1,len(nums)):
                if nums[num] + nums[number] == target:
                    return [num,number]
                           