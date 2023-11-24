class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n=len(nums)
        if n==2:
            return nums[0]!=0
        if n==1:
            return True
        i,j=0,n-2
        final=n-1
        while j>=0:
            if nums[j]>=(final-j):
                final=j
            j-=1
        if final==0:
            return True
        return False