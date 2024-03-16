class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        ones,dicti=0,{}
        ans=0
        for i in range(len(nums)):
            if nums[i]==1:
                ones+=1
            if ones-(i+1-ones) not in dicti:
                dicti[ones-(i+1-ones)]=i
            if ones==i+1-ones:
                ans=i+1
            else:
                ans=max(ans,i-dicti[ones-(i+1-ones)])
        return ans