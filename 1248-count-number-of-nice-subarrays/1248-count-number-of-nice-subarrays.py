class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        temp=[1 if i%2!=0 else 0 for i in nums]
        def func(nums,k):
            if k<0:
                return 0
            sums,ans=0,0
            left,right,n=0,0,len(nums)
            while right<n:
                sums+=nums[right]
                while left<=right and sums>k:
                    sums-=nums[left]
                    left+=1
                ans+=right-left+1
                right+=1
            return ans
        #print(func(temp,k),func(temp,k-1))
        return func(temp,k)-func(temp,k-1)