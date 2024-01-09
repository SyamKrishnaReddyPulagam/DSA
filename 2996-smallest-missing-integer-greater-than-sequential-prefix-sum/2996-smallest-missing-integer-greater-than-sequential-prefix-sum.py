class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        sums=0
        n=len(nums)
        i,j=0,1
        while j<n:
            if nums[j]!=nums[j-1]+1:
                sums=sum(nums[i:j])
                break
            j+=1
        if sums==0:
            sums=sum(nums)
        while nums:
            if sums in nums:
                sums+=1
            else:
                return sums