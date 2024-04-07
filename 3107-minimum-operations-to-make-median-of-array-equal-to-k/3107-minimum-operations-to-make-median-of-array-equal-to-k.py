class Solution:
    def minOperationsToMakeMedianK(self, nums: List[int], k: int) -> int:
        nums.sort()
        n=len(nums)
        ans=abs(nums[n//2]-k)
        nums[n//2]=k
        if nums[n//2]>nums[n//2-1]: #goto right
            i=n//2+1
            while i<n:
                if nums[i]<k:
                    ans+=abs(nums[i]-k)
                i+=1
        elif nums[n//2]< nums[n//2-1]: #goto left
            i=n//2-1
            while i>=0:
                if nums[i]>k:
                    ans+=abs(nums[i]-k)
                i-=1
        return ans