class Solution(object):
    def findMaxLength(self, nums):
        dicti={0:-1}
        prefix,ans=0,0
        for i in range(len(nums)):
            if nums[i]==0:
                prefix+=-1
            else:
                prefix+=nums[i]
            if prefix not in dicti:
                dicti[prefix]=i
            else:
                ans=max(ans,i-dicti[prefix])
        return ans