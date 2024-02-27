class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans=[]
        i,j=0,0
        n=len(nums)
        temp=0
        while i<n and j<n:
            temp+=nums[j]
            if temp>=target:
                while temp>=target:
                    ans.append(j-i+1)
                    temp-=nums[i]
                    i+=1
            j+=1
        if not ans:
            return 0
        return min(ans)