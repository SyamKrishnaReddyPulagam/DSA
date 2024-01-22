class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        dicti={}
        n=len(nums)
        for i in range(1,n+1):
            dicti[i]=0
        for i in nums:
            dicti[i]+=1
        ans=[0,0]
        for i in dicti:
            if dicti[i]==2:
                ans[0]=i
            if dicti[i]==0:
                ans[1]=i
        return ans