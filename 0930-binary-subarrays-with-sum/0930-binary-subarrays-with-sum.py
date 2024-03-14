class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def func(arr,goal):
            if goal<0:
                return 0
            sums,ans=0,0
            left,right=0,0
            while left<len(arr) and right<len(arr):
                sums+=arr[right]
                while sums>goal:
                    sums-=arr[left]
                    left+=1
                ans+=right-left+1
                right+=1
            return ans
        return func(nums,goal)-func(nums,goal-1)