class Solution(object):
    def minimumReplacement(self, nums):
        def ceilnotwork(a,b):
            x=a//b
            if a%b==0:
                return x
            else:
                return x+1
        n=len(nums)
        prev=nums[n-1]
        opr=0
        for i in range(n-2,-1,-1):
            if nums[i]>prev:
                k=ceilnotwork(nums[i],prev)
                opr+=k-1
                prev=nums[i]//k
                
            else:
                prev=nums[i]
        return opr