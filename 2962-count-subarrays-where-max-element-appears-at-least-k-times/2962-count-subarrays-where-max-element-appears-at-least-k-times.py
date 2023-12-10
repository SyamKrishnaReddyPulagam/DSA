class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n=len(nums)
        maxi=max(nums)
        left,right=0,0
        mcount=0
        ans=0
        while right<n:
            if nums[right]==maxi:
                mcount+=1
            if mcount>=k:
                while mcount>=k:
                    ans+=n-right
                    if nums[left]==maxi:
                        mcount-=1
                    left+=1
            right+=1
        return ans