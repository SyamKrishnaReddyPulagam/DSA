class Solution:
    def hIndex(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1 and nums[0]>=1:
            return 1
        if nums[0]>=n:
            return n
        for i in range(n):
            if nums[i]>=n-i:
                return n-i
        return 0