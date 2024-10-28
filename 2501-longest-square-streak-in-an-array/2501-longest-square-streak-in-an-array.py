class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        temp=set(nums)
        ans=0
        for i in nums:
            count,cur=1,i
            while cur**2 in temp:
                count+=1
                cur=cur**2
            ans=max(ans,count)
        if ans==1:
            return -1
        return ans