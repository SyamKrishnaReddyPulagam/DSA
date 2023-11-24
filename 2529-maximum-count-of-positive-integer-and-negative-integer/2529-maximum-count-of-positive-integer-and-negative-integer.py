class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        n=len(nums)
        i=0
        while i<n and nums[i]<0:
            i+=1
        #print(i,n-(i)-(nums.count(0)))
        return max(i,n-i-(nums.count(0)))