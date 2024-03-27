class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        ans=0
        if k<=1:
            return 0
        i,j,n=0,0,len(nums)
        pro=1
        while j<n:
            pro*=nums[j]
            while pro>=k:
                pro//=nums[i]
                i+=1
            ans+=1+j-i
            j+=1
        return ans