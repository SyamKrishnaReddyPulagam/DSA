class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix=1
        pre=[0]*len(nums)
        for i in range(len(nums)):
            prefix*=nums[i]
            pre[i]=prefix
        postfix=1
        post=[0]*len(nums)
        for i in range(len(nums)-1,-1,-1):
            postfix*=nums[i]
            post[i]=postfix
        res=[0]*len(nums)
        res[0]=post[1]
        res[-1]=pre[-2]
        for i in range(1,len(res)-1):
            res[i]=pre[i-1]*post[i+1]
        return res
        
        
        
        
        
        
        """x=1
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
            
        return nums"""
        
        