class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n=len(nums)
        lsum=[0]*n
        rsum=[0]*n
        x=nums[0]
        y=nums[-1]
        for i in range(1,n):
            lsum[i]=x
            x+=nums[i]
        for i in range(n-2,-1,-1):
            rsum[i]=y
            y+=nums[i]
        for i in range(n):
            if lsum[i]==rsum[i]:
                return i
        return -1