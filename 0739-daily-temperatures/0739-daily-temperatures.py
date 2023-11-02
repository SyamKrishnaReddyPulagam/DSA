class Solution:
    def dailyTemperatures(self, nums: List[int]) -> List[int]:
        n=len(nums)
        ans=[0]*n
        stack=[]
        for i in range(n):
            while stack and nums[i]>nums[stack[-1]]:
                ans[stack[-1]]=(i-stack[-1])
                stack.pop()
            stack.append(i)
        return ans