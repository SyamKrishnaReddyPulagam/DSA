class Solution(object):
    def minOperations(self, nums):
        if len(nums)==1:
            return 0
        n=len(nums)
        inc=0
        prev=nums[0]
        for i in range(1,n):
            if nums[i]<prev:
                k=prev-nums[i]
                inc+=k+1
                nums[i]=prev+1
                prev=nums[i]
            elif nums[i]==prev:
                nums[i]+=1
                inc+=1
            prev=nums[i]
        return inc