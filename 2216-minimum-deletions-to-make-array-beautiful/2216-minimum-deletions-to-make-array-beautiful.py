class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        op=0
        for i in range(len(nums)):
            if (i+op)%2==0 and i+1<len(nums) and nums[i]==nums[i+1]:
                op+=1
        if (len(nums)-op)%2!=0:
            op+=1
        return op