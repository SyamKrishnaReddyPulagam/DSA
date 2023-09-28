class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        ans=[0]*len(nums)
        start=0
        end=len(nums)-1
        for i in nums:
            if i%2==0:
                ans[start]=i
                start+=1
            else:
                ans[end]=i
                end-=1
        return ans